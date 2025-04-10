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

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.tableau_metricqueryservice_types_v1_compare_config import TableauMetricqueryserviceTypesV1CompareConfig
from typing import Optional, Set
from typing_extensions import Self

class TableauMetricqueryserviceTypesV1ComparisonsComparison(BaseModel):
    """
    TableauMetricqueryserviceTypesV1ComparisonsComparison
    """ # noqa: E501
    compare_config: Optional[TableauMetricqueryserviceTypesV1CompareConfig] = None
    index: Optional[int] = None
    __properties: ClassVar[List[str]] = ["compare_config", "index"]

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
        """Create an instance of TableauMetricqueryserviceTypesV1ComparisonsComparison from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of compare_config
        if self.compare_config:
            _dict['compare_config'] = self.compare_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TableauMetricqueryserviceTypesV1ComparisonsComparison from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "compare_config": TableauMetricqueryserviceTypesV1CompareConfig.from_dict(obj["compare_config"]) if obj.get("compare_config") is not None else None,
            "index": obj.get("index")
        })
        return _obj


