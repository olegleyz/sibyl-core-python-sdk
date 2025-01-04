# coding: utf-8

"""
    Sibyl Core API

    Core API for Sibyl Numerology Bot

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sibyl_core_sdk.models.error import Error

class TestError(unittest.TestCase):
    """Error unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Error:
        """Test Error
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Error`
        """
        model = Error()
        if include_optional:
            return Error(
                error = ''
            )
        else:
            return Error(
                error = '',
        )
        """

    def testError(self):
        """Test Error"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
