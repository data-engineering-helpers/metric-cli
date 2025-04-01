# TableauMetricqueryserviceV1CreateMetricRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition_id** | **str** |  | [optional] 
**specification** | [**TableauMetricqueryserviceTypesV1MetricSpecification**](TableauMetricqueryserviceTypesV1MetricSpecification.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_v1_create_metric_request import TableauMetricqueryserviceV1CreateMetricRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceV1CreateMetricRequest from a JSON string
tableau_metricqueryservice_v1_create_metric_request_instance = TableauMetricqueryserviceV1CreateMetricRequest.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceV1CreateMetricRequest.to_json())

# convert the object into a dict
tableau_metricqueryservice_v1_create_metric_request_dict = tableau_metricqueryservice_v1_create_metric_request_instance.to_dict()
# create an instance of TableauMetricqueryserviceV1CreateMetricRequest from a dict
tableau_metricqueryservice_v1_create_metric_request_from_dict = TableauMetricqueryserviceV1CreateMetricRequest.from_dict(tableau_metricqueryservice_v1_create_metric_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


