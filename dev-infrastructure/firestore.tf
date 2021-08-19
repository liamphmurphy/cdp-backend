provider "google-beta" {}

resource "google_project_service" "cloud_resource_service" {
  provider                   = google-beta
  service                    = "cloudresourcemanager.googleapis.com"
  project                    = "firestore-sr-test-05"
  disable_dependent_services = true
}

resource "google_project_service" "app_engine_service" {
  provider                   = google-beta
  service                    = "appengine.googleapis.com"
  project                    = google_project_service.cloud_resource_service.project
  disable_dependent_services = true
}

resource "google_project_service" "firebase_service" {
  provider                   = google-beta
  service                    = "firebase.googleapis.com"
  project                    = google_project_service.cloud_resource_service.project
  disable_dependent_services = true
}

resource "google_project_service" "firebase_storage_service" {
  provider                   = google-beta
  service                    = "firebasestorage.googleapis.com"
  project                    = google_project_service.cloud_resource_service.project
  disable_dependent_services = true
}

resource "google_project_service" "firestore_service" {
  provider                   = google-beta
  service                    = "firestore.googleapis.com"
  project                    = google_project_service.cloud_resource_service.project
  disable_dependent_services = true
}

resource "google_app_engine_application" "app" {
  provider      = google-beta
  project       = google_project_service.app_engine_service.project
  location_id   = "us-west1"
  database_type = "CLOUD_FIRESTORE"
  depends_on = [
    google_project_service.app_engine_service,
    google_project_service.firebase_service,
    google_project_service.firebase_storage_service,
    google_project_service.firestore_service
  ]
}

resource "google_firebase_project" "firebase_init" {
  provider = google-beta
  project  = google_app_engine_application.app.project
}

resource "google_firebase_project_location" "firebase_project" {
  provider    = google-beta
  project     = google_firebase_project.firebase_init.project
  location_id = google_app_engine_application.app.location_id
}

resource "google_project_service" "firestore_sr_service" {
  provider                   = google-beta
  service                    = "firebaserules.googleapis.com"
  project                    = google_firebase_project_location.firebase_project.project
  disable_dependent_services = true
}