# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_usagestats_v1_content_item_usage_stats import TableauUsagestatsV1ContentItemUsageStats

class TestTableauUsagestatsV1ContentItemUsageStats(unittest.TestCase):
    """TableauUsagestatsV1ContentItemUsageStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauUsagestatsV1ContentItemUsageStats:
        """Test TableauUsagestatsV1ContentItemUsageStats
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauUsagestatsV1ContentItemUsageStats`
        """
        model = TableauUsagestatsV1ContentItemUsageStats()
        if include_optional:
            return TableauUsagestatsV1ContentItemUsageStats(
                content = openapi_client.models.tableau/usagestats/v1/content_item_id.tableau.usagestats.v1.ContentItemId(
                    luid = '', 
                    type = '', ),
                usage = openapi_client.models.tableau/usagestats/v1/usage_stats.tableau.usagestats.v1.UsageStats(
                    hits_total = 56, 
                    hits_last_two_weeks_total = 56, 
                    hits_last_one_month_total = 56, 
                    hits_last_three_months_total = 56, 
                    hits_last_twelve_months_total = 56, )
            )
        else:
            return TableauUsagestatsV1ContentItemUsageStats(
        )
        """

    def testTableauUsagestatsV1ContentItemUsageStats(self):
        """Test TableauUsagestatsV1ContentItemUsageStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
