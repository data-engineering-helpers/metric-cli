# TableauPulseInsightsserviceV1Summary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**markup** | **str** |  | [optional] 
**viz** | **object** |  | [optional] 
**generation_id** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**last_attempted_timestamp** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_insightsservice_v1_summary import TableauPulseInsightsserviceV1Summary

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseInsightsserviceV1Summary from a JSON string
tableau_pulse_insightsservice_v1_summary_instance = TableauPulseInsightsserviceV1Summary.from_json(json)
# print the JSON string representation of the object
print(TableauPulseInsightsserviceV1Summary.to_json())

# convert the object into a dict
tableau_pulse_insightsservice_v1_summary_dict = tableau_pulse_insightsservice_v1_summary_instance.to_dict()
# create an instance of TableauPulseInsightsserviceV1Summary from a dict
tableau_pulse_insightsservice_v1_summary_from_dict = TableauPulseInsightsserviceV1Summary.from_dict(tableau_pulse_insightsservice_v1_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


