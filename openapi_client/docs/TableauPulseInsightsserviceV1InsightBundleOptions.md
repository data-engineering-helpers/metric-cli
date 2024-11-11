# TableauPulseInsightsserviceV1InsightBundleOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output_format** | **str** |  | [optional] 
**now** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**score_weights** | [**TableauPulseInsightsserviceV1ScoreWeights**](TableauPulseInsightsserviceV1ScoreWeights.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_insightsservice_v1_insight_bundle_options import TableauPulseInsightsserviceV1InsightBundleOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseInsightsserviceV1InsightBundleOptions from a JSON string
tableau_pulse_insightsservice_v1_insight_bundle_options_instance = TableauPulseInsightsserviceV1InsightBundleOptions.from_json(json)
# print the JSON string representation of the object
print(TableauPulseInsightsserviceV1InsightBundleOptions.to_json())

# convert the object into a dict
tableau_pulse_insightsservice_v1_insight_bundle_options_dict = tableau_pulse_insightsservice_v1_insight_bundle_options_instance.to_dict()
# create an instance of TableauPulseInsightsserviceV1InsightBundleOptions from a dict
tableau_pulse_insightsservice_v1_insight_bundle_options_from_dict = TableauPulseInsightsserviceV1InsightBundleOptions.from_dict(tableau_pulse_insightsservice_v1_insight_bundle_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


