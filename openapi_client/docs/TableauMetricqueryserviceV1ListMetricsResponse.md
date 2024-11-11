# TableauMetricqueryserviceV1ListMetricsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[TableauMetricqueryserviceTypesV1Metric]**](TableauMetricqueryserviceTypesV1Metric.md) |  | [optional] 
**next_page_token** | **str** |  | [optional] 
**total_available** | **int** | If available, specifies the total number of items in a requested list | [optional] 
**offset** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_v1_list_metrics_response import TableauMetricqueryserviceV1ListMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceV1ListMetricsResponse from a JSON string
tableau_metricqueryservice_v1_list_metrics_response_instance = TableauMetricqueryserviceV1ListMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceV1ListMetricsResponse.to_json())

# convert the object into a dict
tableau_metricqueryservice_v1_list_metrics_response_dict = tableau_metricqueryservice_v1_list_metrics_response_instance.to_dict()
# create an instance of TableauMetricqueryserviceV1ListMetricsResponse from a dict
tableau_metricqueryservice_v1_list_metrics_response_from_dict = TableauMetricqueryserviceV1ListMetricsResponse.from_dict(tableau_metricqueryservice_v1_list_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


