# TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_id** | **str** |  | [optional] 
**followers** | [**List[TableauPulseSubscriptionserviceTypesV1Follower]**](TableauPulseSubscriptionserviceTypesV1Follower.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_request import TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsRequest from a JSON string
tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_request_instance = TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsRequest.from_json(json)
# print the JSON string representation of the object
print(TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsRequest.to_json())

# convert the object into a dict
tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_request_dict = tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_request_instance.to_dict()
# create an instance of TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsRequest from a dict
tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_request_from_dict = TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsRequest.from_dict(tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


