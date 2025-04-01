# TableauPulseInsightsserviceV1InputMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition** | [**TableauMetricqueryserviceTypesV1DefinitionSpecification**](TableauMetricqueryserviceTypesV1DefinitionSpecification.md) |  | [optional] 
**metric_specification** | [**TableauMetricqueryserviceTypesV1MetricSpecification**](TableauMetricqueryserviceTypesV1MetricSpecification.md) |  | [optional] 
**extension_options** | [**TableauMetricqueryserviceTypesV1ExtensionOptions**](TableauMetricqueryserviceTypesV1ExtensionOptions.md) |  | [optional] 
**representation_options** | [**TableauMetricqueryserviceTypesV1RepresentationOptions**](TableauMetricqueryserviceTypesV1RepresentationOptions.md) |  | [optional] 
**insights_options** | [**TableauMetricqueryserviceTypesV1InsightsOptions**](TableauMetricqueryserviceTypesV1InsightsOptions.md) |  | [optional] 
**goals** | [**TableauPulseInsightsserviceV1Goals**](TableauPulseInsightsserviceV1Goals.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_insightsservice_v1_input_metric import TableauPulseInsightsserviceV1InputMetric

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseInsightsserviceV1InputMetric from a JSON string
tableau_pulse_insightsservice_v1_input_metric_instance = TableauPulseInsightsserviceV1InputMetric.from_json(json)
# print the JSON string representation of the object
print(TableauPulseInsightsserviceV1InputMetric.to_json())

# convert the object into a dict
tableau_pulse_insightsservice_v1_input_metric_dict = tableau_pulse_insightsservice_v1_input_metric_instance.to_dict()
# create an instance of TableauPulseInsightsserviceV1InputMetric from a dict
tableau_pulse_insightsservice_v1_input_metric_from_dict = TableauPulseInsightsserviceV1InputMetric.from_dict(tableau_pulse_insightsservice_v1_input_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


