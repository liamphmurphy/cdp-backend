#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is just used for dev setup and CI stack preview.
It is recommended to use the cookiecutter-cdp-deployment as it
"""

from pulumi import export, get_stack

from cdp_backend.infrastructure import CDPStack

###############################################################################

cdp_stack = CDPStack(get_stack())

export("firestore_address", cdp_stack.firestore_app.app_id)
export("gcp_bucket_name", cdp_stack.firestore_app.default_bucket)
