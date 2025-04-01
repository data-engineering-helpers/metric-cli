# TableauPulseSubscriptionserviceV1ListFollowedMetricsGroupsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_groups** | [**List[TableauMetricqueryserviceTypesV1MetricGroup]**](TableauMetricqueryserviceTypesV1MetricGroup.md) |  | [optional] 
**group_by** | **str** |  | [optional] 
**sort_order** | **str** |  | [optional] 
**errors** | [**List[TableauMetricqueryserviceTypesV1BatchGetMetricErrors]**](TableauMetricqueryserviceTypesV1BatchGetMetricErrors.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_subscriptionservice_v1_list_followed_metrics_groups_response import TableauPulseSubscriptionserviceV1ListFollowedMetricsGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseSubscriptionserviceV1ListFollowedMetricsGroupsResponse from a JSON string
tableau_pulse_subscriptionservice_v1_list_followed_metrics_groups_response_instance = TableauPulseSubscriptionserviceV1ListFollowedMetricsGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauPulseSubscriptionserviceV1ListFollowedMetricsGroupsResponse.to_json())

# convert the object into a dict
tableau_pulse_subscriptionservice_v1_list_followed_metrics_groups_response_dict = tableau_pulse_subscriptionservice_v1_list_followed_metrics_groups_response_instance.to_dict()
# create an instance of TableauPulseSubscriptionserviceV1ListFollowedMetricsGroupsResponse from a dict
tableau_pulse_subscriptionservice_v1_list_followed_metrics_groups_response_from_dict = TableauPulseSubscriptionserviceV1ListFollowedMetricsGroupsResponse.from_dict(tableau_pulse_subscriptionservice_v1_list_followed_metrics_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


