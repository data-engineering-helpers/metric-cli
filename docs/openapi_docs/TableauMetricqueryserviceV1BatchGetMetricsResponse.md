# TableauMetricqueryserviceV1BatchGetMetricsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[TableauMetricqueryserviceTypesV1Metric]**](TableauMetricqueryserviceTypesV1Metric.md) |  | [optional] 
**errors** | [**List[TableauMetricqueryserviceTypesV1BatchGetMetricErrors]**](TableauMetricqueryserviceTypesV1BatchGetMetricErrors.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_v1_batch_get_metrics_response import TableauMetricqueryserviceV1BatchGetMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceV1BatchGetMetricsResponse from a JSON string
tableau_metricqueryservice_v1_batch_get_metrics_response_instance = TableauMetricqueryserviceV1BatchGetMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceV1BatchGetMetricsResponse.to_json())

# convert the object into a dict
tableau_metricqueryservice_v1_batch_get_metrics_response_dict = tableau_metricqueryservice_v1_batch_get_metrics_response_instance.to_dict()
# create an instance of TableauMetricqueryserviceV1BatchGetMetricsResponse from a dict
tableau_metricqueryservice_v1_batch_get_metrics_response_from_dict = TableauMetricqueryserviceV1BatchGetMetricsResponse.from_dict(tableau_metricqueryservice_v1_batch_get_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


