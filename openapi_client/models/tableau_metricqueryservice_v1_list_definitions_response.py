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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.tableau_metricqueryservice_types_v1_definition import TableauMetricqueryserviceTypesV1Definition
from typing import Optional, Set
from typing_extensions import Self

class TableauMetricqueryserviceV1ListDefinitionsResponse(BaseModel):
    """
    TableauMetricqueryserviceV1ListDefinitionsResponse
    """ # noqa: E501
    definitions: Optional[List[TableauMetricqueryserviceTypesV1Definition]] = None
    next_page_token: Optional[StrictStr] = None
    total_available: Optional[StrictInt] = Field(default=None, description="If available, specifies the total number of items in a requested list")
    offset: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["definitions", "next_page_token", "total_available", "offset"]

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
        """Create an instance of TableauMetricqueryserviceV1ListDefinitionsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in definitions (list)
        _items = []
        if self.definitions:
            for _item_definitions in self.definitions:
                if _item_definitions:
                    _items.append(_item_definitions.to_dict())
            _dict['definitions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TableauMetricqueryserviceV1ListDefinitionsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "definitions": [TableauMetricqueryserviceTypesV1Definition.from_dict(_item) for _item in obj["definitions"]] if obj.get("definitions") is not None else None,
            "next_page_token": obj.get("next_page_token"),
            "total_available": obj.get("total_available"),
            "offset": obj.get("offset")
        })
        return _obj


