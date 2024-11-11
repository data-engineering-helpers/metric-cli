# TableauNlpLensPublicrestV1FieldDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph_id** | **str** | Required. Field identifier for ask data. In most cases this is the column name. But for cases where the same column name repeats in multiple objects, calculated fields, or for hierarchy fields this is derived from TDS rules. To identify the graph id for a particular field, you could create a test lens with all fields from the datasource and invoke GetLens API to get a list of all fields and their field graph ids. | [optional] 
**custom_label** | **str** | Optional. Custom Label of the lens field. If not specified, the field inherits label from the corresponding datasource field. Up to 50 characters long | [optional] 
**custom_description** | **str** | Optional. Custom Description of the lens field. If not specified, the field inherits description from the corresponding datasource field. Up to 4000 characters long | [optional] 
**field_synonyms** | **List[str]** |  | [optional] 
**value_synonyms** | [**List[TableauNlpLensPublicrestV1ValueSynonym]**](TableauNlpLensPublicrestV1ValueSynonym.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_nlp_lens_publicrest_v1_field_detail import TableauNlpLensPublicrestV1FieldDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TableauNlpLensPublicrestV1FieldDetail from a JSON string
tableau_nlp_lens_publicrest_v1_field_detail_instance = TableauNlpLensPublicrestV1FieldDetail.from_json(json)
# print the JSON string representation of the object
print(TableauNlpLensPublicrestV1FieldDetail.to_json())

# convert the object into a dict
tableau_nlp_lens_publicrest_v1_field_detail_dict = tableau_nlp_lens_publicrest_v1_field_detail_instance.to_dict()
# create an instance of TableauNlpLensPublicrestV1FieldDetail from a dict
tableau_nlp_lens_publicrest_v1_field_detail_from_dict = TableauNlpLensPublicrestV1FieldDetail.from_dict(tableau_nlp_lens_publicrest_v1_field_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


