# TableauMetricqueryserviceTypesV1Metric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**specification** | [**TableauMetricqueryserviceTypesV1MetricSpecification**](TableauMetricqueryserviceTypesV1MetricSpecification.md) |  | [optional] 
**definition_id** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**schema_version** | **str** |  | [optional] 
**metric_version** | **int** |  | [optional] 
**goals** | [**TableauMetricqueryserviceTypesV1MetricGoals**](TableauMetricqueryserviceTypesV1MetricGoals.md) |  | [optional] 
**is_followed** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_types_v1_metric import TableauMetricqueryserviceTypesV1Metric

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceTypesV1Metric from a JSON string
tableau_metricqueryservice_types_v1_metric_instance = TableauMetricqueryserviceTypesV1Metric.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceTypesV1Metric.to_json())

# convert the object into a dict
tableau_metricqueryservice_types_v1_metric_dict = tableau_metricqueryservice_types_v1_metric_instance.to_dict()
# create an instance of TableauMetricqueryserviceTypesV1Metric from a dict
tableau_metricqueryservice_types_v1_metric_from_dict = TableauMetricqueryserviceTypesV1Metric.from_dict(tableau_metricqueryservice_types_v1_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


