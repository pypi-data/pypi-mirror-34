# coding: utf-8
"""Copyright
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="configuration.py">
   Copyright (c) 2018 Aspose.HTML for Cloud
 </copyright>
 <summary>

  Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
</summary>
--------------------------------------------------------------------------------------------------------------------
"""

from __future__ import absolute_import
import os
import copy
import logging
import multiprocessing
import sys
import urllib3
import json
from tempfile import gettempdir
import urllib3.contrib.pyopenssl
import six
from six.moves import http_client as httplib
import certifi

urllib3.contrib.pyopenssl.inject_into_urllib3()

class TypeWithDefault(type):
    def __init__(cls, name, bases, dct):
        super(TypeWithDefault, cls).__init__(name, bases, dct)
        cls._default = None

    def __call__(cls, *args, **kwargs):
        if cls._default is None:
            cls._default = type.__call__(cls, *args, **kwargs)
        return copy.copy(cls._default)

    def set_default(cls, default):
        cls._default = copy.copy(default)


class Configuration(six.with_metaclass(TypeWithDefault, object)):

    def __init__(self, apiKey=None, appSid=None, basePath="https://api.aspose.cloud/v1.1",
                 authPath = "https://api.aspose.cloud/oauth2/token", debug=False):

        """Constructor"""
        # Get configuration from external file
        if apiKey == None or appSid == None :

            # Load config from external file
            with open(os.path.dirname(__file__) + '/../setting/config.json', 'r') as f:
                self.config = json.load(f)

            # Authentication Settings
            self.api_key = self.config['apiKey']
            self.app_sid = self.config['appSID']

            # Default Base url
            self.host = self.config['basePath']
            self.auth_host = self.config['authPath']
            self.test_result = os.path.dirname(__file__) + '/..' + self.config['testResult']
            self.test_data = os.path.dirname(__file__) + '/..' + self.config['testData']
            self.remote_folder = self.config['remoteFolder']

            # Default client
            self.default_user_agent = self.config['defaultUserAgent']

            # Debug file location
            log_file = os.pardir + '/' + self.config['debugFile']
            # Debug switch
            dbg = self.config['debug']
        # Configuration in parameters
        else:
            # Authentication Settings
            self.api_key = apiKey
            self.app_sid = appSid

            # Default Base url
            self.host = basePath
            self.auth_host = authPath

            # Default client
            self.default_user_agent = "Aspose_SDK"

            # Debug file location
            log_file = os.pardir + '/debug.log'
            # Debug switch
            dbg = debug

        # Temp file folder for downloading files
        self.temp_folder_path = gettempdir()

        # dict to store API prefix (e.g. Bearer)
        self.api_key_prefix = {}

        # access token for OAuth2
        self.access_token = 'Bearer ' + self.get_token()

        # Logging Settings
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("asposehtmlcloud")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None

        self.logger_file = log_file

        self.debug= dbg

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API
        # from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = certifi.where()
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None
        # Set this to True/False to enable/disable SSL hostname verification.
        self.assert_hostname = None

        # urllib3 connection pool's maximum number of connections saved
        # per pool. urllib3 uses 1 connection as default value, but this is
        # not the best value when you are making a lot of possibly parallel
        # requests to the same host, which is often the case here.
        # cpu_count * 5 is used as default value to increase performance.
        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5

        # Proxy URL
        self.proxy = None
        # Safe chars for path_param
        self.safe_chars_for_path_param = ''

    def get_token(self):
        # call from __init__ - CERT not ready
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        r = http.request("POST",self.auth_host,
                         headers={"ContentType": "application/x-www-form-urlencoded;charset=UTF-8",
                                  "Accept":"application/json"},
                         body="client_id="+self.app_sid+"&client_secret="
                              + self.api_key +"&grant_type=client_credentials")
        return json.loads(r.data)['access_token']

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.
        """
        if (self.api_key.get(identifier) and
                self.api_key_prefix.get(identifier)):
            return self.api_key_prefix[identifier] + ' ' + self.api_key[identifier]
        elif self.api_key.get(identifier):
            return self.api_key[identifier]

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        return urllib3.util.make_headers(
            basic_auth=self.username + ':' + self.password
        ).get('authorization')

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        return {
            'appsid':
                {
                    'type': 'api_key',
                    'in': 'query',
                    'key': 'appsid',
                    'value': self.get_api_key_with_prefix('appsid')
                },

            'oauth':
                {
                    'type': 'oauth2',
                    'in': 'header',
                    'key': 'Authorization',
                    'value': 'Bearer ' + self.access_token
                },
            'signature':
                {
                    'type': 'api_key',
                    'in': 'query',
                    'key': 'signature',
                    'value': self.get_api_key_with_prefix('signature')
                },

        }

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 18.04\n"\
               "SDK Package Version: 1.0.1".\
               format(env=sys.platform, pyversion=sys.version)

