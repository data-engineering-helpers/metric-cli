# TableauMetricqueryserviceTypesV1RepresentationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**number_units** | [**TableauMetricqueryserviceTypesV1RepresentationOptionsNumberUnits**](TableauMetricqueryserviceTypesV1RepresentationOptionsNumberUnits.md) |  | [optional] 
**sentiment_type** | **str** |  | [optional] 
**row_level_id_field** | [**TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelIDField**](TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelIDField.md) |  | [optional] 
**row_level_entity_names** | [**TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelEntityNames**](TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelEntityNames.md) |  | [optional] 
**row_level_name_field** | [**TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelNameField**](TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelNameField.md) |  | [optional] 
**currency_code** | **str** |  | [optional] 
**nested_number_units** | [**TableauMetricqueryserviceTypesV1RepresentationOptionsNumberUnits**](.md) |  | [optional] 
**nested_row_level_id_field** | [**TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelIDField**](.md) |  | [optional] 
**nested_row_level_name_field** | [**TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelNameField**](.md) |  | [optional] 
**nested_row_level_entity_names** | [**TableauMetricqueryserviceTypesV1RepresentationOptionsRowLevelEntityNames**](.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_types_v1_representation_options import TableauMetricqueryserviceTypesV1RepresentationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceTypesV1RepresentationOptions from a JSON string
tableau_metricqueryservice_types_v1_representation_options_instance = TableauMetricqueryserviceTypesV1RepresentationOptions.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceTypesV1RepresentationOptions.to_json())

# convert the object into a dict
tableau_metricqueryservice_types_v1_representation_options_dict = tableau_metricqueryservice_types_v1_representation_options_instance.to_dict()
# create an instance of TableauMetricqueryserviceTypesV1RepresentationOptions from a dict
tableau_metricqueryservice_types_v1_representation_options_from_dict = TableauMetricqueryserviceTypesV1RepresentationOptions.from_dict(tableau_metricqueryservice_types_v1_representation_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


