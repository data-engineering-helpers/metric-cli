# TableauEventserviceTypesV1Event


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 
**service** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**site_id** | **int** |  | [optional] 
**session_id** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**event_properties** | [**GoogleProtobufAny**](GoogleProtobufAny.md) |  | [optional] 
**site_luid** | **str** |  | [optional] 
**user_luid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_eventservice_types_v1_event import TableauEventserviceTypesV1Event

# TODO update the JSON string below
json = "{}"
# create an instance of TableauEventserviceTypesV1Event from a JSON string
tableau_eventservice_types_v1_event_instance = TableauEventserviceTypesV1Event.from_json(json)
# print the JSON string representation of the object
print(TableauEventserviceTypesV1Event.to_json())

# convert the object into a dict
tableau_eventservice_types_v1_event_dict = tableau_eventservice_types_v1_event_instance.to_dict()
# create an instance of TableauEventserviceTypesV1Event from a dict
tableau_eventservice_types_v1_event_from_dict = TableauEventserviceTypesV1Event.from_dict(tableau_eventservice_types_v1_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


