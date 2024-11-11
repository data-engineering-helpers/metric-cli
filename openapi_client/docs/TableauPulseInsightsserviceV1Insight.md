# TableauPulseInsightsserviceV1Insight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**content** | **str** |  | [optional] 
**markup** | **str** |  | [optional] 
**viz** | **object** |  | [optional] 
**facts** | **object** |  | [optional] 
**characterization** | **str** |  | [optional] 
**question** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**insight_feedback_metadata** | [**TableauPulseInsightsserviceTypesV1InsightFeedbackMetadata**](TableauPulseInsightsserviceTypesV1InsightFeedbackMetadata.md) |  | [optional] 
**table** | [**TableauPulseInsightsserviceV1Table**](TableauPulseInsightsserviceV1Table.md) |  | [optional] 
**generation_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_insightsservice_v1_insight import TableauPulseInsightsserviceV1Insight

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseInsightsserviceV1Insight from a JSON string
tableau_pulse_insightsservice_v1_insight_instance = TableauPulseInsightsserviceV1Insight.from_json(json)
# print the JSON string representation of the object
print(TableauPulseInsightsserviceV1Insight.to_json())

# convert the object into a dict
tableau_pulse_insightsservice_v1_insight_dict = tableau_pulse_insightsservice_v1_insight_instance.to_dict()
# create an instance of TableauPulseInsightsserviceV1Insight from a dict
tableau_pulse_insightsservice_v1_insight_from_dict = TableauPulseInsightsserviceV1Insight.from_dict(tableau_pulse_insightsservice_v1_insight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


