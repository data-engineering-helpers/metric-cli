# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_metricqueryservice_types_v1_categorical_value import TableauMetricqueryserviceTypesV1CategoricalValue

class TestTableauMetricqueryserviceTypesV1CategoricalValue(unittest.TestCase):
    """TableauMetricqueryserviceTypesV1CategoricalValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauMetricqueryserviceTypesV1CategoricalValue:
        """Test TableauMetricqueryserviceTypesV1CategoricalValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauMetricqueryserviceTypesV1CategoricalValue`
        """
        model = TableauMetricqueryserviceTypesV1CategoricalValue()
        if include_optional:
            return TableauMetricqueryserviceTypesV1CategoricalValue(
                string_value = '',
                bool_value = True,
                null_value = 'NULL_VALUE'
            )
        else:
            return TableauMetricqueryserviceTypesV1CategoricalValue(
        )
        """

    def testTableauMetricqueryserviceTypesV1CategoricalValue(self):
        """Test TableauMetricqueryserviceTypesV1CategoricalValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
