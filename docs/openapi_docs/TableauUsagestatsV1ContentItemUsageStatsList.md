# TableauUsagestatsV1ContentItemUsageStatsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_items** | [**List[TableauUsagestatsV1ContentItemUsageStats]**](TableauUsagestatsV1ContentItemUsageStats.md) |  | [optional] 
**errors** | [**List[TableauUsagestatsV1ErrorInfo]**](TableauUsagestatsV1ErrorInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_usagestats_v1_content_item_usage_stats_list import TableauUsagestatsV1ContentItemUsageStatsList

# TODO update the JSON string below
json = "{}"
# create an instance of TableauUsagestatsV1ContentItemUsageStatsList from a JSON string
tableau_usagestats_v1_content_item_usage_stats_list_instance = TableauUsagestatsV1ContentItemUsageStatsList.from_json(json)
# print the JSON string representation of the object
print(TableauUsagestatsV1ContentItemUsageStatsList.to_json())

# convert the object into a dict
tableau_usagestats_v1_content_item_usage_stats_list_dict = tableau_usagestats_v1_content_item_usage_stats_list_instance.to_dict()
# create an instance of TableauUsagestatsV1ContentItemUsageStatsList from a dict
tableau_usagestats_v1_content_item_usage_stats_list_from_dict = TableauUsagestatsV1ContentItemUsageStatsList.from_dict(tableau_usagestats_v1_content_item_usage_stats_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


