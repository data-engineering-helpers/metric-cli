# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_usagestats_v1_content_item_id import TableauUsagestatsV1ContentItemId

class TestTableauUsagestatsV1ContentItemId(unittest.TestCase):
    """TableauUsagestatsV1ContentItemId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauUsagestatsV1ContentItemId:
        """Test TableauUsagestatsV1ContentItemId
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauUsagestatsV1ContentItemId`
        """
        model = TableauUsagestatsV1ContentItemId()
        if include_optional:
            return TableauUsagestatsV1ContentItemId(
                luid = '',
                type = ''
            )
        else:
            return TableauUsagestatsV1ContentItemId(
        )
        """

    def testTableauUsagestatsV1ContentItemId(self):
        """Test TableauUsagestatsV1ContentItemId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
