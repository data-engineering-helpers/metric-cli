# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_pulse_subscriptionservice_v1_update_user_preferences_request import TableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest

class TestTableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest(unittest.TestCase):
    """TableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest:
        """Test TableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest`
        """
        model = TableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest()
        if include_optional:
            return TableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest(
                cadence = 'CADENCE_UNSPECIFIED',
                channel_preferences_request = [
                    openapi_client.models.tableau/pulse/subscriptionservice/types/v1/channel_preferences_request.tableau.pulse.subscriptionservice.types.v1.ChannelPreferencesRequest(
                        channel = 'DELIVERY_CHANNEL_UNSPECIFIED', 
                        status = 'CHANNEL_STATUS_UNSPECIFIED', )
                    ],
                metric_grouping_preferences = openapi_client.models.tableau/pulse/subscriptionservice/types/v1/metric_grouping_preferences.tableau.pulse.subscriptionservice.types.v1.MetricGroupingPreferences(
                    group_by = 'GROUP_BY_UNSPECIFIED', 
                    sort_order = 'SORT_ORDER_UNSPECIFIED', )
            )
        else:
            return TableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest(
        )
        """

    def testTableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest(self):
        """Test TableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
