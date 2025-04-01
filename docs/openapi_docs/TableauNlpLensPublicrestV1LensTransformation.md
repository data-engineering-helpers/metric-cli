# TableauNlpLensPublicrestV1LensTransformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Optional. If provided, this will be the name of the imported lens. Upto 300 characters | [optional] 
**description** | **str** | Optional. If provided, this will be the description of the imported lens. 4000 characters maximum | [optional] 
**datasource_id** | **str** | Optional. If provided, this will be luid of the datasource to which the lens is associated to | [optional] 
**project_id** | **str** | Optional. If provided, this will be the luid of the project to which the lens will be imported to. | [optional] 
**owner_id** | **str** | Optional. If provided, this will be the luid of the owner of the lens. | [optional] 

## Example

```python
from openapi_client.models.tableau_nlp_lens_publicrest_v1_lens_transformation import TableauNlpLensPublicrestV1LensTransformation

# TODO update the JSON string below
json = "{}"
# create an instance of TableauNlpLensPublicrestV1LensTransformation from a JSON string
tableau_nlp_lens_publicrest_v1_lens_transformation_instance = TableauNlpLensPublicrestV1LensTransformation.from_json(json)
# print the JSON string representation of the object
print(TableauNlpLensPublicrestV1LensTransformation.to_json())

# convert the object into a dict
tableau_nlp_lens_publicrest_v1_lens_transformation_dict = tableau_nlp_lens_publicrest_v1_lens_transformation_instance.to_dict()
# create an instance of TableauNlpLensPublicrestV1LensTransformation from a dict
tableau_nlp_lens_publicrest_v1_lens_transformation_from_dict = TableauNlpLensPublicrestV1LensTransformation.from_dict(tableau_nlp_lens_publicrest_v1_lens_transformation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


