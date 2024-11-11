# TableauPulseInsightsserviceV1GenerateInsightBundleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  | [optional] 
**options** | [**TableauPulseInsightsserviceV1InsightBundleOptions**](TableauPulseInsightsserviceV1InsightBundleOptions.md) |  | [optional] 
**input** | [**TableauPulseInsightsserviceV1InsightBundleInput**](TableauPulseInsightsserviceV1InsightBundleInput.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_insightsservice_v1_generate_insight_bundle_request import TableauPulseInsightsserviceV1GenerateInsightBundleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseInsightsserviceV1GenerateInsightBundleRequest from a JSON string
tableau_pulse_insightsservice_v1_generate_insight_bundle_request_instance = TableauPulseInsightsserviceV1GenerateInsightBundleRequest.from_json(json)
# print the JSON string representation of the object
print(TableauPulseInsightsserviceV1GenerateInsightBundleRequest.to_json())

# convert the object into a dict
tableau_pulse_insightsservice_v1_generate_insight_bundle_request_dict = tableau_pulse_insightsservice_v1_generate_insight_bundle_request_instance.to_dict()
# create an instance of TableauPulseInsightsserviceV1GenerateInsightBundleRequest from a dict
tableau_pulse_insightsservice_v1_generate_insight_bundle_request_from_dict = TableauPulseInsightsserviceV1GenerateInsightBundleRequest.from_dict(tableau_pulse_insightsservice_v1_generate_insight_bundle_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


