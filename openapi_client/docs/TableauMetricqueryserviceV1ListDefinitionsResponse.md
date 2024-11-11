# TableauMetricqueryserviceV1ListDefinitionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definitions** | [**List[TableauMetricqueryserviceTypesV1Definition]**](TableauMetricqueryserviceTypesV1Definition.md) |  | [optional] 
**next_page_token** | **str** |  | [optional] 
**total_available** | **int** | If available, specifies the total number of items in a requested list | [optional] 
**offset** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_v1_list_definitions_response import TableauMetricqueryserviceV1ListDefinitionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceV1ListDefinitionsResponse from a JSON string
tableau_metricqueryservice_v1_list_definitions_response_instance = TableauMetricqueryserviceV1ListDefinitionsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceV1ListDefinitionsResponse.to_json())

# convert the object into a dict
tableau_metricqueryservice_v1_list_definitions_response_dict = tableau_metricqueryservice_v1_list_definitions_response_instance.to_dict()
# create an instance of TableauMetricqueryserviceV1ListDefinitionsResponse from a dict
tableau_metricqueryservice_v1_list_definitions_response_from_dict = TableauMetricqueryserviceV1ListDefinitionsResponse.from_dict(tableau_metricqueryservice_v1_list_definitions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


