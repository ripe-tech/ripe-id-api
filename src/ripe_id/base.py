#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

RIPEID_BASE_URL = "https://id.platforme.com/api/"
""" The default base URL to be used when no other
base URL value is provided to the constructor """

class API(appier.OAuth2API):

    def __init__(self, *args, **kwargs):
        appier.API.__init__(self, *args, **kwargs)
        self.base_url = appier.conf("RIPEID_BASE_URL", RIPEID_BASE_URL)
        self.client_id = appier.conf("RIPEID_ID", None)
        self.client_secret = appier.conf("RIPEID_SECRET", None)
        self.redirect_url = appier.conf("RIPEID_REDIRECT_URL", None)
        self.base_url = kwargs.get("base_url", self.base_url)
        self.client_id = kwargs.get("client_id", self.client_id)
        self.client_secret = kwargs.get("client_secret", self.client_secret)
        self.redirect_url = kwargs.get("redirect_url", self.redirect_url)
        self.scope = kwargs.get("scope", None)
        self.access_token = kwargs.get("access_token", None)
        self.refresh_token = kwargs.get("refresh_token", None)
        self.session_id = kwargs.get("session_id", None)

    def auth_callback(self, params, headers):
        if not self.refresh_token: return
        self.oauth_refresh()
        params["access_token"] = self.get_access_token()
        headers["Authorization"] = "Bearer %s" % self.get_access_token()

    def oauth_authorize(self, state = None, access_type = None, approval_prompt = True):
        url = self.login_url + "oauth2/auth"
        values = dict(
            client_id = self.client_id,
            redirect_uri = self.redirect_url,
            response_type = "code",
            scope = " ".join(self.scope)
        )
        if state: values["state"] = state
        if access_type: values["access_type"] = access_type
        if approval_prompt: values["approval_prompt"] = "force"
        data = appier.legacy.urlencode(values)
        url = url + "?" + data
        return url

    def oauth_access(self, code):
        url = self.login_url + "oauth2/token"
        contents = self.post(
            url,
            token = False,
            client_id = self.client_id,
            client_secret = self.client_secret,
            grant_type = "authorization_code",
            redirect_uri = self.redirect_url,
            code = code
        )
        self.access_token = contents["access_token"]
        self.refresh_token = contents.get("refresh_token", None)
        self.trigger("access_token", self.access_token)
        self.trigger("refresh_token", self.refresh_token)
        return self.access_token

    def oauth_refresh(self):
        url = self.login_url + "oauth2/token"
        contents = self.post(
            url,
            callback = False,
            token = False,
            client_id = self.client_id,
            client_secret = self.client_secret,
            grant_type = "refresh_token",
            redirect_uri = self.redirect_url,
            refresh_token = self.refresh_token
        )
        self.access_token = contents["access_token"]
        self.trigger("access_token", self.access_token)
        return self.access_token
