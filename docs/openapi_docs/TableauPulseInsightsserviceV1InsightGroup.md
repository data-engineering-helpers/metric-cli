# TableauPulseInsightsserviceV1InsightGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**insights** | [**List[TableauPulseInsightsserviceV1InsightResponse]**](TableauPulseInsightsserviceV1InsightResponse.md) |  | [optional] 
**summaries** | [**List[TableauPulseInsightsserviceV1SummaryResponse]**](TableauPulseInsightsserviceV1SummaryResponse.md) |  | [optional] 
**error** | [**TableauPulseInsightsserviceV1Error**](TableauPulseInsightsserviceV1Error.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_insightsservice_v1_insight_group import TableauPulseInsightsserviceV1InsightGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseInsightsserviceV1InsightGroup from a JSON string
tableau_pulse_insightsservice_v1_insight_group_instance = TableauPulseInsightsserviceV1InsightGroup.from_json(json)
# print the JSON string representation of the object
print(TableauPulseInsightsserviceV1InsightGroup.to_json())

# convert the object into a dict
tableau_pulse_insightsservice_v1_insight_group_dict = tableau_pulse_insightsservice_v1_insight_group_instance.to_dict()
# create an instance of TableauPulseInsightsserviceV1InsightGroup from a dict
tableau_pulse_insightsservice_v1_insight_group_from_dict = TableauPulseInsightsserviceV1InsightGroup.from_dict(tableau_pulse_insightsservice_v1_insight_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


