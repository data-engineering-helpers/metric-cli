# TableauPulseInsightsserviceV1GenerateInsightBundleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**TableauPulseInsightsserviceV1InsightBundle**](TableauPulseInsightsserviceV1InsightBundle.md) |  | [optional] 
**error** | [**TableauPulseInsightsserviceV1Error**](TableauPulseInsightsserviceV1Error.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_insightsservice_v1_generate_insight_bundle_response import TableauPulseInsightsserviceV1GenerateInsightBundleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseInsightsserviceV1GenerateInsightBundleResponse from a JSON string
tableau_pulse_insightsservice_v1_generate_insight_bundle_response_instance = TableauPulseInsightsserviceV1GenerateInsightBundleResponse.from_json(json)
# print the JSON string representation of the object
print(TableauPulseInsightsserviceV1GenerateInsightBundleResponse.to_json())

# convert the object into a dict
tableau_pulse_insightsservice_v1_generate_insight_bundle_response_dict = tableau_pulse_insightsservice_v1_generate_insight_bundle_response_instance.to_dict()
# create an instance of TableauPulseInsightsserviceV1GenerateInsightBundleResponse from a dict
tableau_pulse_insightsservice_v1_generate_insight_bundle_response_from_dict = TableauPulseInsightsserviceV1GenerateInsightBundleResponse.from_dict(tableau_pulse_insightsservice_v1_generate_insight_bundle_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


