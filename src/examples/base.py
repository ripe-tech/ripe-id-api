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
        client_id = appier.conf("RIPE_ID_ID"),
        client_secret = appier.conf("RIPE_ID_SECRET"),
        redirect_url = appier.conf("RIPE_ID_REDIRECT_URL"),
        scope = SCOPE
    )
