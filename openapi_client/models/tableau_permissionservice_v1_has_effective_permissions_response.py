# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.tableau_permissionservice_v1_permission_state import TableauPermissionserviceV1PermissionState
from typing import Optional, Set
from typing_extensions import Self

class TableauPermissionserviceV1HasEffectivePermissionsResponse(BaseModel):
    """
    TableauPermissionserviceV1HasEffectivePermissionsResponse
    """ # noqa: E501
    definition_id: Optional[StrictStr] = None
    effective_permission_states: Optional[List[TableauPermissionserviceV1PermissionState]] = None
    __properties: ClassVar[List[str]] = ["definition_id", "effective_permission_states"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TableauPermissionserviceV1HasEffectivePermissionsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in effective_permission_states (list)
        _items = []
        if self.effective_permission_states:
            for _item_effective_permission_states in self.effective_permission_states:
                if _item_effective_permission_states:
                    _items.append(_item_effective_permission_states.to_dict())
            _dict['effective_permission_states'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TableauPermissionserviceV1HasEffectivePermissionsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "definition_id": obj.get("definition_id"),
            "effective_permission_states": [TableauPermissionserviceV1PermissionState.from_dict(_item) for _item in obj["effective_permission_states"]] if obj.get("effective_permission_states") is not None else None
        })
        return _obj


