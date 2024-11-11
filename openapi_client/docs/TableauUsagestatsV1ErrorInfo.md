# TableauUsagestatsV1ErrorInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_error_code** | **int** | The error code for a failure to return statistics for a content item in the requested batch. | [optional] 
**message** | **str** | The error message for a failure to return statistics for a content item in the requested batch. | [optional] 

## Example

```python
from openapi_client.models.tableau_usagestats_v1_error_info import TableauUsagestatsV1ErrorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TableauUsagestatsV1ErrorInfo from a JSON string
tableau_usagestats_v1_error_info_instance = TableauUsagestatsV1ErrorInfo.from_json(json)
# print the JSON string representation of the object
print(TableauUsagestatsV1ErrorInfo.to_json())

# convert the object into a dict
tableau_usagestats_v1_error_info_dict = tableau_usagestats_v1_error_info_instance.to_dict()
# create an instance of TableauUsagestatsV1ErrorInfo from a dict
tableau_usagestats_v1_error_info_from_dict = TableauUsagestatsV1ErrorInfo.from_dict(tableau_usagestats_v1_error_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


