# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_metricqueryservice_types_v1_extension_options import TableauMetricqueryserviceTypesV1ExtensionOptions

class TestTableauMetricqueryserviceTypesV1ExtensionOptions(unittest.TestCase):
    """TableauMetricqueryserviceTypesV1ExtensionOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauMetricqueryserviceTypesV1ExtensionOptions:
        """Test TableauMetricqueryserviceTypesV1ExtensionOptions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauMetricqueryserviceTypesV1ExtensionOptions`
        """
        model = TableauMetricqueryserviceTypesV1ExtensionOptions()
        if include_optional:
            return TableauMetricqueryserviceTypesV1ExtensionOptions(
                allowed_dimensions = [
                    ''
                    ],
                allowed_granularities = [
                    'GRANULARITY_UNSPECIFIED'
                    ],
                offset_from_today = 56
            )
        else:
            return TableauMetricqueryserviceTypesV1ExtensionOptions(
        )
        """

    def testTableauMetricqueryserviceTypesV1ExtensionOptions(self):
        """Test TableauMetricqueryserviceTypesV1ExtensionOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
