# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_authn_v1_update_identity_pool_response import TableauAuthnV1UpdateIdentityPoolResponse

class TestTableauAuthnV1UpdateIdentityPoolResponse(unittest.TestCase):
    """TableauAuthnV1UpdateIdentityPoolResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauAuthnV1UpdateIdentityPoolResponse:
        """Test TableauAuthnV1UpdateIdentityPoolResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauAuthnV1UpdateIdentityPoolResponse`
        """
        model = TableauAuthnV1UpdateIdentityPoolResponse()
        if include_optional:
            return TableauAuthnV1UpdateIdentityPoolResponse(
                pool = openapi_client.models.tableau/authn/v1/identity_pool.tableau.authn.v1.IdentityPool(
                    identity_pool_id = openapi_client.models.tableau/authn/v1/uuid.tableau.authn.v1.UUID(
                        value = '', ), 
                    identity_pool_name = '', 
                    identity_store_instance_id = 56, 
                    auth_type_instance_id = 56, 
                    is_enabled = True, 
                    created_at = '', 
                    updated_at = '', 
                    description = '', 
                    identity_store_type = 'LOCAL', 
                    auth_type = 'OIDC', )
            )
        else:
            return TableauAuthnV1UpdateIdentityPoolResponse(
        )
        """

    def testTableauAuthnV1UpdateIdentityPoolResponse(self):
        """Test TableauAuthnV1UpdateIdentityPoolResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
