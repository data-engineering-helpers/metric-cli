# TableauEventserviceV1PublishResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**TableauEventserviceTypesV1Event**](TableauEventserviceTypesV1Event.md) |  | [optional] 
**serialized_event** | [**TableauEventserviceTypesV1SerializedEvent**](TableauEventserviceTypesV1SerializedEvent.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_eventservice_v1_publish_response import TableauEventserviceV1PublishResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauEventserviceV1PublishResponse from a JSON string
tableau_eventservice_v1_publish_response_instance = TableauEventserviceV1PublishResponse.from_json(json)
# print the JSON string representation of the object
print(TableauEventserviceV1PublishResponse.to_json())

# convert the object into a dict
tableau_eventservice_v1_publish_response_dict = tableau_eventservice_v1_publish_response_instance.to_dict()
# create an instance of TableauEventserviceV1PublishResponse from a dict
tableau_eventservice_v1_publish_response_from_dict = TableauEventserviceV1PublishResponse.from_dict(tableau_eventservice_v1_publish_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


