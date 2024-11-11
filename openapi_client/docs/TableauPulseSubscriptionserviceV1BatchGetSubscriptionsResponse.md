# TableauPulseSubscriptionserviceV1BatchGetSubscriptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriptions** | [**List[TableauPulseSubscriptionserviceTypesV1Subscription]**](TableauPulseSubscriptionserviceTypesV1Subscription.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_subscriptionservice_v1_batch_get_subscriptions_response import TableauPulseSubscriptionserviceV1BatchGetSubscriptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseSubscriptionserviceV1BatchGetSubscriptionsResponse from a JSON string
tableau_pulse_subscriptionservice_v1_batch_get_subscriptions_response_instance = TableauPulseSubscriptionserviceV1BatchGetSubscriptionsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauPulseSubscriptionserviceV1BatchGetSubscriptionsResponse.to_json())

# convert the object into a dict
tableau_pulse_subscriptionservice_v1_batch_get_subscriptions_response_dict = tableau_pulse_subscriptionservice_v1_batch_get_subscriptions_response_instance.to_dict()
# create an instance of TableauPulseSubscriptionserviceV1BatchGetSubscriptionsResponse from a dict
tableau_pulse_subscriptionservice_v1_batch_get_subscriptions_response_from_dict = TableauPulseSubscriptionserviceV1BatchGetSubscriptionsResponse.from_dict(tableau_pulse_subscriptionservice_v1_batch_get_subscriptions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


