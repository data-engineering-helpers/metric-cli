# TableauAuthnV1OidcConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Required. Provider client ID that the IdP has assigned to Tableau Server. | [optional] 
**client_secret** | **str** | Required. Provider client secret. This is a token that is used by Tableau Server to verify the authenticity of the response from the IdP. This value should be kept securely. | [optional] 
**config_url** | **str** | Required. Provider configuration URL. Specifies the location of the provider configuration discovery document that contains the OpenID provider metadata. | [optional] 
**custom_scope** | **str** | Custom scope user-related value to query the IdP. | [optional] 
**id_claim** | **str** | Required. Claim for retrieving user ID from the OIDC token. Default value is &#39;sub&#39;. | [optional] 
**username_claim** | **str** | Required. Claim for retrieving username from the OIDC token. Default value is &#39;email&#39;. | [optional] 
**client_authentication** | **str** | Required. Token endpoint authentication method. Default value is &#39;CLIENT_SECRET_BASIC&#39;. | [optional] 
**essential_acr_values** | **str** | List of essential Authentication Context Reference Class values used for authentication. | [optional] 
**voluntary_acr_values** | **str** | List of voluntary Authentication Context Reference Class values used for authentication. | [optional] 
**prompt** | **str** | Prompts the user for re-authentication and consent. | [optional] 
**connection_timeout** | **int** | Wait time (in seconds) for connecting to the IdP. | [optional] 
**read_timeout** | **int** | Wait time (in seconds) for data from the IdP. | [optional] 
**ignore_domain** | **bool** | Set value to &#39;true&#39; only if the following are true: you are using email addresses as usernames in Tableau Server, you have provisioned users in the IdP with multiple domains, and you want to ignore the domain name portion of the email claim from the IdP. Default value is &#39;false&#39;. | [optional] 
**ignore_jwk** | **bool** | Set value to &#39;true&#39; if the IdP does not support JWK validation. Default value is &#39;false&#39;. | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_oidc_config import TableauAuthnV1OidcConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1OidcConfig from a JSON string
tableau_authn_v1_oidc_config_instance = TableauAuthnV1OidcConfig.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1OidcConfig.to_json())

# convert the object into a dict
tableau_authn_v1_oidc_config_dict = tableau_authn_v1_oidc_config_instance.to_dict()
# create an instance of TableauAuthnV1OidcConfig from a dict
tableau_authn_v1_oidc_config_from_dict = TableauAuthnV1OidcConfig.from_dict(tableau_authn_v1_oidc_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


