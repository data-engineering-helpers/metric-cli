# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_permissionservice_v1_delete_definition_permissions_response import TableauPermissionserviceV1DeleteDefinitionPermissionsResponse

class TestTableauPermissionserviceV1DeleteDefinitionPermissionsResponse(unittest.TestCase):
    """TableauPermissionserviceV1DeleteDefinitionPermissionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauPermissionserviceV1DeleteDefinitionPermissionsResponse:
        """Test TableauPermissionserviceV1DeleteDefinitionPermissionsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauPermissionserviceV1DeleteDefinitionPermissionsResponse`
        """
        model = TableauPermissionserviceV1DeleteDefinitionPermissionsResponse()
        if include_optional:
            return TableauPermissionserviceV1DeleteDefinitionPermissionsResponse(
                definition_id = '',
                member_permissions = [
                    openapi_client.models.tableau/permissionservice/v1/member_permission.tableau.permissionservice.v1.MemberPermission(
                        member_id = '', 
                        member_entity_type = 'MEMBER_ENTITY_TYPE_UNSPECIFIED', 
                        permission = 'PERMISSION_UNSPECIFIED', )
                    ],
                member_errors = [
                    openapi_client.models.tableau/permissionservice/v1/member_error.tableau.permissionservice.v1.MemberError(
                        member_id = '', 
                        member_entity_type = 'MEMBER_ENTITY_TYPE_UNSPECIFIED', 
                        error_id = '', 
                        error_message = '', )
                    ]
            )
        else:
            return TableauPermissionserviceV1DeleteDefinitionPermissionsResponse(
        )
        """

    def testTableauPermissionserviceV1DeleteDefinitionPermissionsResponse(self):
        """Test TableauPermissionserviceV1DeleteDefinitionPermissionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
