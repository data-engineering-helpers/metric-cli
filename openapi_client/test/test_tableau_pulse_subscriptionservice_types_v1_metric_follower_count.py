# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_pulse_subscriptionservice_types_v1_metric_follower_count import TableauPulseSubscriptionserviceTypesV1MetricFollowerCount

class TestTableauPulseSubscriptionserviceTypesV1MetricFollowerCount(unittest.TestCase):
    """TableauPulseSubscriptionserviceTypesV1MetricFollowerCount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauPulseSubscriptionserviceTypesV1MetricFollowerCount:
        """Test TableauPulseSubscriptionserviceTypesV1MetricFollowerCount
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauPulseSubscriptionserviceTypesV1MetricFollowerCount`
        """
        model = TableauPulseSubscriptionserviceTypesV1MetricFollowerCount()
        if include_optional:
            return TableauPulseSubscriptionserviceTypesV1MetricFollowerCount(
                metric_id = '',
                follower_count = 56
            )
        else:
            return TableauPulseSubscriptionserviceTypesV1MetricFollowerCount(
        )
        """

    def testTableauPulseSubscriptionserviceTypesV1MetricFollowerCount(self):
        """Test TableauPulseSubscriptionserviceTypesV1MetricFollowerCount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
