# TableauAnalyticsextensionsV1ConnectionBrief


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_name** | **str** | Required. The title of the connection. | [optional] 
**connection_type** | **str** | Required. The kind of service responding to analytics extension requests. The value can be: TABPY, for a [Tableau TabPy](https://github.com/tableau/TabPy) server; GENERIC_API for your custom service that complies with the [Analytics Extensions API spec](https://tableau.github.io/analytics-extensions-api/docs/ae_intro.html); or RSERVE, for an [Rserve](https://www.tableau.com/solutions/r) service; or EINSTEIN_DISCOVERY for your instance of [Einstein Discovery](https://help.tableau.com/current/server-linux/en-us/config_r_tabpy.htm). | [optional] 

## Example

```python
from openapi_client.models.tableau_analyticsextensions_v1_connection_brief import TableauAnalyticsextensionsV1ConnectionBrief

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAnalyticsextensionsV1ConnectionBrief from a JSON string
tableau_analyticsextensions_v1_connection_brief_instance = TableauAnalyticsextensionsV1ConnectionBrief.from_json(json)
# print the JSON string representation of the object
print(TableauAnalyticsextensionsV1ConnectionBrief.to_json())

# convert the object into a dict
tableau_analyticsextensions_v1_connection_brief_dict = tableau_analyticsextensions_v1_connection_brief_instance.to_dict()
# create an instance of TableauAnalyticsextensionsV1ConnectionBrief from a dict
tableau_analyticsextensions_v1_connection_brief_from_dict = TableauAnalyticsextensionsV1ConnectionBrief.from_dict(tableau_analyticsextensions_v1_connection_brief_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


