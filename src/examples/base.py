#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import ripe_id

SCOPE = (
    "acl",
    "email"
)

def get_api():
    return ripe_id.API(
        client_id = appier.conf("RIPEID_ID"),
        client_secret = appier.conf("RIPEID_SECRET"),
        redirect_url = appier.conf("RIPEID_REDIRECT_URL"),
        scope = SCOPE
    )
