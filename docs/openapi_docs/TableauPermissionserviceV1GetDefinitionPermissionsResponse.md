# TableauPermissionserviceV1GetDefinitionPermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition_id** | **str** |  | [optional] 
**member_permissions** | [**List[TableauPermissionserviceV1MemberPermission]**](TableauPermissionserviceV1MemberPermission.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_permissionservice_v1_get_definition_permissions_response import TableauPermissionserviceV1GetDefinitionPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPermissionserviceV1GetDefinitionPermissionsResponse from a JSON string
tableau_permissionservice_v1_get_definition_permissions_response_instance = TableauPermissionserviceV1GetDefinitionPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauPermissionserviceV1GetDefinitionPermissionsResponse.to_json())

# convert the object into a dict
tableau_permissionservice_v1_get_definition_permissions_response_dict = tableau_permissionservice_v1_get_definition_permissions_response_instance.to_dict()
# create an instance of TableauPermissionserviceV1GetDefinitionPermissionsResponse from a dict
tableau_permissionservice_v1_get_definition_permissions_response_from_dict = TableauPermissionserviceV1GetDefinitionPermissionsResponse.from_dict(tableau_permissionservice_v1_get_definition_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


