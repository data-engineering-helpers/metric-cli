# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_error import TableauError

class TestTableauError(unittest.TestCase):
    """TableauError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauError:
        """Test TableauError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauError`
        """
        model = TableauError()
        if include_optional:
            return TableauError(
                http_error_code = '',
                message = ''
            )
        else:
            return TableauError(
        )
        """

    def testTableauError(self):
        """Test TableauError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
