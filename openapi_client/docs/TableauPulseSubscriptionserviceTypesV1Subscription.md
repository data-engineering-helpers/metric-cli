# TableauPulseSubscriptionserviceTypesV1Subscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**metric_id** | **str** |  | [optional] 
**follower** | [**TableauPulseSubscriptionserviceTypesV1Follower**](TableauPulseSubscriptionserviceTypesV1Follower.md) |  | [optional] 
**create_time** | **str** |  | [optional] 
**update_time** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_subscriptionservice_types_v1_subscription import TableauPulseSubscriptionserviceTypesV1Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseSubscriptionserviceTypesV1Subscription from a JSON string
tableau_pulse_subscriptionservice_types_v1_subscription_instance = TableauPulseSubscriptionserviceTypesV1Subscription.from_json(json)
# print the JSON string representation of the object
print(TableauPulseSubscriptionserviceTypesV1Subscription.to_json())

# convert the object into a dict
tableau_pulse_subscriptionservice_types_v1_subscription_dict = tableau_pulse_subscriptionservice_types_v1_subscription_instance.to_dict()
# create an instance of TableauPulseSubscriptionserviceTypesV1Subscription from a dict
tableau_pulse_subscriptionservice_types_v1_subscription_from_dict = TableauPulseSubscriptionserviceTypesV1Subscription.from_dict(tableau_pulse_subscriptionservice_types_v1_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


