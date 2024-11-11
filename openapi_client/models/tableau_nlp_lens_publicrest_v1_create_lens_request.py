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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.tableau_nlp_lens_publicrest_v1_field_detail import TableauNlpLensPublicrestV1FieldDetail
from typing import Optional, Set
from typing_extensions import Self

class TableauNlpLensPublicrestV1CreateLensRequest(BaseModel):
    """
    TableauNlpLensPublicrestV1CreateLensRequest
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Required. Name of the lens . Upto 300 characters")
    datasource_id: Optional[StrictStr] = Field(default=None, description="Required. Luid of the datasource to which the lens is associated to")
    project_id: Optional[StrictStr] = Field(default=None, description="Required. Luid of the project in which lens should be created.")
    description: Optional[StrictStr] = Field(default=None, description="Optional. Description of the lens. 4000 characters maximum")
    is_feedback_enabled: Optional[StrictBool] = Field(default=None, description="Required. Indicates if feedback to lens author setting is enabled.")
    fields: Optional[List[TableauNlpLensPublicrestV1FieldDetail]] = None
    __properties: ClassVar[List[str]] = ["name", "datasource_id", "project_id", "description", "is_feedback_enabled", "fields"]

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
        """Create an instance of TableauNlpLensPublicrestV1CreateLensRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item_fields in self.fields:
                if _item_fields:
                    _items.append(_item_fields.to_dict())
            _dict['fields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TableauNlpLensPublicrestV1CreateLensRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "datasource_id": obj.get("datasource_id"),
            "project_id": obj.get("project_id"),
            "description": obj.get("description"),
            "is_feedback_enabled": obj.get("is_feedback_enabled"),
            "fields": [TableauNlpLensPublicrestV1FieldDetail.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None
        })
        return _obj


