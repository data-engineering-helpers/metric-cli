# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_permissionservice_v1_get_definition_permissions_response import TableauPermissionserviceV1GetDefinitionPermissionsResponse

class TestTableauPermissionserviceV1GetDefinitionPermissionsResponse(unittest.TestCase):
    """TableauPermissionserviceV1GetDefinitionPermissionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauPermissionserviceV1GetDefinitionPermissionsResponse:
        """Test TableauPermissionserviceV1GetDefinitionPermissionsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauPermissionserviceV1GetDefinitionPermissionsResponse`
        """
        model = TableauPermissionserviceV1GetDefinitionPermissionsResponse()
        if include_optional:
            return TableauPermissionserviceV1GetDefinitionPermissionsResponse(
                definition_id = '',
                member_permissions = [
                    openapi_client.models.tableau/permissionservice/v1/member_permission.tableau.permissionservice.v1.MemberPermission(
                        member_id = '', 
                        member_entity_type = 'MEMBER_ENTITY_TYPE_UNSPECIFIED', 
                        permission = 'PERMISSION_UNSPECIFIED', )
                    ]
            )
        else:
            return TableauPermissionserviceV1GetDefinitionPermissionsResponse(
        )
        """

    def testTableauPermissionserviceV1GetDefinitionPermissionsResponse(self):
        """Test TableauPermissionserviceV1GetDefinitionPermissionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
