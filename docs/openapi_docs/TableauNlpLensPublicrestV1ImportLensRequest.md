# TableauNlpLensPublicrestV1ImportLensRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lens** | [**TableauNlpLensPublicrestV1Lens**](TableauNlpLensPublicrestV1Lens.md) |  | [optional] 
**lens_transformations** | [**TableauNlpLensPublicrestV1LensTransformation**](TableauNlpLensPublicrestV1LensTransformation.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_nlp_lens_publicrest_v1_import_lens_request import TableauNlpLensPublicrestV1ImportLensRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauNlpLensPublicrestV1ImportLensRequest from a JSON string
tableau_nlp_lens_publicrest_v1_import_lens_request_instance = TableauNlpLensPublicrestV1ImportLensRequest.from_json(json)
# print the JSON string representation of the object
print(TableauNlpLensPublicrestV1ImportLensRequest.to_json())

# convert the object into a dict
tableau_nlp_lens_publicrest_v1_import_lens_request_dict = tableau_nlp_lens_publicrest_v1_import_lens_request_instance.to_dict()
# create an instance of TableauNlpLensPublicrestV1ImportLensRequest from a dict
tableau_nlp_lens_publicrest_v1_import_lens_request_from_dict = TableauNlpLensPublicrestV1ImportLensRequest.from_dict(tableau_nlp_lens_publicrest_v1_import_lens_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


