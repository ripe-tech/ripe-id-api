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

    @appier.route("/logout", "GET")
    def logout(self):
        return self.oauth_error(None)

    @appier.route("/oauth", "GET")
    def oauth(self):
        code = self.field("code")
        error = self.field("error")
        appier.verify(
            not error,
            message = "Invalid OAuth response (%s)" % error,
            exception = appier.OperationalError
        )
        api = self.get_api()
        access_token = api.oauth_access(code)
        self.session["rid.access_token"] = access_token
        return self.redirect(
            self.url_for("ripe_id.index")
        )

    @appier.exception_handler(appier.OAuthAccessError)
    def oauth_error(self, error):
        if "rid.access_token" in self.session: del self.session["rid.access_token"]
        if "rid.session_id" in self.session: del self.session["rid.session_id"]
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
        session_id = self.session and self.session.get("rid.session_id", None)
        api = base.get_api()
        api.access_token = access_token
        api.session_id = session_id
        api.bind("auth", self.on_auth)
        return api

    def on_auth(self, contents):
        if not self.session: return
        session_id = contents.get("session_id", None)
        self.session["rid.session_id"] = session_id

if __name__ == "__main__":
    app = RipeIdApp()
    app.serve()
else:
    __path__ = []
