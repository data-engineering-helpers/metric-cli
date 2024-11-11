# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_permissionservice_v1_has_effective_permissions_response import TableauPermissionserviceV1HasEffectivePermissionsResponse

class TestTableauPermissionserviceV1HasEffectivePermissionsResponse(unittest.TestCase):
    """TableauPermissionserviceV1HasEffectivePermissionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauPermissionserviceV1HasEffectivePermissionsResponse:
        """Test TableauPermissionserviceV1HasEffectivePermissionsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauPermissionserviceV1HasEffectivePermissionsResponse`
        """
        model = TableauPermissionserviceV1HasEffectivePermissionsResponse()
        if include_optional:
            return TableauPermissionserviceV1HasEffectivePermissionsResponse(
                definition_id = '',
                effective_permission_states = [
                    openapi_client.models.tableau/permissionservice/v1/permission_state.tableau.permissionservice.v1.PermissionState(
                        permission = 'PERMISSION_UNSPECIFIED', 
                        has_permission = True, )
                    ]
            )
        else:
            return TableauPermissionserviceV1HasEffectivePermissionsResponse(
        )
        """

    def testTableauPermissionserviceV1HasEffectivePermissionsResponse(self):
        """Test TableauPermissionserviceV1HasEffectivePermissionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
