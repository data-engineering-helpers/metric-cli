# TableauPulseSubscriptionserviceV1GetUserDigestPreferencesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cadence** | **str** |  | [optional] 
**channel_preferences** | [**List[TableauPulseSubscriptionserviceTypesV1ChannelPreferences]**](TableauPulseSubscriptionserviceTypesV1ChannelPreferences.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_subscriptionservice_v1_get_user_digest_preferences_response import TableauPulseSubscriptionserviceV1GetUserDigestPreferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseSubscriptionserviceV1GetUserDigestPreferencesResponse from a JSON string
tableau_pulse_subscriptionservice_v1_get_user_digest_preferences_response_instance = TableauPulseSubscriptionserviceV1GetUserDigestPreferencesResponse.from_json(json)
# print the JSON string representation of the object
print(TableauPulseSubscriptionserviceV1GetUserDigestPreferencesResponse.to_json())

# convert the object into a dict
tableau_pulse_subscriptionservice_v1_get_user_digest_preferences_response_dict = tableau_pulse_subscriptionservice_v1_get_user_digest_preferences_response_instance.to_dict()
# create an instance of TableauPulseSubscriptionserviceV1GetUserDigestPreferencesResponse from a dict
tableau_pulse_subscriptionservice_v1_get_user_digest_preferences_response_from_dict = TableauPulseSubscriptionserviceV1GetUserDigestPreferencesResponse.from_dict(tableau_pulse_subscriptionservice_v1_get_user_digest_preferences_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


