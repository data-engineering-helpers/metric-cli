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
from openapi_client.models.tableau_metricqueryservice_types_v1_comparisons import TableauMetricqueryserviceTypesV1Comparisons
from openapi_client.models.tableau_metricqueryservice_types_v1_definition_specification import TableauMetricqueryserviceTypesV1DefinitionSpecification
from openapi_client.models.tableau_metricqueryservice_types_v1_extension_options import TableauMetricqueryserviceTypesV1ExtensionOptions
from openapi_client.models.tableau_metricqueryservice_types_v1_insights_options import TableauMetricqueryserviceTypesV1InsightsOptions
from openapi_client.models.tableau_metricqueryservice_types_v1_representation_options import TableauMetricqueryserviceTypesV1RepresentationOptions
from typing import Optional, Set
from typing_extensions import Self

class TableauMetricqueryserviceV1UpdateDefinitionRequest(BaseModel):
    """
    TableauMetricqueryserviceV1UpdateDefinitionRequest
    """ # noqa: E501
    definition_id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    specification: Optional[TableauMetricqueryserviceTypesV1DefinitionSpecification] = None
    extension_options: Optional[TableauMetricqueryserviceTypesV1ExtensionOptions] = None
    representation_options: Optional[TableauMetricqueryserviceTypesV1RepresentationOptions] = None
    insights_options: Optional[TableauMetricqueryserviceTypesV1InsightsOptions] = None
    user_link: Optional[StrictStr] = None
    user_link_name: Optional[StrictStr] = None
    comparisons: Optional[TableauMetricqueryserviceTypesV1Comparisons] = None
    __properties: ClassVar[List[str]] = ["definition_id", "name", "description", "specification", "extension_options", "representation_options", "insights_options", "user_link", "user_link_name", "comparisons"]

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
        """Create an instance of TableauMetricqueryserviceV1UpdateDefinitionRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of specification
        if self.specification:
            _dict['specification'] = self.specification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extension_options
        if self.extension_options:
            _dict['extension_options'] = self.extension_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of representation_options
        if self.representation_options:
            _dict['representation_options'] = self.representation_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of insights_options
        if self.insights_options:
            _dict['insights_options'] = self.insights_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of comparisons
        if self.comparisons:
            _dict['comparisons'] = self.comparisons.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TableauMetricqueryserviceV1UpdateDefinitionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "definition_id": obj.get("definition_id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "specification": TableauMetricqueryserviceTypesV1DefinitionSpecification.from_dict(obj["specification"]) if obj.get("specification") is not None else None,
            "extension_options": TableauMetricqueryserviceTypesV1ExtensionOptions.from_dict(obj["extension_options"]) if obj.get("extension_options") is not None else None,
            "representation_options": TableauMetricqueryserviceTypesV1RepresentationOptions.from_dict(obj["representation_options"]) if obj.get("representation_options") is not None else None,
            "insights_options": TableauMetricqueryserviceTypesV1InsightsOptions.from_dict(obj["insights_options"]) if obj.get("insights_options") is not None else None,
            "user_link": obj.get("user_link"),
            "user_link_name": obj.get("user_link_name"),
            "comparisons": TableauMetricqueryserviceTypesV1Comparisons.from_dict(obj["comparisons"]) if obj.get("comparisons") is not None else None
        })
        return _obj


