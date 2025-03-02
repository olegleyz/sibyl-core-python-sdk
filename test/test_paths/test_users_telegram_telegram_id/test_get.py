# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import sibyl_core_sdk
from sibyl_core_sdk.paths.users_telegram_telegram_id import get  # noqa: E501
from sibyl_core_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestUsersTelegramTelegramId(ApiTestMixin, unittest.TestCase):
    """
    UsersTelegramTelegramId unit test stubs
        Get user by Telegram ID  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
