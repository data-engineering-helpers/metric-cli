# TableauMetricqueryserviceTypesV1Definition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**TableauMetricqueryserviceTypesV1Metadata**](TableauMetricqueryserviceTypesV1Metadata.md) |  | [optional] 
**specification** | [**TableauMetricqueryserviceTypesV1DefinitionSpecification**](TableauMetricqueryserviceTypesV1DefinitionSpecification.md) |  | [optional] 
**extension_options** | [**TableauMetricqueryserviceTypesV1ExtensionOptions**](TableauMetricqueryserviceTypesV1ExtensionOptions.md) |  | [optional] 
**metrics** | [**List[TableauMetricqueryserviceTypesV1Metric]**](TableauMetricqueryserviceTypesV1Metric.md) |  | [optional] 
**total_metrics** | **int** |  | [optional] 
**representation_options** | [**TableauMetricqueryserviceTypesV1RepresentationOptions**](TableauMetricqueryserviceTypesV1RepresentationOptions.md) |  | [optional] 
**insights_options** | [**TableauMetricqueryserviceTypesV1InsightsOptions**](TableauMetricqueryserviceTypesV1InsightsOptions.md) |  | [optional] 
**comparisons** | [**TableauMetricqueryserviceTypesV1Comparisons**](TableauMetricqueryserviceTypesV1Comparisons.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_types_v1_definition import TableauMetricqueryserviceTypesV1Definition

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceTypesV1Definition from a JSON string
tableau_metricqueryservice_types_v1_definition_instance = TableauMetricqueryserviceTypesV1Definition.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceTypesV1Definition.to_json())

# convert the object into a dict
tableau_metricqueryservice_types_v1_definition_dict = tableau_metricqueryservice_types_v1_definition_instance.to_dict()
# create an instance of TableauMetricqueryserviceTypesV1Definition from a dict
tableau_metricqueryservice_types_v1_definition_from_dict = TableauMetricqueryserviceTypesV1Definition.from_dict(tableau_metricqueryservice_types_v1_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


