# TableauPulseInsightsserviceV1InsightResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**TableauPulseInsightsserviceV1Insight**](TableauPulseInsightsserviceV1Insight.md) |  | [optional] 
**error** | [**TableauPulseInsightsserviceV1Error**](TableauPulseInsightsserviceV1Error.md) |  | [optional] 
**insight_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_insightsservice_v1_insight_response import TableauPulseInsightsserviceV1InsightResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseInsightsserviceV1InsightResponse from a JSON string
tableau_pulse_insightsservice_v1_insight_response_instance = TableauPulseInsightsserviceV1InsightResponse.from_json(json)
# print the JSON string representation of the object
print(TableauPulseInsightsserviceV1InsightResponse.to_json())

# convert the object into a dict
tableau_pulse_insightsservice_v1_insight_response_dict = tableau_pulse_insightsservice_v1_insight_response_instance.to_dict()
# create an instance of TableauPulseInsightsserviceV1InsightResponse from a dict
tableau_pulse_insightsservice_v1_insight_response_from_dict = TableauPulseInsightsserviceV1InsightResponse.from_dict(tableau_pulse_insightsservice_v1_insight_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


