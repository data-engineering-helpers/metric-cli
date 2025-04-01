# TableauPulseInsightsserviceV1Table


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[TableauPulseInsightsserviceV1ColumnInfo]**](TableauPulseInsightsserviceV1ColumnInfo.md) |  | [optional] 
**rows** | [**List[TableauPulseInsightsserviceV1Row]**](TableauPulseInsightsserviceV1Row.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_insightsservice_v1_table import TableauPulseInsightsserviceV1Table

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseInsightsserviceV1Table from a JSON string
tableau_pulse_insightsservice_v1_table_instance = TableauPulseInsightsserviceV1Table.from_json(json)
# print the JSON string representation of the object
print(TableauPulseInsightsserviceV1Table.to_json())

# convert the object into a dict
tableau_pulse_insightsservice_v1_table_dict = tableau_pulse_insightsservice_v1_table_instance.to_dict()
# create an instance of TableauPulseInsightsserviceV1Table from a dict
tableau_pulse_insightsservice_v1_table_from_dict = TableauPulseInsightsserviceV1Table.from_dict(tableau_pulse_insightsservice_v1_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


