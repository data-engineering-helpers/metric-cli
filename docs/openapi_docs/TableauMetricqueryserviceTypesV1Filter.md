# TableauMetricqueryserviceTypesV1Filter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**operator** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 
**include_null** | **bool** |  | [optional] 
**categorical_values** | [**List[TableauMetricqueryserviceTypesV1CategoricalValue]**](TableauMetricqueryserviceTypesV1CategoricalValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_types_v1_filter import TableauMetricqueryserviceTypesV1Filter

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceTypesV1Filter from a JSON string
tableau_metricqueryservice_types_v1_filter_instance = TableauMetricqueryserviceTypesV1Filter.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceTypesV1Filter.to_json())

# convert the object into a dict
tableau_metricqueryservice_types_v1_filter_dict = tableau_metricqueryservice_types_v1_filter_instance.to_dict()
# create an instance of TableauMetricqueryserviceTypesV1Filter from a dict
tableau_metricqueryservice_types_v1_filter_from_dict = TableauMetricqueryserviceTypesV1Filter.from_dict(tableau_metricqueryservice_types_v1_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


