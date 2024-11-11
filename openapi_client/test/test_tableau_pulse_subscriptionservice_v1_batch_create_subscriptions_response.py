# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_response import TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse

class TestTableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse(unittest.TestCase):
    """TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse:
        """Test TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse`
        """
        model = TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse()
        if include_optional:
            return TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse(
                subscriptions = [
                    openapi_client.models.tableau/pulse/subscriptionservice/types/v1/subscription.tableau.pulse.subscriptionservice.types.v1.Subscription(
                        id = '', 
                        metric_id = '', 
                        follower = openapi_client.models.tableau/pulse/subscriptionservice/types/v1/follower.tableau.pulse.subscriptionservice.types.v1.Follower(
                            user_id = '', 
                            group_id = '', ), 
                        create_time = '', 
                        update_time = '', )
                    ]
            )
        else:
            return TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse(
        )
        """

    def testTableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse(self):
        """Test TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
