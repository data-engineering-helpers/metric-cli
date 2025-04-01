# TableauPulseInsightsserviceV1InsightBundleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**TableauPulseInsightsserviceV1MetricMetadata**](TableauPulseInsightsserviceV1MetricMetadata.md) |  | [optional] 
**metric** | [**TableauPulseInsightsserviceV1InputMetric**](TableauPulseInsightsserviceV1InputMetric.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_insightsservice_v1_insight_bundle_input import TableauPulseInsightsserviceV1InsightBundleInput

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseInsightsserviceV1InsightBundleInput from a JSON string
tableau_pulse_insightsservice_v1_insight_bundle_input_instance = TableauPulseInsightsserviceV1InsightBundleInput.from_json(json)
# print the JSON string representation of the object
print(TableauPulseInsightsserviceV1InsightBundleInput.to_json())

# convert the object into a dict
tableau_pulse_insightsservice_v1_insight_bundle_input_dict = tableau_pulse_insightsservice_v1_insight_bundle_input_instance.to_dict()
# create an instance of TableauPulseInsightsserviceV1InsightBundleInput from a dict
tableau_pulse_insightsservice_v1_insight_bundle_input_from_dict = TableauPulseInsightsserviceV1InsightBundleInput.from_dict(tableau_pulse_insightsservice_v1_insight_bundle_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


