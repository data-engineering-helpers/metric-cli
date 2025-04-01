# TableauMetricqueryserviceTypesV1MetricGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_metadata** | [**TableauMetricqueryserviceTypesV1MetricGroupGroupMetadata**](TableauMetricqueryserviceTypesV1MetricGroupGroupMetadata.md) |  | [optional] 
**metrics** | [**List[TableauMetricqueryserviceTypesV1Metric]**](TableauMetricqueryserviceTypesV1Metric.md) |  | [optional] 
**nested_group_metadata** | [**TableauMetricqueryserviceTypesV1MetricGroupGroupMetadata**](.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_types_v1_metric_group import TableauMetricqueryserviceTypesV1MetricGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceTypesV1MetricGroup from a JSON string
tableau_metricqueryservice_types_v1_metric_group_instance = TableauMetricqueryserviceTypesV1MetricGroup.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceTypesV1MetricGroup.to_json())

# convert the object into a dict
tableau_metricqueryservice_types_v1_metric_group_dict = tableau_metricqueryservice_types_v1_metric_group_instance.to_dict()
# create an instance of TableauMetricqueryserviceTypesV1MetricGroup from a dict
tableau_metricqueryservice_types_v1_metric_group_from_dict = TableauMetricqueryserviceTypesV1MetricGroup.from_dict(tableau_metricqueryservice_types_v1_metric_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


