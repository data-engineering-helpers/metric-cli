# TableauError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_error_code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_error import TableauError

# TODO update the JSON string below
json = "{}"
# create an instance of TableauError from a JSON string
tableau_error_instance = TableauError.from_json(json)
# print the JSON string representation of the object
print(TableauError.to_json())

# convert the object into a dict
tableau_error_dict = tableau_error_instance.to_dict()
# create an instance of TableauError from a dict
tableau_error_from_dict = TableauError.from_dict(tableau_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


