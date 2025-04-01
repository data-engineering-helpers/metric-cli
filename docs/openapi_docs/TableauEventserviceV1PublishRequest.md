# TableauEventserviceV1PublishRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] 
**event** | [**TableauEventserviceV1EventInput**](TableauEventserviceV1EventInput.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_eventservice_v1_publish_request import TableauEventserviceV1PublishRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauEventserviceV1PublishRequest from a JSON string
tableau_eventservice_v1_publish_request_instance = TableauEventserviceV1PublishRequest.from_json(json)
# print the JSON string representation of the object
print(TableauEventserviceV1PublishRequest.to_json())

# convert the object into a dict
tableau_eventservice_v1_publish_request_dict = tableau_eventservice_v1_publish_request_instance.to_dict()
# create an instance of TableauEventserviceV1PublishRequest from a dict
tableau_eventservice_v1_publish_request_from_dict = TableauEventserviceV1PublishRequest.from_dict(tableau_eventservice_v1_publish_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


