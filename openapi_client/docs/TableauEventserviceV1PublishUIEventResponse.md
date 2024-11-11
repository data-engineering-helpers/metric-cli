# TableauEventserviceV1PublishUIEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**TableauEventserviceTypesV1Event**](TableauEventserviceTypesV1Event.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_eventservice_v1_publish_ui_event_response import TableauEventserviceV1PublishUIEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauEventserviceV1PublishUIEventResponse from a JSON string
tableau_eventservice_v1_publish_ui_event_response_instance = TableauEventserviceV1PublishUIEventResponse.from_json(json)
# print the JSON string representation of the object
print(TableauEventserviceV1PublishUIEventResponse.to_json())

# convert the object into a dict
tableau_eventservice_v1_publish_ui_event_response_dict = tableau_eventservice_v1_publish_ui_event_response_instance.to_dict()
# create an instance of TableauEventserviceV1PublishUIEventResponse from a dict
tableau_eventservice_v1_publish_ui_event_response_from_dict = TableauEventserviceV1PublishUIEventResponse.from_dict(tableau_eventservice_v1_publish_ui_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


