# TableauPulseSubscriptionserviceV1ListSubscriptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriptions** | [**List[TableauPulseSubscriptionserviceTypesV1Subscription]**](TableauPulseSubscriptionserviceTypesV1Subscription.md) |  | [optional] 
**next_page_token** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_subscriptionservice_v1_list_subscriptions_response import TableauPulseSubscriptionserviceV1ListSubscriptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseSubscriptionserviceV1ListSubscriptionsResponse from a JSON string
tableau_pulse_subscriptionservice_v1_list_subscriptions_response_instance = TableauPulseSubscriptionserviceV1ListSubscriptionsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauPulseSubscriptionserviceV1ListSubscriptionsResponse.to_json())

# convert the object into a dict
tableau_pulse_subscriptionservice_v1_list_subscriptions_response_dict = tableau_pulse_subscriptionservice_v1_list_subscriptions_response_instance.to_dict()
# create an instance of TableauPulseSubscriptionserviceV1ListSubscriptionsResponse from a dict
tableau_pulse_subscriptionservice_v1_list_subscriptions_response_from_dict = TableauPulseSubscriptionserviceV1ListSubscriptionsResponse.from_dict(tableau_pulse_subscriptionservice_v1_list_subscriptions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


