# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_metricqueryservice_v1_get_entitlements_response import TableauMetricqueryserviceV1GetEntitlementsResponse

class TestTableauMetricqueryserviceV1GetEntitlementsResponse(unittest.TestCase):
    """TableauMetricqueryserviceV1GetEntitlementsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauMetricqueryserviceV1GetEntitlementsResponse:
        """Test TableauMetricqueryserviceV1GetEntitlementsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauMetricqueryserviceV1GetEntitlementsResponse`
        """
        model = TableauMetricqueryserviceV1GetEntitlementsResponse()
        if include_optional:
            return TableauMetricqueryserviceV1GetEntitlementsResponse(
                entitlements = [
                    openapi_client.models.tableau/metricqueryservice/types/v1/entitlement.tableau.metricqueryservice.types.v1.Entitlement(
                        entitlement_type = 'ENTITLEMENT_TYPE_UNSPECIFIED', 
                        enabled = True, )
                    ]
            )
        else:
            return TableauMetricqueryserviceV1GetEntitlementsResponse(
        )
        """

    def testTableauMetricqueryserviceV1GetEntitlementsResponse(self):
        """Test TableauMetricqueryserviceV1GetEntitlementsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
