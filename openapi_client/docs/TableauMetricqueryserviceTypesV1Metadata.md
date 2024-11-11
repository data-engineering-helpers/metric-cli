# TableauMetricqueryserviceTypesV1Metadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**user_link** | **str** |  | [optional] 
**user_link_name** | **str** |  | [optional] 
**schema_version** | **str** |  | [optional] 
**metric_version** | **int** |  | [optional] 
**definition_version** | **int** |  | [optional] 
**last_updated_user** | [**TableauMetricqueryserviceTypesV1MetadataUser**](TableauMetricqueryserviceTypesV1MetadataUser.md) |  | [optional] 
**nested_user** | [**TableauMetricqueryserviceTypesV1MetadataUser**](.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_types_v1_metadata import TableauMetricqueryserviceTypesV1Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceTypesV1Metadata from a JSON string
tableau_metricqueryservice_types_v1_metadata_instance = TableauMetricqueryserviceTypesV1Metadata.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceTypesV1Metadata.to_json())

# convert the object into a dict
tableau_metricqueryservice_types_v1_metadata_dict = tableau_metricqueryservice_types_v1_metadata_instance.to_dict()
# create an instance of TableauMetricqueryserviceTypesV1Metadata from a dict
tableau_metricqueryservice_types_v1_metadata_from_dict = TableauMetricqueryserviceTypesV1Metadata.from_dict(tableau_metricqueryservice_types_v1_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


