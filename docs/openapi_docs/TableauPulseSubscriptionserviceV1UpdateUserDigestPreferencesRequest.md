# TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_preferences_request** | [**List[TableauPulseSubscriptionserviceTypesV1ChannelPreferencesRequest]**](TableauPulseSubscriptionserviceTypesV1ChannelPreferencesRequest.md) |  | [optional] 
**cadence** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_request import TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesRequest from a JSON string
tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_request_instance = TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesRequest.from_json(json)
# print the JSON string representation of the object
print(TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesRequest.to_json())

# convert the object into a dict
tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_request_dict = tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_request_instance.to_dict()
# create an instance of TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesRequest from a dict
tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_request_from_dict = TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesRequest.from_dict(tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


