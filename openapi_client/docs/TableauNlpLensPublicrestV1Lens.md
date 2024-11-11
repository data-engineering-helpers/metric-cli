# TableauNlpLensPublicrestV1Lens


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
**is_feedback_enabled** | **bool** | Indicates if feedback to lens author setting is enabled | [optional] 
**fields** | [**List[TableauNlpLensPublicrestV1LensField]**](TableauNlpLensPublicrestV1LensField.md) |  | [optional] 
**recommended_visualization_groups** | [**List[TableauNlpLensPublicrestV1RecommendedVisualizationGroup]**](TableauNlpLensPublicrestV1RecommendedVisualizationGroup.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_nlp_lens_publicrest_v1_lens import TableauNlpLensPublicrestV1Lens

# TODO update the JSON string below
json = "{}"
# create an instance of TableauNlpLensPublicrestV1Lens from a JSON string
tableau_nlp_lens_publicrest_v1_lens_instance = TableauNlpLensPublicrestV1Lens.from_json(json)
# print the JSON string representation of the object
print(TableauNlpLensPublicrestV1Lens.to_json())

# convert the object into a dict
tableau_nlp_lens_publicrest_v1_lens_dict = tableau_nlp_lens_publicrest_v1_lens_instance.to_dict()
# create an instance of TableauNlpLensPublicrestV1Lens from a dict
tableau_nlp_lens_publicrest_v1_lens_from_dict = TableauNlpLensPublicrestV1Lens.from_dict(tableau_nlp_lens_publicrest_v1_lens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


