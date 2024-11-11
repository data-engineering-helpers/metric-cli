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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.tableau_pulse_subscriptionservice_types_v1_channel_preferences import TableauPulseSubscriptionserviceTypesV1ChannelPreferences
from openapi_client.models.tableau_pulse_subscriptionservice_types_v1_metric_grouping_preferences import TableauPulseSubscriptionserviceTypesV1MetricGroupingPreferences
from typing import Optional, Set
from typing_extensions import Self

class TableauPulseSubscriptionserviceV1UserPreferencesResponse(BaseModel):
    """
    TableauPulseSubscriptionserviceV1UserPreferencesResponse
    """ # noqa: E501
    cadence: Optional[StrictStr] = None
    channel_preferences: Optional[List[TableauPulseSubscriptionserviceTypesV1ChannelPreferences]] = None
    metric_grouping_preferences: Optional[TableauPulseSubscriptionserviceTypesV1MetricGroupingPreferences] = None
    __properties: ClassVar[List[str]] = ["cadence", "channel_preferences", "metric_grouping_preferences"]

    @field_validator('cadence')
    def cadence_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CADENCE_UNSPECIFIED', 'CADENCE_DAILY', 'CADENCE_WEEKLY', 'CADENCE_MONTHLY']):
            raise ValueError("must be one of enum values ('CADENCE_UNSPECIFIED', 'CADENCE_DAILY', 'CADENCE_WEEKLY', 'CADENCE_MONTHLY')")
        return value

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
        """Create an instance of TableauPulseSubscriptionserviceV1UserPreferencesResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in channel_preferences (list)
        _items = []
        if self.channel_preferences:
            for _item_channel_preferences in self.channel_preferences:
                if _item_channel_preferences:
                    _items.append(_item_channel_preferences.to_dict())
            _dict['channel_preferences'] = _items
        # override the default output from pydantic by calling `to_dict()` of metric_grouping_preferences
        if self.metric_grouping_preferences:
            _dict['metric_grouping_preferences'] = self.metric_grouping_preferences.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TableauPulseSubscriptionserviceV1UserPreferencesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cadence": obj.get("cadence"),
            "channel_preferences": [TableauPulseSubscriptionserviceTypesV1ChannelPreferences.from_dict(_item) for _item in obj["channel_preferences"]] if obj.get("channel_preferences") is not None else None,
            "metric_grouping_preferences": TableauPulseSubscriptionserviceTypesV1MetricGroupingPreferences.from_dict(obj["metric_grouping_preferences"]) if obj.get("metric_grouping_preferences") is not None else None
        })
        return _obj


