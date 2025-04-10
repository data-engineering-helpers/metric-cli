# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_pulse_insightsservice_v1_summary_response import TableauPulseInsightsserviceV1SummaryResponse

class TestTableauPulseInsightsserviceV1SummaryResponse(unittest.TestCase):
    """TableauPulseInsightsserviceV1SummaryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauPulseInsightsserviceV1SummaryResponse:
        """Test TableauPulseInsightsserviceV1SummaryResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauPulseInsightsserviceV1SummaryResponse`
        """
        model = TableauPulseInsightsserviceV1SummaryResponse()
        if include_optional:
            return TableauPulseInsightsserviceV1SummaryResponse(
                result = openapi_client.models.tableau/pulse/insightsservice/v1/summary.tableau.pulse.insightsservice.v1.Summary(
                    id = '', 
                    markup = '', 
                    viz = null, 
                    generation_id = '', 
                    timestamp = '', 
                    last_attempted_timestamp = '', ),
                error = openapi_client.models.tableau/pulse/insightsservice/v1/error.tableau.pulse.insightsservice.v1.Error(
                    code = '', 
                    message = '', )
            )
        else:
            return TableauPulseInsightsserviceV1SummaryResponse(
        )
        """

    def testTableauPulseInsightsserviceV1SummaryResponse(self):
        """Test TableauPulseInsightsserviceV1SummaryResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
