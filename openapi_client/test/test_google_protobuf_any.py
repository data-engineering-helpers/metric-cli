# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.google_protobuf_any import GoogleProtobufAny

class TestGoogleProtobufAny(unittest.TestCase):
    """GoogleProtobufAny unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoogleProtobufAny:
        """Test GoogleProtobufAny
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoogleProtobufAny`
        """
        model = GoogleProtobufAny()
        if include_optional:
            return GoogleProtobufAny(
                type_url = '',
                value = 'YQ=='
            )
        else:
            return GoogleProtobufAny(
        )
        """

    def testGoogleProtobufAny(self):
        """Test GoogleProtobufAny"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
