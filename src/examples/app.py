#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class RipeIdApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "ripe_id",
            *args, **kwargs
        )

    @appier.route("/", "GET")
    def index(self):
        return self.me()

    @appier.route("/me", "GET")
    def me(self):
        url = self.ensure_api()
        if url: return self.redirect(url)
        api = self.get_api()
        account = api.self_account()
        return account

    @appier.route("/oauth", "GET")
    def oauth(self):
        code = self.field("code")
        api = self.get_api()
        access_token = api.oauth_access(code)
        self.session["rid.access_token"] = access_token
        return self.redirect(
            self.url_for("ripe_id.index")
        )

    @appier.exception_handler(appier.OAuthAccessError)
    def oauth_error(self, error):
        if "rid.access_token" in self.session: del self.session["rid.access_token"]
        return self.redirect(
            self.url_for("ripe_id.index")
        )

    def ensure_api(self):
        access_token = self.session.get("rid.access_token", None)
        if access_token: return
        api = base.get_api()
        return api.oauth_authorize()

    def get_api(self):
        access_token = self.session and self.session.get("rid.access_token", None)
        api = base.get_api()
        api.access_token = access_token
        return api

if __name__ == "__main__":
    app = RipeIdApp()
    app.serve()
else:
    __path__ = []
