# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_usagestats_v1_batch_get_usage_request import TableauUsagestatsV1BatchGetUsageRequest

class TestTableauUsagestatsV1BatchGetUsageRequest(unittest.TestCase):
    """TableauUsagestatsV1BatchGetUsageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauUsagestatsV1BatchGetUsageRequest:
        """Test TableauUsagestatsV1BatchGetUsageRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauUsagestatsV1BatchGetUsageRequest`
        """
        model = TableauUsagestatsV1BatchGetUsageRequest()
        if include_optional:
            return TableauUsagestatsV1BatchGetUsageRequest(
                content_items = [
                    openapi_client.models.tableau/usagestats/v1/content_item_id.tableau.usagestats.v1.ContentItemId(
                        luid = '', 
                        type = '', )
                    ]
            )
        else:
            return TableauUsagestatsV1BatchGetUsageRequest(
        )
        """

    def testTableauUsagestatsV1BatchGetUsageRequest(self):
        """Test TableauUsagestatsV1BatchGetUsageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
