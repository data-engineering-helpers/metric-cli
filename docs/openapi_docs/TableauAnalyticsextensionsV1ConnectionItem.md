# TableauAnalyticsextensionsV1ConnectionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Required. The location of an external service (TabPy, Rserve, Einstein_Discovery, Generic API, or other) that responds to your analytics extension requests. The case sensitive value must be a URI, IPv4 or IPv6 address that is a maximum of 255 Unicode characters. Starting in v2022.1, a host address can include path information (&#x60;www.example.com/path&#x60;), where previous versions supported only the root domain name (&#x60;www.example.com&#x60;).  | [optional] 
**port** | **int** | Required. Integer between 1 and 65535. | [optional] 
**is_auth_enabled** | **bool** | For Tableau Online: The value is always true. For on premise Tableau servers: Optional. Set to true if authentication is enabled on the external service. If true, username and password are required. Default is false. | [optional] 
**username** | **str** | For Tableau Online: A username is always required. | [optional] 
**password** | **str** | For Tableau Online: A password is always required. | [optional] 
**is_ssl_enabled** | **bool** | For Tableau Online: The value is always true. For on premise Tableau servers: Optional. Set true if SSL is enabled on the external service. If true, the host address must use HTTPS. Default is false. | [optional] 
**connection_brief** | [**TableauAnalyticsextensionsV1ConnectionBrief**](TableauAnalyticsextensionsV1ConnectionBrief.md) |  | [optional] 
**connection_luid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_analyticsextensions_v1_connection_item import TableauAnalyticsextensionsV1ConnectionItem

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAnalyticsextensionsV1ConnectionItem from a JSON string
tableau_analyticsextensions_v1_connection_item_instance = TableauAnalyticsextensionsV1ConnectionItem.from_json(json)
# print the JSON string representation of the object
print(TableauAnalyticsextensionsV1ConnectionItem.to_json())

# convert the object into a dict
tableau_analyticsextensions_v1_connection_item_dict = tableau_analyticsextensions_v1_connection_item_instance.to_dict()
# create an instance of TableauAnalyticsextensionsV1ConnectionItem from a dict
tableau_analyticsextensions_v1_connection_item_from_dict = TableauAnalyticsextensionsV1ConnectionItem.from_dict(tableau_analyticsextensions_v1_connection_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


