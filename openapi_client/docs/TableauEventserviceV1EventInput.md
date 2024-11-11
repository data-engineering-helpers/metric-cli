# TableauEventserviceV1EventInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**details** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_eventservice_v1_event_input import TableauEventserviceV1EventInput

# TODO update the JSON string below
json = "{}"
# create an instance of TableauEventserviceV1EventInput from a JSON string
tableau_eventservice_v1_event_input_instance = TableauEventserviceV1EventInput.from_json(json)
# print the JSON string representation of the object
print(TableauEventserviceV1EventInput.to_json())

# convert the object into a dict
tableau_eventservice_v1_event_input_dict = tableau_eventservice_v1_event_input_instance.to_dict()
# create an instance of TableauEventserviceV1EventInput from a dict
tableau_eventservice_v1_event_input_from_dict = TableauEventserviceV1EventInput.from_dict(tableau_eventservice_v1_event_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


