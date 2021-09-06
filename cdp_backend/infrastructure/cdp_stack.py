#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

import pulumi
import pulumi_gcp as gcp
from pulumi_google_native.firebaserules import v1 as firebaserules
from pulumi_google_native.firestore import v1 as firestore

from ..database import DATABASE_MODELS
from ..version import __version__

###############################################################################

PUBLIC_READ_FIRESTORE_RULESET_CONTENT = """
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read;
    }
  }
}
""".strip()

PUBLIC_READ_STORAGE_RULESET_CONTENT = """
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read;
    }
  }
}
""".strip()

###############################################################################


class CDPStack(pulumi.ComponentResource):
    def __init__(
        self,
        gcp_project_id: str,
        firestore_location: str = "us-west2",
        opts: pulumi.ResourceOptions = None,
    ):
        """
        Creates all required infrastructure and enables all required services for CDP
        backend stacks.

        Parameters
        ----------
        gcp_project_id: str
            The id of the gcp_project, the Pulumi stack, and any other required
            names for resources created during infrastructure creation will use this id
            as a prefix.
            I.E. `cdp-seattle` would create a Cloud Firestore instance called
            `cdp-seattle`, a GCP bucket called `cdp-seattle`, etc.

        firestore_location: str
            The location for the Cloud Firestore database and file storage servers
            to be hosted.
            List of locations: https://firebase.google.com/docs/firestore/locations
            Default: "us-west2"

        opts: pulumi.ResourceOptions
            Extra resource options to initialize the entire stack with.
            Default: None

        Notes
        -----
        When using this resource it is recommended to run set Pulumi parallel resource
        creation to five (5) max. GCP has limits on how many resources you can create
        in parallel.
        """
        super().__init__("CDPStack", gcp_project_id, None, opts)

        # Store parameters
        self.gcp_project_id = gcp_project_id
        self.firestore_location = firestore_location

        # Enable all required services
        self.cloudresourcemanager = gcp.projects.Service(
            f"{self.gcp_project_id}-cloudresourcemanager-service",
            disable_dependent_services=True,
            project=self.gcp_project_id,
            service="cloudresourcemanager.googleapis.com",
            opts=pulumi.ResourceOptions(parent=self),
        )
        self.speech_service = gcp.projects.Service(
            f"{self.gcp_project_id}-speech-service",
            disable_dependent_services=True,
            project=self.gcp_project_id,
            service="speech.googleapis.com",
            opts=pulumi.ResourceOptions(
                parent=self, depends_on=[self.cloudresourcemanager]
            ),
        )
        self.firebase_service = gcp.projects.Service(
            f"{self.gcp_project_id}-firebase-service",
            disable_dependent_services=True,
            project=self.gcp_project_id,
            service="firebase.googleapis.com",
            opts=pulumi.ResourceOptions(
                parent=self, depends_on=[self.cloudresourcemanager]
            ),
        )
        self.app_engine_service = gcp.projects.Service(
            f"{self.gcp_project_id}-app-engine-service",
            disable_dependent_services=True,
            project=self.gcp_project_id,
            service="appengine.googleapis.com",
            opts=pulumi.ResourceOptions(
                parent=self, depends_on=[self.cloudresourcemanager]
            ),
        )
        self.firestore_service = gcp.projects.Service(
            f"{self.gcp_project_id}-firestore-service",
            disable_dependent_services=True,
            project=self.gcp_project_id,
            service="firestore.googleapis.com",
            opts=pulumi.ResourceOptions(
                parent=self, depends_on=[self.cloudresourcemanager]
            ),
        )
        self.firebase_rules_service = gcp.projects.Service(
            f"{self.gcp_project_id}-firebase-rules-service",
            disable_dependent_services=True,
            project=self.gcp_project_id,
            service="firebaserules.googleapis.com",
            opts=pulumi.ResourceOptions(
                parent=self, depends_on=[self.cloudresourcemanager]
            ),
        )

        # Create the firestore application
        self.firestore_app = gcp.appengine.Application(
            f"{self.gcp_project_id}-firestore-app",
            project=self.gcp_project_id,
            location_id=self.firestore_location,
            database_type="CLOUD_FIRESTORE",
            opts=pulumi.ResourceOptions(
                parent=self,
                depends_on=[
                    self.firebase_service,
                    self.app_engine_service,
                    self.firestore_service,
                    self.firebase_rules_service,
                ],
            ),
        )

        # Init firebase project
        self.firebase_init = gcp.firebase.Project(
            resource_name=f"{self.gcp_project_id}-firebase-init",
            project=self.gcp_project_id,
            opts=pulumi.ResourceOptions(parent=self, depends_on=[self.firestore_app]),
        )

        # Connect app engine (firestore) + bucket
        self.firebase_project = gcp.firebase.ProjectLocation(
            resource_name=f"{self.gcp_project_id}-firebase-project",
            project=self.gcp_project_id,
            location_id=self.firestore_location,
            opts=pulumi.ResourceOptions(parent=self.firebase_init),
        )

        # TODO:
        # Create rulesets for firestore and storage and release
        for service, ruleset_content in [
            ("firestore", PUBLIC_READ_FIRESTORE_RULESET_CONTENT),
            ("storage", PUBLIC_READ_STORAGE_RULESET_CONTENT),
        ]:
            # Create ruleset
            ruleset_filename = (
                f"projects/{self.gcp_project_id}/"
                f"rulesets/{service}-public-read--cdp-v{__version__}"
            )
            generated_ruleset = firebaserules.Ruleset(
                f"{self.gcp_project_id}-{service}-public-read-rules",
                project=self.gcp_project_id,
                source=firebaserules.SourceArgs(
                    files=[
                        firebaserules.FileArgs(
                            name=ruleset_filename,
                            content=ruleset_content,
                            fingerprint=str(
                                base64.b64encode(__version__.encode("utf-8"))
                            )[2:-1],
                        )
                    ]
                ),
                opts=pulumi.ResourceOptions(parent=self.firebase_project),
            )

            # Store on stack
            ruleset_attr = f"{service}_ruleset"
            setattr(self, ruleset_attr, generated_ruleset)

            # Release ruleset
            release_name = (
                f"projects/{self.gcp_project_id}/"
                f"releases/{service}-public-read-release--cdp-v{__version__}"
            )
            firebaserules.Release(
                f"{self.gcp_project_id}-{service}-public-read-release",
                name=release_name,
                project=self.gcp_project_id,
                ruleset_name=getattr(self, ruleset_attr).name,
                opts=pulumi.ResourceOptions(
                    parent=self.firebase_project,
                    depends_on=[getattr(self, ruleset_attr)],
                ),
            )

        # Create all firestore indexes
        for model_cls in DATABASE_MODELS:
            for idx_field_set in model_cls._INDEXES:

                # Add fields to field list
                idx_set_name_parts = []
                idx_set_fields = []
                for idx_field in idx_field_set.fields:
                    idx_set_name_parts += [idx_field.name, idx_field.order]
                    idx_set_fields.append(
                        firestore.GoogleFirestoreAdminV1IndexFieldArgs(
                            field_path=idx_field.name,
                            order=idx_field.order,
                        )
                    )

                # Finish creating the index set name
                idx_set_name = "_".join(idx_set_name_parts)
                fq_idx_set_name = f"{model_cls.collection_name}-{idx_set_name}"
                firestore.Index(
                    fq_idx_set_name,
                    project=self.gcp_project_id,
                    database_id="(default)",
                    collection_group_id=model_cls.collection_name,
                    fields=idx_set_fields,
                    query_scope="COLLECTION",
                    opts=pulumi.ResourceOptions(parent=self.firestore_app),
                )

        super().register_outputs({})
