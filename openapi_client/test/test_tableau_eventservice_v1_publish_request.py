# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_eventservice_v1_publish_request import TableauEventserviceV1PublishRequest

class TestTableauEventserviceV1PublishRequest(unittest.TestCase):
    """TableauEventserviceV1PublishRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauEventserviceV1PublishRequest:
        """Test TableauEventserviceV1PublishRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauEventserviceV1PublishRequest`
        """
        model = TableauEventserviceV1PublishRequest()
        if include_optional:
            return TableauEventserviceV1PublishRequest(
                service = '',
                event = openapi_client.models.tableau/eventservice/v1/event_input.tableau.eventservice.v1.EventInput(
                    type = '', 
                    details = '', )
            )
        else:
            return TableauEventserviceV1PublishRequest(
        )
        """

    def testTableauEventserviceV1PublishRequest(self):
        """Test TableauEventserviceV1PublishRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
