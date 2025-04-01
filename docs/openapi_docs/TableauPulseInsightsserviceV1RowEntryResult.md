# TableauPulseInsightsserviceV1RowEntryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**TableauPulseInsightsserviceV1RowEntry**](TableauPulseInsightsserviceV1RowEntry.md) |  | [optional] 
**error** | [**TableauPulseInsightsserviceV1Error**](TableauPulseInsightsserviceV1Error.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_pulse_insightsservice_v1_row_entry_result import TableauPulseInsightsserviceV1RowEntryResult

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPulseInsightsserviceV1RowEntryResult from a JSON string
tableau_pulse_insightsservice_v1_row_entry_result_instance = TableauPulseInsightsserviceV1RowEntryResult.from_json(json)
# print the JSON string representation of the object
print(TableauPulseInsightsserviceV1RowEntryResult.to_json())

# convert the object into a dict
tableau_pulse_insightsservice_v1_row_entry_result_dict = tableau_pulse_insightsservice_v1_row_entry_result_instance.to_dict()
# create an instance of TableauPulseInsightsserviceV1RowEntryResult from a dict
tableau_pulse_insightsservice_v1_row_entry_result_from_dict = TableauPulseInsightsserviceV1RowEntryResult.from_dict(tableau_pulse_insightsservice_v1_row_entry_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


