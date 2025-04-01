# TableauPulseInsightsserviceV1SummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**TableauPulseInsightsserviceV1Summary**](TableauPulseInsightsserviceV1Summary.md) |  | [optional] 
**error** | [**TableauPulseInsightsserviceV1Error**](TableauPulseInsightsserviceV1Error.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_insightsservice_v1_summary_response import TableauPulseInsightsserviceV1SummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseInsightsserviceV1SummaryResponse from a JSON string
tableau_pulse_insightsservice_v1_summary_response_instance = TableauPulseInsightsserviceV1SummaryResponse.from_json(json)
# print the JSON string representation of the object
print(TableauPulseInsightsserviceV1SummaryResponse.to_json())

# convert the object into a dict
tableau_pulse_insightsservice_v1_summary_response_dict = tableau_pulse_insightsservice_v1_summary_response_instance.to_dict()
# create an instance of TableauPulseInsightsserviceV1SummaryResponse from a dict
tableau_pulse_insightsservice_v1_summary_response_from_dict = TableauPulseInsightsserviceV1SummaryResponse.from_dict(tableau_pulse_insightsservice_v1_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


