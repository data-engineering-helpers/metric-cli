# TableauMetricqueryserviceTypesV1InsightsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show_insights** | **bool** |  | [optional] 
**settings** | [**List[TableauMetricqueryserviceTypesV1InsightsOptionsInsightSetting]**](TableauMetricqueryserviceTypesV1InsightsOptionsInsightSetting.md) |  | [optional] 
**nested_insight_setting** | [**TableauMetricqueryserviceTypesV1InsightsOptionsInsightSetting**](.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_metricqueryservice_types_v1_insights_options import TableauMetricqueryserviceTypesV1InsightsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TableauMetricqueryserviceTypesV1InsightsOptions from a JSON string
tableau_metricqueryservice_types_v1_insights_options_instance = TableauMetricqueryserviceTypesV1InsightsOptions.from_json(json)
# print the JSON string representation of the object
print(TableauMetricqueryserviceTypesV1InsightsOptions.to_json())

# convert the object into a dict
tableau_metricqueryservice_types_v1_insights_options_dict = tableau_metricqueryservice_types_v1_insights_options_instance.to_dict()
# create an instance of TableauMetricqueryserviceTypesV1InsightsOptions from a dict
tableau_metricqueryservice_types_v1_insights_options_from_dict = TableauMetricqueryserviceTypesV1InsightsOptions.from_dict(tableau_metricqueryservice_types_v1_insights_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


