# TableauPulseInsightsserviceV1InsightBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insight_groups** | [**List[TableauPulseInsightsserviceV1InsightGroup]**](TableauPulseInsightsserviceV1InsightGroup.md) |  | [optional] 
**has_errors** | **bool** |  | [optional] 
**characterization** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_insightsservice_v1_insight_bundle import TableauPulseInsightsserviceV1InsightBundle

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseInsightsserviceV1InsightBundle from a JSON string
tableau_pulse_insightsservice_v1_insight_bundle_instance = TableauPulseInsightsserviceV1InsightBundle.from_json(json)
# print the JSON string representation of the object
print(TableauPulseInsightsserviceV1InsightBundle.to_json())

# convert the object into a dict
tableau_pulse_insightsservice_v1_insight_bundle_dict = tableau_pulse_insightsservice_v1_insight_bundle_instance.to_dict()
# create an instance of TableauPulseInsightsserviceV1InsightBundle from a dict
tableau_pulse_insightsservice_v1_insight_bundle_from_dict = TableauPulseInsightsserviceV1InsightBundle.from_dict(tableau_pulse_insightsservice_v1_insight_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


