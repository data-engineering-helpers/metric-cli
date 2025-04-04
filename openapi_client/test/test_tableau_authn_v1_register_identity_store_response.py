# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_authn_v1_register_identity_store_response import TableauAuthnV1RegisterIdentityStoreResponse

class TestTableauAuthnV1RegisterIdentityStoreResponse(unittest.TestCase):
    """TableauAuthnV1RegisterIdentityStoreResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauAuthnV1RegisterIdentityStoreResponse:
        """Test TableauAuthnV1RegisterIdentityStoreResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauAuthnV1RegisterIdentityStoreResponse`
        """
        model = TableauAuthnV1RegisterIdentityStoreResponse()
        if include_optional:
            return TableauAuthnV1RegisterIdentityStoreResponse(
                store_instance = openapi_client.models.tableau/authn/v1/identity_store_instance.tableau.authn.v1.IdentityStoreInstance(
                    id = 56, 
                    type = 'LOCAL', 
                    name = '', 
                    display_name = '', 
                    created_at = '', 
                    updated_at = '', )
            )
        else:
            return TableauAuthnV1RegisterIdentityStoreResponse(
        )
        """

    def testTableauAuthnV1RegisterIdentityStoreResponse(self):
        """Test TableauAuthnV1RegisterIdentityStoreResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
