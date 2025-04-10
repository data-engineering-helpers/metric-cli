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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TableauUsagestatsV1UsageStats(BaseModel):
    """
    TableauUsagestatsV1UsageStats
    """ # noqa: E501
    hits_total: Optional[StrictInt] = Field(default=None, description="The number of times the content item has been marked as used.", alias="hitsTotal")
    hits_last_two_weeks_total: Optional[StrictInt] = Field(default=None, description="The number of times the content item has been marked as used in the last two weeks.", alias="hitsLastTwoWeeksTotal")
    hits_last_one_month_total: Optional[StrictInt] = Field(default=None, description="The number of times the content item has been marked as used in the last month.", alias="hitsLastOneMonthTotal")
    hits_last_three_months_total: Optional[StrictInt] = Field(default=None, description="The number of times the content item has been marked as used in the last three months.", alias="hitsLastThreeMonthsTotal")
    hits_last_twelve_months_total: Optional[StrictInt] = Field(default=None, description="The number of times the content item has been marked as used in the last tweleve months.", alias="hitsLastTwelveMonthsTotal")
    __properties: ClassVar[List[str]] = ["hitsTotal", "hitsLastTwoWeeksTotal", "hitsLastOneMonthTotal", "hitsLastThreeMonthsTotal", "hitsLastTwelveMonthsTotal"]

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
        """Create an instance of TableauUsagestatsV1UsageStats from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TableauUsagestatsV1UsageStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hitsTotal": obj.get("hitsTotal"),
            "hitsLastTwoWeeksTotal": obj.get("hitsLastTwoWeeksTotal"),
            "hitsLastOneMonthTotal": obj.get("hitsLastOneMonthTotal"),
            "hitsLastThreeMonthsTotal": obj.get("hitsLastThreeMonthsTotal"),
            "hitsLastTwelveMonthsTotal": obj.get("hitsLastTwelveMonthsTotal")
        })
        return _obj


