# TableauMetricqueryserviceV1BatchGetDefinitionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definitions** | [**List[TableauMetricqueryserviceTypesV1Definition]**](TableauMetricqueryserviceTypesV1Definition.md) |  | [optional] 
**errors** | [**List[TableauMetricqueryserviceTypesV1BatchGetMetricErrors]**](TableauMetricqueryserviceTypesV1BatchGetMetricErrors.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_v1_batch_get_definitions_response import TableauMetricqueryserviceV1BatchGetDefinitionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceV1BatchGetDefinitionsResponse from a JSON string
tableau_metricqueryservice_v1_batch_get_definitions_response_instance = TableauMetricqueryserviceV1BatchGetDefinitionsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceV1BatchGetDefinitionsResponse.to_json())

# convert the object into a dict
tableau_metricqueryservice_v1_batch_get_definitions_response_dict = tableau_metricqueryservice_v1_batch_get_definitions_response_instance.to_dict()
# create an instance of TableauMetricqueryserviceV1BatchGetDefinitionsResponse from a dict
tableau_metricqueryservice_v1_batch_get_definitions_response_from_dict = TableauMetricqueryserviceV1BatchGetDefinitionsResponse.from_dict(tableau_metricqueryservice_v1_batch_get_definitions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


