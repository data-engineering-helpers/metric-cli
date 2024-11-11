# TableauUsagestatsV1UsageStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hits_total** | **int** | The number of times the content item has been marked as used. | [optional] 
**hits_last_two_weeks_total** | **int** | The number of times the content item has been marked as used in the last two weeks. | [optional] 
**hits_last_one_month_total** | **int** | The number of times the content item has been marked as used in the last month. | [optional] 
**hits_last_three_months_total** | **int** | The number of times the content item has been marked as used in the last three months. | [optional] 
**hits_last_twelve_months_total** | **int** | The number of times the content item has been marked as used in the last tweleve months. | [optional] 

## Example

```python
from openapi_client.models.tableau_usagestats_v1_usage_stats import TableauUsagestatsV1UsageStats

# TODO update the JSON string below
json = "{}"
# create an instance of TableauUsagestatsV1UsageStats from a JSON string
tableau_usagestats_v1_usage_stats_instance = TableauUsagestatsV1UsageStats.from_json(json)
# print the JSON string representation of the object
print(TableauUsagestatsV1UsageStats.to_json())

# convert the object into a dict
tableau_usagestats_v1_usage_stats_dict = tableau_usagestats_v1_usage_stats_instance.to_dict()
# create an instance of TableauUsagestatsV1UsageStats from a dict
tableau_usagestats_v1_usage_stats_from_dict = TableauUsagestatsV1UsageStats.from_dict(tableau_usagestats_v1_usage_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


