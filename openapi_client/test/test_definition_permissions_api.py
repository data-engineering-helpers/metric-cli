# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.definition_permissions_api import DefinitionPermissionsApi


class TestDefinitionPermissionsApi(unittest.TestCase):
    """DefinitionPermissionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefinitionPermissionsApi()

    def tearDown(self) -> None:
        pass

    def test_permission_service_add_definition_permissions(self) -> None:
        """Test case for permission_service_add_definition_permissions

        Add definition permission records to the definition specified by the id.
        """
        pass

    def test_permission_service_delete_definition_permissions(self) -> None:
        """Test case for permission_service_delete_definition_permissions

        Delete definition permission records from the definition specified by the id.
        """
        pass

    def test_permission_service_get_definition_permissions(self) -> None:
        """Test case for permission_service_get_definition_permissions

        Get definition permission records for the definition specified by the id.
        """
        pass

    def test_permission_service_has_effective_permissions(self) -> None:
        """Test case for permission_service_has_effective_permissions

        Based on the site role and other rules get the effective permissions of the current user
        """
        pass


if __name__ == '__main__':
    unittest.main()
