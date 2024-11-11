# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_metricqueryservice_v1_update_definition_request import TableauMetricqueryserviceV1UpdateDefinitionRequest

class TestTableauMetricqueryserviceV1UpdateDefinitionRequest(unittest.TestCase):
    """TableauMetricqueryserviceV1UpdateDefinitionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauMetricqueryserviceV1UpdateDefinitionRequest:
        """Test TableauMetricqueryserviceV1UpdateDefinitionRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauMetricqueryserviceV1UpdateDefinitionRequest`
        """
        model = TableauMetricqueryserviceV1UpdateDefinitionRequest()
        if include_optional:
            return TableauMetricqueryserviceV1UpdateDefinitionRequest(
                definition_id = '',
                name = '',
                description = '',
                specification = openapi_client.models.tableau/metricqueryservice/types/v1/definition_specification.tableau.metricqueryservice.types.v1.DefinitionSpecification(
                    datasource = openapi_client.models.tableau/metricqueryservice/types/v1/datasource.tableau.metricqueryservice.types.v1.Datasource(
                        id = '', ), 
                    basic_specification = openapi_client.models.tableau/metricqueryservice/types/v1/basic_specification.tableau.metricqueryservice.types.v1.BasicSpecification(
                        measure = openapi_client.models.tableau/metricqueryservice/types/v1/measure.tableau.metricqueryservice.types.v1.Measure(
                            field = '', 
                            aggregation = 'AGGREGATION_UNSPECIFIED', ), 
                        time_dimension = openapi_client.models.tableau/metricqueryservice/types/v1/time_dimension.tableau.metricqueryservice.types.v1.TimeDimension(
                            field = '', ), 
                        filters = [
                            openapi_client.models.tableau/metricqueryservice/types/v1/filter.tableau.metricqueryservice.types.v1.Filter(
                                field = '', 
                                operator = 'OPERATOR_UNSPECIFIED', 
                                values = [
                                    ''
                                    ], 
                                include_null = True, 
                                categorical_values = [
                                    openapi_client.models.tableau/metricqueryservice/types/v1/categorical_value.tableau.metricqueryservice.types.v1.CategoricalValue(
                                        string_value = '', 
                                        bool_value = True, 
                                        null_value = 'NULL_VALUE', )
                                    ], )
                            ], ), 
                    abstract_query_specification = openapi_client.models.tableau/metricqueryservice/types/v1/abstract_query_specification.tableau.metricqueryservice.types.v1.AbstractQuerySpecification(
                        abstract_query_string = '', ), 
                    viz_state_specification = openapi_client.models.tableau/metricqueryservice/types/v1/viz_state_specification.tableau.metricqueryservice.types.v1.VizStateSpecification(
                        viz_state_string = '', ), 
                    is_running_total = True, ),
                extension_options = openapi_client.models.tableau/metricqueryservice/types/v1/extension_options.tableau.metricqueryservice.types.v1.ExtensionOptions(
                    allowed_dimensions = [
                        ''
                        ], 
                    allowed_granularities = [
                        'GRANULARITY_UNSPECIFIED'
                        ], 
                    offset_from_today = 56, ),
                representation_options = openapi_client.models.tableau/metricqueryservice/types/v1/representation_options.tableau.metricqueryservice.types.v1.RepresentationOptions(
                    type = 'NUMBER_FORMAT_TYPE_UNSPECIFIED', 
                    number_units = openapi_client.models.tableau/metricqueryservice/types/v1/representation_options/number_units.tableau.metricqueryservice.types.v1.RepresentationOptions.NumberUnits(
                        singular_noun = '', 
                        plural_noun = '', ), 
                    sentiment_type = 'SENTIMENT_TYPE_UNSPECIFIED', 
                    row_level_id_field = openapi_client.models.tableau/metricqueryservice/types/v1/representation_options/row_level_id_field.tableau.metricqueryservice.types.v1.RepresentationOptions.RowLevelIDField(
                        identifier_col = '', 
                        identifier_label = '', ), 
                    row_level_entity_names = openapi_client.models.tableau/metricqueryservice/types/v1/representation_options/row_level_entity_names.tableau.metricqueryservice.types.v1.RepresentationOptions.RowLevelEntityNames(
                        entity_name_singular = '', 
                        entity_name_plural = '', ), 
                    row_level_name_field = openapi_client.models.tableau/metricqueryservice/types/v1/representation_options/row_level_name_field.tableau.metricqueryservice.types.v1.RepresentationOptions.RowLevelNameField(
                        name_col = '', ), 
                    currency_code = 'CURRENCY_CODE_UNSPECIFIED', 
                    nested_number_units = openapi_client.models.tableau/metricqueryservice/types/v1/representation_options/number_units.tableau.metricqueryservice.types.v1.RepresentationOptions.NumberUnits(
                        singular_noun = '', 
                        plural_noun = '', ), 
                    nested_row_level_id_field = openapi_client.models.tableau/metricqueryservice/types/v1/representation_options/row_level_id_field.tableau.metricqueryservice.types.v1.RepresentationOptions.RowLevelIDField(
                        identifier_col = '', 
                        identifier_label = '', ), 
                    nested_row_level_name_field = openapi_client.models.tableau/metricqueryservice/types/v1/representation_options/row_level_name_field.tableau.metricqueryservice.types.v1.RepresentationOptions.RowLevelNameField(
                        name_col = '', ), 
                    nested_row_level_entity_names = openapi_client.models.tableau/metricqueryservice/types/v1/representation_options/row_level_entity_names.tableau.metricqueryservice.types.v1.RepresentationOptions.RowLevelEntityNames(
                        entity_name_singular = '', 
                        entity_name_plural = '', ), ),
                insights_options = openapi_client.models.tableau/metricqueryservice/types/v1/insights_options.tableau.metricqueryservice.types.v1.InsightsOptions(
                    show_insights = True, 
                    settings = [
                        openapi_client.models.tableau/metricqueryservice/types/v1/insights_options/insight_setting.tableau.metricqueryservice.types.v1.InsightsOptions.InsightSetting(
                            type = 'INSIGHT_TYPE_UNSPECIFIED', 
                            disabled = True, )
                        ], 
                    nested_insight_setting = openapi_client.models.tableau/metricqueryservice/types/v1/insights_options/insight_setting.tableau.metricqueryservice.types.v1.InsightsOptions.InsightSetting(
                        type = 'INSIGHT_TYPE_UNSPECIFIED', 
                        disabled = True, ), ),
                user_link = '',
                user_link_name = '',
                comparisons = openapi_client.models.tableau/metricqueryservice/types/v1/comparisons.tableau.metricqueryservice.types.v1.Comparisons(
                    comparisons = [
                        openapi_client.models.tableau/metricqueryservice/types/v1/comparisons/comparison.tableau.metricqueryservice.types.v1.Comparisons.Comparison(
                            compare_config = openapi_client.models.tableau/metricqueryservice/types/v1/compare_config.tableau.metricqueryservice.types.v1.CompareConfig(
                                comparison = 'TIME_COMPARISON_UNSPECIFIED', ), 
                            index = 56, )
                        ], 
                    nested_comparison = openapi_client.models.tableau/metricqueryservice/types/v1/comparisons/comparison.tableau.metricqueryservice.types.v1.Comparisons.Comparison(
                        index = 56, ), )
            )
        else:
            return TableauMetricqueryserviceV1UpdateDefinitionRequest(
        )
        """

    def testTableauMetricqueryserviceV1UpdateDefinitionRequest(self):
        """Test TableauMetricqueryserviceV1UpdateDefinitionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
