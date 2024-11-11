# TableauEventserviceV1PublishUIEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**data_source_id** | **str** |  | [optional] 
**metric_id** | **str** |  | [optional] 
**scoped_metric_id** | **str** |  | [optional] 
**feature_flags** | **str** |  | [optional] 
**metric_definition_type** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**browser** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**embedded_api_version** | **str** |  | [optional] 
**tableau_version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_eventservice_v1_publish_ui_event_request import TableauEventserviceV1PublishUIEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauEventserviceV1PublishUIEventRequest from a JSON string
tableau_eventservice_v1_publish_ui_event_request_instance = TableauEventserviceV1PublishUIEventRequest.from_json(json)
# print the JSON string representation of the object
print(TableauEventserviceV1PublishUIEventRequest.to_json())

# convert the object into a dict
tableau_eventservice_v1_publish_ui_event_request_dict = tableau_eventservice_v1_publish_ui_event_request_instance.to_dict()
# create an instance of TableauEventserviceV1PublishUIEventRequest from a dict
tableau_eventservice_v1_publish_ui_event_request_from_dict = TableauEventserviceV1PublishUIEventRequest.from_dict(tableau_eventservice_v1_publish_ui_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


