# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_analyticsextensions_v1_connection_mapping import TableauAnalyticsextensionsV1ConnectionMapping

class TestTableauAnalyticsextensionsV1ConnectionMapping(unittest.TestCase):
    """TableauAnalyticsextensionsV1ConnectionMapping unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauAnalyticsextensionsV1ConnectionMapping:
        """Test TableauAnalyticsextensionsV1ConnectionMapping
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauAnalyticsextensionsV1ConnectionMapping`
        """
        model = TableauAnalyticsextensionsV1ConnectionMapping()
        if include_optional:
            return TableauAnalyticsextensionsV1ConnectionMapping(
                workbook_luid = '',
                connection_luid = ''
            )
        else:
            return TableauAnalyticsextensionsV1ConnectionMapping(
        )
        """

    def testTableauAnalyticsextensionsV1ConnectionMapping(self):
        """Test TableauAnalyticsextensionsV1ConnectionMapping"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
