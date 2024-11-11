# TableauMetricqueryserviceV1BatchGetDefinitionsByPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition_ids** | **List[str]** |  | [optional] 
**view** | **str** |  | [optional] 
**number_of_metrics** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_v1_batch_get_definitions_by_post_request import TableauMetricqueryserviceV1BatchGetDefinitionsByPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceV1BatchGetDefinitionsByPostRequest from a JSON string
tableau_metricqueryservice_v1_batch_get_definitions_by_post_request_instance = TableauMetricqueryserviceV1BatchGetDefinitionsByPostRequest.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceV1BatchGetDefinitionsByPostRequest.to_json())

# convert the object into a dict
tableau_metricqueryservice_v1_batch_get_definitions_by_post_request_dict = tableau_metricqueryservice_v1_batch_get_definitions_by_post_request_instance.to_dict()
# create an instance of TableauMetricqueryserviceV1BatchGetDefinitionsByPostRequest from a dict
tableau_metricqueryservice_v1_batch_get_definitions_by_post_request_from_dict = TableauMetricqueryserviceV1BatchGetDefinitionsByPostRequest.from_dict(tableau_metricqueryservice_v1_batch_get_definitions_by_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


