# TableauAnalyticsextensionsV1ConnectionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_luid** | **str** |  | [optional] 
**connection_brief** | [**TableauAnalyticsextensionsV1ConnectionBrief**](TableauAnalyticsextensionsV1ConnectionBrief.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_analyticsextensions_v1_connection_metadata import TableauAnalyticsextensionsV1ConnectionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAnalyticsextensionsV1ConnectionMetadata from a JSON string
tableau_analyticsextensions_v1_connection_metadata_instance = TableauAnalyticsextensionsV1ConnectionMetadata.from_json(json)
# print the JSON string representation of the object
print(TableauAnalyticsextensionsV1ConnectionMetadata.to_json())

# convert the object into a dict
tableau_analyticsextensions_v1_connection_metadata_dict = tableau_analyticsextensions_v1_connection_metadata_instance.to_dict()
# create an instance of TableauAnalyticsextensionsV1ConnectionMetadata from a dict
tableau_analyticsextensions_v1_connection_metadata_from_dict = TableauAnalyticsextensionsV1ConnectionMetadata.from_dict(tableau_analyticsextensions_v1_connection_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


