# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_metricqueryservice_types_v1_representation_options_row_level_id_field import TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelIDField

class TestTableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelIDField(unittest.TestCase):
    """TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelIDField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelIDField:
        """Test TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelIDField
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelIDField`
        """
        model = TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelIDField()
        if include_optional:
            return TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelIDField(
                identifier_col = '',
                identifier_label = ''
            )
        else:
            return TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelIDField(
        )
        """

    def testTableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelIDField(self):
        """Test TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelIDField"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
