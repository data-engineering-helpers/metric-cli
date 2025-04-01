# TableauMetricqueryserviceTypesV1BasicSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measure** | [**TableauMetricqueryserviceTypesV1Measure**](TableauMetricqueryserviceTypesV1Measure.md) |  | [optional] 
**time_dimension** | [**TableauMetricqueryserviceTypesV1TimeDimension**](TableauMetricqueryserviceTypesV1TimeDimension.md) |  | [optional] 
**filters** | [**List[TableauMetricqueryserviceTypesV1Filter]**](TableauMetricqueryserviceTypesV1Filter.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_types_v1_basic_specification import TableauMetricqueryserviceTypesV1BasicSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceTypesV1BasicSpecification from a JSON string
tableau_metricqueryservice_types_v1_basic_specification_instance = TableauMetricqueryserviceTypesV1BasicSpecification.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceTypesV1BasicSpecification.to_json())

# convert the object into a dict
tableau_metricqueryservice_types_v1_basic_specification_dict = tableau_metricqueryservice_types_v1_basic_specification_instance.to_dict()
# create an instance of TableauMetricqueryserviceTypesV1BasicSpecification from a dict
tableau_metricqueryservice_types_v1_basic_specification_from_dict = TableauMetricqueryserviceTypesV1BasicSpecification.from_dict(tableau_metricqueryservice_types_v1_basic_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


