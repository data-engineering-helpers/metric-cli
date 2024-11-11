# TableauNlpLensPublicrestV1ListLensItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Luid of the lens | [optional] 
**name** | **str** | Name of the lens | [optional] 
**site_id** | **str** | Luid of the site to which the lens belong to. | [optional] 
**datasource_id** | **str** | Luid of the datasource to which the lens is associated to. | [optional] 
**project_id** | **str** | Luid of the project. | [optional] 
**owner_id** | **str** | Luid of the owner of the lens. | [optional] 
**description** | **str** | Description of the lens. | [optional] 
**repository_url** | **str** | Internal URL to access the lens. | [optional] 

## Example

```python
from openapi_client.models.tableau_nlp_lens_publicrest_v1_list_lens_item import TableauNlpLensPublicrestV1ListLensItem

# TODO update the JSON string below
json = "{}"
# create an instance of TableauNlpLensPublicrestV1ListLensItem from a JSON string
tableau_nlp_lens_publicrest_v1_list_lens_item_instance = TableauNlpLensPublicrestV1ListLensItem.from_json(json)
# print the JSON string representation of the object
print(TableauNlpLensPublicrestV1ListLensItem.to_json())

# convert the object into a dict
tableau_nlp_lens_publicrest_v1_list_lens_item_dict = tableau_nlp_lens_publicrest_v1_list_lens_item_instance.to_dict()
# create an instance of TableauNlpLensPublicrestV1ListLensItem from a dict
tableau_nlp_lens_publicrest_v1_list_lens_item_from_dict = TableauNlpLensPublicrestV1ListLensItem.from_dict(tableau_nlp_lens_publicrest_v1_list_lens_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


