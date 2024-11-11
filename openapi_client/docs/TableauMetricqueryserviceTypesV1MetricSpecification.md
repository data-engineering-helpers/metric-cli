# TableauMetricqueryserviceTypesV1MetricSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[TableauMetricqueryserviceTypesV1Filter]**](TableauMetricqueryserviceTypesV1Filter.md) |  | [optional] 
**measurement_period** | [**TableauMetricqueryserviceTypesV1MeasurementPeriod**](TableauMetricqueryserviceTypesV1MeasurementPeriod.md) |  | [optional] 
**comparison** | [**TableauMetricqueryserviceTypesV1CompareConfig**](TableauMetricqueryserviceTypesV1CompareConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_types_v1_metric_specification import TableauMetricqueryserviceTypesV1MetricSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceTypesV1MetricSpecification from a JSON string
tableau_metricqueryservice_types_v1_metric_specification_instance = TableauMetricqueryserviceTypesV1MetricSpecification.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceTypesV1MetricSpecification.to_json())

# convert the object into a dict
tableau_metricqueryservice_types_v1_metric_specification_dict = tableau_metricqueryservice_types_v1_metric_specification_instance.to_dict()
# create an instance of TableauMetricqueryserviceTypesV1MetricSpecification from a dict
tableau_metricqueryservice_types_v1_metric_specification_from_dict = TableauMetricqueryserviceTypesV1MetricSpecification.from_dict(tableau_metricqueryservice_types_v1_metric_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


