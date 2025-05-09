# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_metricqueryservice_types_v1_insights_options import TableauMetricqueryserviceTypesV1InsightsOptions

class TestTableauMetricqueryserviceTypesV1InsightsOptions(unittest.TestCase):
    """TableauMetricqueryserviceTypesV1InsightsOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauMetricqueryserviceTypesV1InsightsOptions:
        """Test TableauMetricqueryserviceTypesV1InsightsOptions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauMetricqueryserviceTypesV1InsightsOptions`
        """
        model = TableauMetricqueryserviceTypesV1InsightsOptions()
        if include_optional:
            return TableauMetricqueryserviceTypesV1InsightsOptions(
                show_insights = True,
                settings = [
                    openapi_client.models.tableau/metricqueryservice/types/v1/insights_options/insight_setting.tableau.metricqueryservice.types.v1.InsightsOptions.InsightSetting(
                        type = 'INSIGHT_TYPE_UNSPECIFIED', 
                        disabled = True, )
                    ],
                nested_insight_setting = openapi_client.models.tableau/metricqueryservice/types/v1/insights_options/insight_setting.tableau.metricqueryservice.types.v1.InsightsOptions.InsightSetting(
                    type = 'INSIGHT_TYPE_UNSPECIFIED', 
                    disabled = True, )
            )
        else:
            return TableauMetricqueryserviceTypesV1InsightsOptions(
        )
        """

    def testTableauMetricqueryserviceTypesV1InsightsOptions(self):
        """Test TableauMetricqueryserviceTypesV1InsightsOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
