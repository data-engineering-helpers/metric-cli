# TableauNlpLensPublicrestV1CreateLensRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Required. Name of the lens . Upto 300 characters | [optional] 
**datasource_id** | **str** | Required. Luid of the datasource to which the lens is associated to | [optional] 
**project_id** | **str** | Required. Luid of the project in which lens should be created. | [optional] 
**description** | **str** | Optional. Description of the lens. 4000 characters maximum | [optional] 
**is_feedback_enabled** | **bool** | Required. Indicates if feedback to lens author setting is enabled. | [optional] 
**fields** | [**List[TableauNlpLensPublicrestV1FieldDetail]**](TableauNlpLensPublicrestV1FieldDetail.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_nlp_lens_publicrest_v1_create_lens_request import TableauNlpLensPublicrestV1CreateLensRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauNlpLensPublicrestV1CreateLensRequest from a JSON string
tableau_nlp_lens_publicrest_v1_create_lens_request_instance = TableauNlpLensPublicrestV1CreateLensRequest.from_json(json)
# print the JSON string representation of the object
print(TableauNlpLensPublicrestV1CreateLensRequest.to_json())

# convert the object into a dict
tableau_nlp_lens_publicrest_v1_create_lens_request_dict = tableau_nlp_lens_publicrest_v1_create_lens_request_instance.to_dict()
# create an instance of TableauNlpLensPublicrestV1CreateLensRequest from a dict
tableau_nlp_lens_publicrest_v1_create_lens_request_from_dict = TableauNlpLensPublicrestV1CreateLensRequest.from_dict(tableau_nlp_lens_publicrest_v1_create_lens_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


