# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_pulse_insightsservice_v1_generate_insight_bundle_ban_response import TableauPulseInsightsserviceV1GenerateInsightBundleBANResponse

class TestTableauPulseInsightsserviceV1GenerateInsightBundleBANResponse(unittest.TestCase):
    """TableauPulseInsightsserviceV1GenerateInsightBundleBANResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauPulseInsightsserviceV1GenerateInsightBundleBANResponse:
        """Test TableauPulseInsightsserviceV1GenerateInsightBundleBANResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauPulseInsightsserviceV1GenerateInsightBundleBANResponse`
        """
        model = TableauPulseInsightsserviceV1GenerateInsightBundleBANResponse()
        if include_optional:
            return TableauPulseInsightsserviceV1GenerateInsightBundleBANResponse(
                bundle_response = openapi_client.models.tableau/pulse/insightsservice/v1/generate_insight_bundle_response.tableau.pulse.insightsservice.v1.GenerateInsightBundleResponse(
                    result = openapi_client.models.tableau/pulse/insightsservice/v1/insight_bundle.tableau.pulse.insightsservice.v1.InsightBundle(
                        insight_groups = [
                            openapi_client.models.tableau/pulse/insightsservice/v1/insight_group.tableau.pulse.insightsservice.v1.InsightGroup(
                                type = '', 
                                insights = [
                                    openapi_client.models.tableau/pulse/insightsservice/v1/insight_response.tableau.pulse.insightsservice.v1.InsightResponse(
                                        error = openapi_client.models.tableau/pulse/insightsservice/v1/error.tableau.pulse.insightsservice.v1.Error(
                                            code = '', 
                                            message = '', ), 
                                        insight_type = '', )
                                    ], 
                                summaries = [
                                    openapi_client.models.tableau/pulse/insightsservice/v1/summary_response.tableau.pulse.insightsservice.v1.SummaryResponse()
                                    ], 
                                error = openapi_client.models.tableau/pulse/insightsservice/v1/error.tableau.pulse.insightsservice.v1.Error(
                                    code = '', 
                                    message = '', ), )
                            ], 
                        has_errors = True, 
                        characterization = 'CHARACTERIZATION_UNSPECIFIED', ), 
                    error = , )
            )
        else:
            return TableauPulseInsightsserviceV1GenerateInsightBundleBANResponse(
        )
        """

    def testTableauPulseInsightsserviceV1GenerateInsightBundleBANResponse(self):
        """Test TableauPulseInsightsserviceV1GenerateInsightBundleBANResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
