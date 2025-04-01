# TableauMetricqueryserviceV1GetEntitlementsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlements** | [**List[TableauMetricqueryserviceTypesV1Entitlement]**](TableauMetricqueryserviceTypesV1Entitlement.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_v1_get_entitlements_response import TableauMetricqueryserviceV1GetEntitlementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceV1GetEntitlementsResponse from a JSON string
tableau_metricqueryservice_v1_get_entitlements_response_instance = TableauMetricqueryserviceV1GetEntitlementsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceV1GetEntitlementsResponse.to_json())

# convert the object into a dict
tableau_metricqueryservice_v1_get_entitlements_response_dict = tableau_metricqueryservice_v1_get_entitlements_response_instance.to_dict()
# create an instance of TableauMetricqueryserviceV1GetEntitlementsResponse from a dict
tableau_metricqueryservice_v1_get_entitlements_response_from_dict = TableauMetricqueryserviceV1GetEntitlementsResponse.from_dict(tableau_metricqueryservice_v1_get_entitlements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


