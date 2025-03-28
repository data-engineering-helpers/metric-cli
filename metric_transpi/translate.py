

from metric_transpi.dbt import CalculationMethod, Metric, TimeGrains
from metric_transpi.tableau import TableauAggregation, TableauGranularity
from openapi_client.models.tableau_metricqueryservice_types_v1_definition import MetricDefinition
from openapi_client.models.tableau_metricqueryservice_types_v1_metadata import MetricDefinitionMetadata
from openapi_client.models.tableau_metricqueryservice_types_v1_basic_specification import TableauMetricqueryserviceTypesV1BasicSpecification as basic_spec
from openapi_client.models.tableau_metricqueryservice_types_v1_datasource import TableauMetricqueryserviceTypesV1Datasource as datasource
from openapi_client.models.tableau_metricqueryservice_types_v1_definition import MetricDefinition
from openapi_client.models.tableau_metricqueryservice_types_v1_definition_specification import TableauMetricqueryserviceTypesV1DefinitionSpecification as def_spec
from openapi_client.models.tableau_metricqueryservice_types_v1_insights_options import TableauMetricqueryserviceTypesV1InsightsOptions as insights_opt
from openapi_client.models.tableau_metricqueryservice_types_v1_metadata import MetricDefinitionMetadata
from openapi_client.models.tableau_metricqueryservice_v1_create_definition_request import TableauMetricqueryserviceV1CreateDefinitionRequest as create_request
from openapi_client.models.tableau_metricqueryservice_v1_update_definition_request import TableauMetricqueryserviceV1UpdateDefinitionRequest as update_request
from openapi_client.models.tableau_metricqueryservice_types_v1_extension_options import TableauMetricqueryserviceTypesV1ExtensionOptions as extension
from openapi_client.models.tableau_metricqueryservice_types_v1_representation_options import TableauMetricqueryserviceTypesV1RepresentationOptions as representation_opt
from openapi_client.models.tableau_metricqueryservice_types_v1_measure import TableauMetricqueryserviceTypesV1Measure as measure
from openapi_client.models.tableau_metricqueryservice_types_v1_time_dimension import TableauMetricqueryserviceTypesV1TimeDimension as time_dim
from openapi_client.models.tableau_metricqueryservice_types_v1_compare_config import TableauMetricqueryserviceTypesV1CompareConfig
from openapi_client.models.tableau_metricqueryservice_types_v1_comparisons import TableauMetricqueryserviceTypesV1Comparisons
from openapi_client.models.tableau_metricqueryservice_types_v1_comparisons_comparison import TableauMetricqueryserviceTypesV1ComparisonsComparison
from deepdiff import DeepDiff



def to_pulse(m: Metric)-> MetricDefinition:
    definition = MetricDefinition(
        metadata=MetricDefinitionMetadata(
            name=m.name,
            description=m.description,
        ),
        specification=def_spec(
            datasource=datasource(
                id=m.datasource_id
            ),
            basic_specification=basic_spec(
                measure=measure(
                    var_field=m.expression,
                    aggregation=TableauAggregation[m.calculation_method.name].value
                ),
                time_dimension=time_dim(
                    field=m.timestamp,
                )
            ),
            is_running_total=True
        ),
        extension_options=extension(
            allowed_dimensions=m.dimensions,
            allowed_granularities=[TableauGranularity[grain.name].value for grain in m.time_grains]
        ),
        representation_options=representation_opt(),
        insights_options=insights_opt(),
        comparisons=TableauMetricqueryserviceTypesV1Comparisons(
            comparisons=[
                TableauMetricqueryserviceTypesV1ComparisonsComparison(
                    compare_config=TableauMetricqueryserviceTypesV1CompareConfig(
                        comparison='TIME_COMPARISON_PREVIOUS_PERIOD'
                    )
            )]
        )
    ) 
    return definition

def to_dbt(mdf: MetricDefinition)->Metric:
    return Metric(
        name=mdf.metadata.name,
        description=mdf.metadata.description,
        label='',
        model='',
        datasource_id=mdf.specification.datasource.id,
        timestamp=mdf.specification.basic_specification.time_dimension.var_field,
        expression=mdf.specification.basic_specification.measure.var_field,
        time_grains=[TimeGrains[TableauGranularity(grain).name].value for grain in mdf.extension_options.allowed_granularities],
        calculation_method=CalculationMethod[TableauAggregation(mdf.specification.basic_specification.measure.aggregation).name].value,
        dimensions=mdf.extension_options.allowed_dimensions
    )

def diff(m: Metric, mdf: MetricDefinition):
    return DeepDiff(
        t1=to_dbt(mdf).to_dict(),
        t2=m.to_dict(), 
        exclude_paths=["model", "label"]
    )