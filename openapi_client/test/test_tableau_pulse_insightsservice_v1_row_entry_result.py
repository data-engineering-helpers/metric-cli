# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_pulse_insightsservice_v1_row_entry_result import TableauPulseInsightsserviceV1RowEntryResult

class TestTableauPulseInsightsserviceV1RowEntryResult(unittest.TestCase):
    """TableauPulseInsightsserviceV1RowEntryResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauPulseInsightsserviceV1RowEntryResult:
        """Test TableauPulseInsightsserviceV1RowEntryResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauPulseInsightsserviceV1RowEntryResult`
        """
        model = TableauPulseInsightsserviceV1RowEntryResult()
        if include_optional:
            return TableauPulseInsightsserviceV1RowEntryResult(
                value = openapi_client.models.tableau/pulse/insightsservice/v1/row_entry.tableau.pulse.insightsservice.v1.RowEntry(
                    formatted_value = '', ),
                error = openapi_client.models.tableau/pulse/insightsservice/v1/error.tableau.pulse.insightsservice.v1.Error(
                    code = '', 
                    message = '', )
            )
        else:
            return TableauPulseInsightsserviceV1RowEntryResult(
        )
        """

    def testTableauPulseInsightsserviceV1RowEntryResult(self):
        """Test TableauPulseInsightsserviceV1RowEntryResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
