# TableauPermissionserviceV1MemberError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** |  | [optional] 
**member_entity_type** | **str** |  | [optional] 
**error_id** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_permissionservice_v1_member_error import TableauPermissionserviceV1MemberError

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPermissionserviceV1MemberError from a JSON string
tableau_permissionservice_v1_member_error_instance = TableauPermissionserviceV1MemberError.from_json(json)
# print the JSON string representation of the object
print(TableauPermissionserviceV1MemberError.to_json())

# convert the object into a dict
tableau_permissionservice_v1_member_error_dict = tableau_permissionservice_v1_member_error_instance.to_dict()
# create an instance of TableauPermissionserviceV1MemberError from a dict
tableau_permissionservice_v1_member_error_from_dict = TableauPermissionserviceV1MemberError.from_dict(tableau_permissionservice_v1_member_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


