# TableauUsagestatsV1BatchGetUsageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_items** | [**List[TableauUsagestatsV1ContentItemId]**](TableauUsagestatsV1ContentItemId.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_usagestats_v1_batch_get_usage_request import TableauUsagestatsV1BatchGetUsageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauUsagestatsV1BatchGetUsageRequest from a JSON string
tableau_usagestats_v1_batch_get_usage_request_instance = TableauUsagestatsV1BatchGetUsageRequest.from_json(json)
# print the JSON string representation of the object
print(TableauUsagestatsV1BatchGetUsageRequest.to_json())

# convert the object into a dict
tableau_usagestats_v1_batch_get_usage_request_dict = tableau_usagestats_v1_batch_get_usage_request_instance.to_dict()
# create an instance of TableauUsagestatsV1BatchGetUsageRequest from a dict
tableau_usagestats_v1_batch_get_usage_request_from_dict = TableauUsagestatsV1BatchGetUsageRequest.from_dict(tableau_usagestats_v1_batch_get_usage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


