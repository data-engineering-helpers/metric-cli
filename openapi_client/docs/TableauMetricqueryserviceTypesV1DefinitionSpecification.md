# TableauMetricqueryserviceTypesV1DefinitionSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | [**TableauMetricqueryserviceTypesV1Datasource**](TableauMetricqueryserviceTypesV1Datasource.md) |  | [optional] 
**basic_specification** | [**TableauMetricqueryserviceTypesV1BasicSpecification**](TableauMetricqueryserviceTypesV1BasicSpecification.md) |  | [optional] 
**abstract_query_specification** | [**TableauMetricqueryserviceTypesV1AbstractQuerySpecification**](TableauMetricqueryserviceTypesV1AbstractQuerySpecification.md) |  | [optional] 
**viz_state_specification** | [**TableauMetricqueryserviceTypesV1VizStateSpecification**](TableauMetricqueryserviceTypesV1VizStateSpecification.md) |  | [optional] 
**is_running_total** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_types_v1_definition_specification import TableauMetricqueryserviceTypesV1DefinitionSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceTypesV1DefinitionSpecification from a JSON string
tableau_metricqueryservice_types_v1_definition_specification_instance = TableauMetricqueryserviceTypesV1DefinitionSpecification.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceTypesV1DefinitionSpecification.to_json())

# convert the object into a dict
tableau_metricqueryservice_types_v1_definition_specification_dict = tableau_metricqueryservice_types_v1_definition_specification_instance.to_dict()
# create an instance of TableauMetricqueryserviceTypesV1DefinitionSpecification from a dict
tableau_metricqueryservice_types_v1_definition_specification_from_dict = TableauMetricqueryserviceTypesV1DefinitionSpecification.from_dict(tableau_metricqueryservice_types_v1_definition_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


