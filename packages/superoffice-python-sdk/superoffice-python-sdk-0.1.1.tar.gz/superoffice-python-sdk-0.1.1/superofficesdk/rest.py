import requests

from collections import OrderedDict
from superofficesdk.login import SuperOfficeLogin

API_VERSION = 'v1'


class SuperOffice():

    def __init__(self,
                 cust_id=None,
                 app_token=None,
                 sys_token=None,
                 private_key=None,
                 username=None,
                 password=None,
                 environment='online'):
        self.cust_id = cust_id
        self.app_token = app_token
        self.sys_token = sys_token
        self.private_key = private_key
        self.environment = environment

        self.session = requests.Session()

        if all(arg is not None for arg in (
               username, password, environment)):

            self.auth_type = 'basic'

            self.ticket = SuperOfficeLogin(
                self.cust_id,
                self.app_token,
                self.sys_token,
                self.private_key,
                self.environment)

        elif all(arg is not None for arg in (
                 cust_id, app_token, sys_token, private_key, environment)):

            self.auth_type = 'SOTicket'

            self.ticket = SuperOfficeLogin(
                self.cust_id,
                self.app_token,
                self.sys_token,
                self.private_key,
                self.environment)

        else:
            raise TypeError(
                'You must provide login information or token/ticket'
            )

        self.base_url = ('https://{env}.superoffice.com/{cust}/api/{ver}/'
                         .format(env=self.environment,
                                 cust=self.cust_id,
                                 ver=API_VERSION))

        self.headers = {
            'Authorization': 'SOTicket %s' % self.ticket,
            'SO-AppToken': self.app_token,
            'Content-Type': 'application/json',
        }

    def query(self, entity, fields, filter, skip, top):
        url = self.base_url + entity

        params = {
            '$select': fields,
            '$filter': filter,
            '$skip': skip,
            '$top': top
        }

        result = self._call_superoffice('GET', url, params=params)

        return result.json(object_pairs_hook=OrderedDict)

    def _call_superoffice(self, method, url, **kwargs):

        result = self.session.request(
            method, url, headers=self.headers, **kwargs)

        # TODO: handle exceptions

        return result
