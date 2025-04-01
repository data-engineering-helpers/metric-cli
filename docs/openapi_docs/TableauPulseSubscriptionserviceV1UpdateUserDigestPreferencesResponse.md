# TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_preferences** | [**List[TableauPulseSubscriptionserviceTypesV1ChannelPreferences]**](TableauPulseSubscriptionserviceTypesV1ChannelPreferences.md) |  | [optional] 
**cadence** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_response import TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesResponse from a JSON string
tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_response_instance = TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesResponse.from_json(json)
# print the JSON string representation of the object
print(TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesResponse.to_json())

# convert the object into a dict
tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_response_dict = tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_response_instance.to_dict()
# create an instance of TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesResponse from a dict
tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_response_from_dict = TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesResponse.from_dict(tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


