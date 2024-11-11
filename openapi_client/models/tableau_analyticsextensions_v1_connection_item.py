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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.tableau_analyticsextensions_v1_connection_brief import TableauAnalyticsextensionsV1ConnectionBrief
from typing import Optional, Set
from typing_extensions import Self

class TableauAnalyticsextensionsV1ConnectionItem(BaseModel):
    """
    TableauAnalyticsextensionsV1ConnectionItem
    """ # noqa: E501
    host: Optional[StrictStr] = Field(default=None, description="Required. The location of an external service (TabPy, Rserve, Einstein_Discovery, Generic API, or other) that responds to your analytics extension requests. The case sensitive value must be a URI, IPv4 or IPv6 address that is a maximum of 255 Unicode characters. Starting in v2022.1, a host address can include path information (`www.example.com/path`), where previous versions supported only the root domain name (`www.example.com`). ")
    port: Optional[StrictInt] = Field(default=None, description="Required. Integer between 1 and 65535.")
    is_auth_enabled: Optional[StrictBool] = Field(default=None, description="For Tableau Online: The value is always true. For on premise Tableau servers: Optional. Set to true if authentication is enabled on the external service. If true, username and password are required. Default is false.")
    username: Optional[StrictStr] = Field(default=None, description="For Tableau Online: A username is always required.")
    password: Optional[StrictStr] = Field(default=None, description="For Tableau Online: A password is always required.")
    is_ssl_enabled: Optional[StrictBool] = Field(default=None, description="For Tableau Online: The value is always true. For on premise Tableau servers: Optional. Set true if SSL is enabled on the external service. If true, the host address must use HTTPS. Default is false.")
    connection_brief: Optional[TableauAnalyticsextensionsV1ConnectionBrief] = None
    connection_luid: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["host", "port", "is_auth_enabled", "username", "password", "is_ssl_enabled", "connection_brief", "connection_luid"]

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
        """Create an instance of TableauAnalyticsextensionsV1ConnectionItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of connection_brief
        if self.connection_brief:
            _dict['connection_brief'] = self.connection_brief.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TableauAnalyticsextensionsV1ConnectionItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "host": obj.get("host"),
            "port": obj.get("port"),
            "is_auth_enabled": obj.get("is_auth_enabled"),
            "username": obj.get("username"),
            "password": obj.get("password"),
            "is_ssl_enabled": obj.get("is_ssl_enabled"),
            "connection_brief": TableauAnalyticsextensionsV1ConnectionBrief.from_dict(obj["connection_brief"]) if obj.get("connection_brief") is not None else None,
            "connection_luid": obj.get("connection_luid")
        })
        return _obj


