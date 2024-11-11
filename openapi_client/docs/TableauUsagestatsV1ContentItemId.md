# TableauUsagestatsV1ContentItemId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**luid** | **str** |  | [optional] 
**type** | **str** | The content type of the specified item, for instance: workbook, flow, and datasource. Note the content type of a member of the &#x60;content_items&#x60; array refers to a single instance of a resource. | [optional] 

## Example

```python
from openapi_client.models.tableau_usagestats_v1_content_item_id import TableauUsagestatsV1ContentItemId

# TODO update the JSON string below
json = "{}"
# create an instance of TableauUsagestatsV1ContentItemId from a JSON string
tableau_usagestats_v1_content_item_id_instance = TableauUsagestatsV1ContentItemId.from_json(json)
# print the JSON string representation of the object
print(TableauUsagestatsV1ContentItemId.to_json())

# convert the object into a dict
tableau_usagestats_v1_content_item_id_dict = tableau_usagestats_v1_content_item_id_instance.to_dict()
# create an instance of TableauUsagestatsV1ContentItemId from a dict
tableau_usagestats_v1_content_item_id_from_dict = TableauUsagestatsV1ContentItemId.from_dict(tableau_usagestats_v1_content_item_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


