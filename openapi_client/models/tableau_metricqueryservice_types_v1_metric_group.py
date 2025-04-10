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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.tableau_metricqueryservice_types_v1_metric import TableauMetricqueryserviceTypesV1Metric
from openapi_client.models.tableau_metricqueryservice_types_v1_metric_group_group_metadata import TableauMetricqueryserviceTypesV1MetricGroupGroupMetadata
from typing import Optional, Set
from typing_extensions import Self

class TableauMetricqueryserviceTypesV1MetricGroup(BaseModel):
    """
    TableauMetricqueryserviceTypesV1MetricGroup
    """ # noqa: E501
    group_metadata: Optional[TableauMetricqueryserviceTypesV1MetricGroupGroupMetadata] = None
    metrics: Optional[List[TableauMetricqueryserviceTypesV1Metric]] = None
    nested_group_metadata: Optional[Dict[str, Any]] = Field(default=None, alias="nestedGroupMetadata")
    __properties: ClassVar[List[str]] = ["group_metadata", "metrics", "nestedGroupMetadata"]

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
        """Create an instance of TableauMetricqueryserviceTypesV1MetricGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of group_metadata
        if self.group_metadata:
            _dict['group_metadata'] = self.group_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in metrics (list)
        _items = []
        if self.metrics:
            for _item_metrics in self.metrics:
                if _item_metrics:
                    _items.append(_item_metrics.to_dict())
            _dict['metrics'] = _items
        # override the default output from pydantic by calling `to_dict()` of nested_group_metadata
        if self.nested_group_metadata:
            _dict['nestedGroupMetadata'] = self.nested_group_metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TableauMetricqueryserviceTypesV1MetricGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "group_metadata": TableauMetricqueryserviceTypesV1MetricGroupGroupMetadata.from_dict(obj["group_metadata"]) if obj.get("group_metadata") is not None else None,
            "metrics": [TableauMetricqueryserviceTypesV1Metric.from_dict(_item) for _item in obj["metrics"]] if obj.get("metrics") is not None else None,
            "nestedGroupMetadata": TableauMetricqueryserviceTypesV1MetricGroupGroupMetadata.from_dict(obj["nestedGroupMetadata"]) if obj.get("nestedGroupMetadata") is not None else None
        })
        return _obj


