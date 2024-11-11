# TableauNlpLensPublicrestV1RecommendedVisualizationGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of group. | [optional] 
**description** | **str** | Description of group. | [optional] 
**recommended_visualizations** | [**List[TableauNlpLensPublicrestV1RecommendedVisualization]**](TableauNlpLensPublicrestV1RecommendedVisualization.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_nlp_lens_publicrest_v1_recommended_visualization_group import TableauNlpLensPublicrestV1RecommendedVisualizationGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TableauNlpLensPublicrestV1RecommendedVisualizationGroup from a JSON string
tableau_nlp_lens_publicrest_v1_recommended_visualization_group_instance = TableauNlpLensPublicrestV1RecommendedVisualizationGroup.from_json(json)
# print the JSON string representation of the object
print(TableauNlpLensPublicrestV1RecommendedVisualizationGroup.to_json())

# convert the object into a dict
tableau_nlp_lens_publicrest_v1_recommended_visualization_group_dict = tableau_nlp_lens_publicrest_v1_recommended_visualization_group_instance.to_dict()
# create an instance of TableauNlpLensPublicrestV1RecommendedVisualizationGroup from a dict
tableau_nlp_lens_publicrest_v1_recommended_visualization_group_from_dict = TableauNlpLensPublicrestV1RecommendedVisualizationGroup.from_dict(tableau_nlp_lens_publicrest_v1_recommended_visualization_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


