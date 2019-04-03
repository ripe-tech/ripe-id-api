#!/usr/bin/python
# -*- coding: utf-8 -*-

class TokenAPI(object):

    def issue_token(self):
        url = self.base_url + "tokens/issue"
        contents = self.post(url)
        return contents

    def redeem_token(self, token):
        url = self.base_url + "tokens/%s/redeem" % token
        contents = self.post(url)
        return contents
