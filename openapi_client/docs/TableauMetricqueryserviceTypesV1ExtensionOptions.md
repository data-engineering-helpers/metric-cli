# TableauMetricqueryserviceTypesV1ExtensionOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_dimensions** | **List[str]** |  | [optional] 
**allowed_granularities** | **List[str]** |  | [optional] 
**offset_from_today** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_types_v1_extension_options import TableauMetricqueryserviceTypesV1ExtensionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceTypesV1ExtensionOptions from a JSON string
tableau_metricqueryservice_types_v1_extension_options_instance = TableauMetricqueryserviceTypesV1ExtensionOptions.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceTypesV1ExtensionOptions.to_json())

# convert the object into a dict
tableau_metricqueryservice_types_v1_extension_options_dict = tableau_metricqueryservice_types_v1_extension_options_instance.to_dict()
# create an instance of TableauMetricqueryserviceTypesV1ExtensionOptions from a dict
tableau_metricqueryservice_types_v1_extension_options_from_dict = TableauMetricqueryserviceTypesV1ExtensionOptions.from_dict(tableau_metricqueryservice_types_v1_extension_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


