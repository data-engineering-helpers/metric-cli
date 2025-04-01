# TableauMetricqueryserviceV1CreateDefinitionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**specification** | [**TableauMetricqueryserviceTypesV1DefinitionSpecification**](TableauMetricqueryserviceTypesV1DefinitionSpecification.md) |  | [optional] 
**extension_options** | [**TableauMetricqueryserviceTypesV1ExtensionOptions**](TableauMetricqueryserviceTypesV1ExtensionOptions.md) |  | [optional] 
**representation_options** | [**TableauMetricqueryserviceTypesV1RepresentationOptions**](TableauMetricqueryserviceTypesV1RepresentationOptions.md) |  | [optional] 
**insights_options** | [**TableauMetricqueryserviceTypesV1InsightsOptions**](TableauMetricqueryserviceTypesV1InsightsOptions.md) |  | [optional] 
**user_link** | **str** |  | [optional] 
**user_link_name** | **str** |  | [optional] 
**comparisons** | [**TableauMetricqueryserviceTypesV1Comparisons**](TableauMetricqueryserviceTypesV1Comparisons.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_v1_create_definition_request import TableauMetricqueryserviceV1CreateDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceV1CreateDefinitionRequest from a JSON string
tableau_metricqueryservice_v1_create_definition_request_instance = TableauMetricqueryserviceV1CreateDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceV1CreateDefinitionRequest.to_json())

# convert the object into a dict
tableau_metricqueryservice_v1_create_definition_request_dict = tableau_metricqueryservice_v1_create_definition_request_instance.to_dict()
# create an instance of TableauMetricqueryserviceV1CreateDefinitionRequest from a dict
tableau_metricqueryservice_v1_create_definition_request_from_dict = TableauMetricqueryserviceV1CreateDefinitionRequest.from_dict(tableau_metricqueryservice_v1_create_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


