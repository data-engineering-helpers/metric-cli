# TableauUsagestatsV1ContentItemUsageStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**TableauUsagestatsV1ContentItemId**](TableauUsagestatsV1ContentItemId.md) |  | [optional] 
**usage** | [**TableauUsagestatsV1UsageStats**](TableauUsagestatsV1UsageStats.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_usagestats_v1_content_item_usage_stats import TableauUsagestatsV1ContentItemUsageStats

# TODO update the JSON string below
json = "{}"
# create an instance of TableauUsagestatsV1ContentItemUsageStats from a JSON string
tableau_usagestats_v1_content_item_usage_stats_instance = TableauUsagestatsV1ContentItemUsageStats.from_json(json)
# print the JSON string representation of the object
print(TableauUsagestatsV1ContentItemUsageStats.to_json())

# convert the object into a dict
tableau_usagestats_v1_content_item_usage_stats_dict = tableau_usagestats_v1_content_item_usage_stats_instance.to_dict()
# create an instance of TableauUsagestatsV1ContentItemUsageStats from a dict
tableau_usagestats_v1_content_item_usage_stats_from_dict = TableauUsagestatsV1ContentItemUsageStats.from_dict(tableau_usagestats_v1_content_item_usage_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


