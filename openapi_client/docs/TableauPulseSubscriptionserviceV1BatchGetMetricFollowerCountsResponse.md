# TableauPulseSubscriptionserviceV1BatchGetMetricFollowerCountsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**follower_counts** | [**List[TableauPulseSubscriptionserviceTypesV1MetricFollowerCount]**](TableauPulseSubscriptionserviceTypesV1MetricFollowerCount.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_subscriptionservice_v1_batch_get_metric_follower_counts_response import TableauPulseSubscriptionserviceV1BatchGetMetricFollowerCountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseSubscriptionserviceV1BatchGetMetricFollowerCountsResponse from a JSON string
tableau_pulse_subscriptionservice_v1_batch_get_metric_follower_counts_response_instance = TableauPulseSubscriptionserviceV1BatchGetMetricFollowerCountsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauPulseSubscriptionserviceV1BatchGetMetricFollowerCountsResponse.to_json())

# convert the object into a dict
tableau_pulse_subscriptionservice_v1_batch_get_metric_follower_counts_response_dict = tableau_pulse_subscriptionservice_v1_batch_get_metric_follower_counts_response_instance.to_dict()
# create an instance of TableauPulseSubscriptionserviceV1BatchGetMetricFollowerCountsResponse from a dict
tableau_pulse_subscriptionservice_v1_batch_get_metric_follower_counts_response_from_dict = TableauPulseSubscriptionserviceV1BatchGetMetricFollowerCountsResponse.from_dict(tableau_pulse_subscriptionservice_v1_batch_get_metric_follower_counts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


