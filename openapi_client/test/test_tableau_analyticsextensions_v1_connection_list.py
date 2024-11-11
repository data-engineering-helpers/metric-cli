# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_analyticsextensions_v1_connection_list import TableauAnalyticsextensionsV1ConnectionList

class TestTableauAnalyticsextensionsV1ConnectionList(unittest.TestCase):
    """TableauAnalyticsextensionsV1ConnectionList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauAnalyticsextensionsV1ConnectionList:
        """Test TableauAnalyticsextensionsV1ConnectionList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauAnalyticsextensionsV1ConnectionList`
        """
        model = TableauAnalyticsextensionsV1ConnectionList()
        if include_optional:
            return TableauAnalyticsextensionsV1ConnectionList(
                connection_list = [
                    openapi_client.models.tableau/analyticsextensions/v1/connection_item.tableau.analyticsextensions.v1.ConnectionItem(
                        host = '', 
                        port = 56, 
                        is_auth_enabled = True, 
                        username = '', 
                        password = '', 
                        is_ssl_enabled = True, 
                        connection_brief = openapi_client.models.tableau/analyticsextensions/v1/connection_brief.tableau.analyticsextensions.v1.ConnectionBrief(
                            connection_name = '', 
                            connection_type = 'UNDEFINED', ), 
                        connection_luid = '', )
                    ]
            )
        else:
            return TableauAnalyticsextensionsV1ConnectionList(
        )
        """

    def testTableauAnalyticsextensionsV1ConnectionList(self):
        """Test TableauAnalyticsextensionsV1ConnectionList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
