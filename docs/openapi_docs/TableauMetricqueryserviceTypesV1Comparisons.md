# TableauMetricqueryserviceTypesV1Comparisons


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparisons** | [**List[TableauMetricqueryserviceTypesV1ComparisonsComparison]**](TableauMetricqueryserviceTypesV1ComparisonsComparison.md) |  | [optional] 
**nested_comparison** | [**TableauMetricqueryserviceTypesV1ComparisonsComparison**](.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_types_v1_comparisons import TableauMetricqueryserviceTypesV1Comparisons

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceTypesV1Comparisons from a JSON string
tableau_metricqueryservice_types_v1_comparisons_instance = TableauMetricqueryserviceTypesV1Comparisons.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceTypesV1Comparisons.to_json())

# convert the object into a dict
tableau_metricqueryservice_types_v1_comparisons_dict = tableau_metricqueryservice_types_v1_comparisons_instance.to_dict()
# create an instance of TableauMetricqueryserviceTypesV1Comparisons from a dict
tableau_metricqueryservice_types_v1_comparisons_from_dict = TableauMetricqueryserviceTypesV1Comparisons.from_dict(tableau_metricqueryservice_types_v1_comparisons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


