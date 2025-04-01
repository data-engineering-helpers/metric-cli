# TableauMetricqueryserviceV1GetOrCreateMetricResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**TableauMetricqueryserviceTypesV1Metric**](TableauMetricqueryserviceTypesV1Metric.md) |  | [optional] 
**is_metric_created** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_v1_get_or_create_metric_response import TableauMetricqueryserviceV1GetOrCreateMetricResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceV1GetOrCreateMetricResponse from a JSON string
tableau_metricqueryservice_v1_get_or_create_metric_response_instance = TableauMetricqueryserviceV1GetOrCreateMetricResponse.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceV1GetOrCreateMetricResponse.to_json())

# convert the object into a dict
tableau_metricqueryservice_v1_get_or_create_metric_response_dict = tableau_metricqueryservice_v1_get_or_create_metric_response_instance.to_dict()
# create an instance of TableauMetricqueryserviceV1GetOrCreateMetricResponse from a dict
tableau_metricqueryservice_v1_get_or_create_metric_response_from_dict = TableauMetricqueryserviceV1GetOrCreateMetricResponse.from_dict(tableau_metricqueryservice_v1_get_or_create_metric_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


