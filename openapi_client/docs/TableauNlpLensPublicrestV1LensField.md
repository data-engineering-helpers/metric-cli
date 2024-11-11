# TableauNlpLensPublicrestV1LensField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph_id** | **str** | Ask data generated internal id of the field. | [optional] 
**custom_label** | **str** | Custom Label of the lens field. If not specified, the field inherits label from the corresponding datasource field. | [optional] 
**custom_description** | **str** | Custom Description of the lens field. If not specified, the field inherits description from the corresponding datasource field. | [optional] 
**field_synonyms** | **List[str]** |  | [optional] 
**inherited_field_synonyms** | **List[str]** |  | [optional] 
**value_synonyms** | [**List[TableauNlpLensPublicrestV1ValueSynonym]**](TableauNlpLensPublicrestV1ValueSynonym.md) |  | [optional] 
**inherited_value_synonyms** | [**List[TableauNlpLensPublicrestV1ValueSynonym]**](TableauNlpLensPublicrestV1ValueSynonym.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_nlp_lens_publicrest_v1_lens_field import TableauNlpLensPublicrestV1LensField

# TODO update the JSON string below
json = "{}"
# create an instance of TableauNlpLensPublicrestV1LensField from a JSON string
tableau_nlp_lens_publicrest_v1_lens_field_instance = TableauNlpLensPublicrestV1LensField.from_json(json)
# print the JSON string representation of the object
print(TableauNlpLensPublicrestV1LensField.to_json())

# convert the object into a dict
tableau_nlp_lens_publicrest_v1_lens_field_dict = tableau_nlp_lens_publicrest_v1_lens_field_instance.to_dict()
# create an instance of TableauNlpLensPublicrestV1LensField from a dict
tableau_nlp_lens_publicrest_v1_lens_field_from_dict = TableauNlpLensPublicrestV1LensField.from_dict(tableau_nlp_lens_publicrest_v1_lens_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


