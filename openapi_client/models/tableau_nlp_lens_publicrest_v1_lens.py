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
from openapi_client.models.tableau_nlp_lens_publicrest_v1_lens_field import TableauNlpLensPublicrestV1LensField
from openapi_client.models.tableau_nlp_lens_publicrest_v1_recommended_visualization_group import TableauNlpLensPublicrestV1RecommendedVisualizationGroup
from typing import Optional, Set
from typing_extensions import Self

class TableauNlpLensPublicrestV1Lens(BaseModel):
    """
    TableauNlpLensPublicrestV1Lens
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Luid of the lens")
    name: Optional[StrictStr] = Field(default=None, description="Name of the lens")
    site_id: Optional[StrictStr] = Field(default=None, description="Luid of the site to which the lens belong to.")
    datasource_id: Optional[StrictStr] = Field(default=None, description="Luid of the datasource to which the lens is associated to.")
    project_id: Optional[StrictStr] = Field(default=None, description="Luid of the project.")
    owner_id: Optional[StrictStr] = Field(default=None, description="Luid of the owner of the lens.")
    description: Optional[StrictStr] = Field(default=None, description="Description of the lens.")
    repository_url: Optional[StrictStr] = Field(default=None, description="Internal URL to access the lens.")
    is_feedback_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if feedback to lens author setting is enabled")
    fields: Optional[List[TableauNlpLensPublicrestV1LensField]] = None
    recommended_visualization_groups: Optional[List[TableauNlpLensPublicrestV1RecommendedVisualizationGroup]] = None
    __properties: ClassVar[List[str]] = ["id", "name", "site_id", "datasource_id", "project_id", "owner_id", "description", "repository_url", "is_feedback_enabled", "fields", "recommended_visualization_groups"]

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
        """Create an instance of TableauNlpLensPublicrestV1Lens from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in recommended_visualization_groups (list)
        _items = []
        if self.recommended_visualization_groups:
            for _item_recommended_visualization_groups in self.recommended_visualization_groups:
                if _item_recommended_visualization_groups:
                    _items.append(_item_recommended_visualization_groups.to_dict())
            _dict['recommended_visualization_groups'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TableauNlpLensPublicrestV1Lens from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "site_id": obj.get("site_id"),
            "datasource_id": obj.get("datasource_id"),
            "project_id": obj.get("project_id"),
            "owner_id": obj.get("owner_id"),
            "description": obj.get("description"),
            "repository_url": obj.get("repository_url"),
            "is_feedback_enabled": obj.get("is_feedback_enabled"),
            "fields": [TableauNlpLensPublicrestV1LensField.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
            "recommended_visualization_groups": [TableauNlpLensPublicrestV1RecommendedVisualizationGroup.from_dict(_item) for _item in obj["recommended_visualization_groups"]] if obj.get("recommended_visualization_groups") is not None else None
        })
        return _obj


