# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_metricqueryservice_types_v1_viz_state_specification import TableauMetricqueryserviceTypesV1VizStateSpecification

class TestTableauMetricqueryserviceTypesV1VizStateSpecification(unittest.TestCase):
    """TableauMetricqueryserviceTypesV1VizStateSpecification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauMetricqueryserviceTypesV1VizStateSpecification:
        """Test TableauMetricqueryserviceTypesV1VizStateSpecification
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauMetricqueryserviceTypesV1VizStateSpecification`
        """
        model = TableauMetricqueryserviceTypesV1VizStateSpecification()
        if include_optional:
            return TableauMetricqueryserviceTypesV1VizStateSpecification(
                viz_state_string = ''
            )
        else:
            return TableauMetricqueryserviceTypesV1VizStateSpecification(
        )
        """

    def testTableauMetricqueryserviceTypesV1VizStateSpecification(self):
        """Test TableauMetricqueryserviceTypesV1VizStateSpecification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
