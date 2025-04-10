# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tableau_pulse_subscriptionservice_v1_create_subscription_response import TableauPulseSubscriptionserviceV1CreateSubscriptionResponse

class TestTableauPulseSubscriptionserviceV1CreateSubscriptionResponse(unittest.TestCase):
    """TableauPulseSubscriptionserviceV1CreateSubscriptionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TableauPulseSubscriptionserviceV1CreateSubscriptionResponse:
        """Test TableauPulseSubscriptionserviceV1CreateSubscriptionResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TableauPulseSubscriptionserviceV1CreateSubscriptionResponse`
        """
        model = TableauPulseSubscriptionserviceV1CreateSubscriptionResponse()
        if include_optional:
            return TableauPulseSubscriptionserviceV1CreateSubscriptionResponse(
                subscription = openapi_client.models.tableau/pulse/subscriptionservice/types/v1/subscription.tableau.pulse.subscriptionservice.types.v1.Subscription(
                    id = '', 
                    metric_id = '', 
                    follower = openapi_client.models.tableau/pulse/subscriptionservice/types/v1/follower.tableau.pulse.subscriptionservice.types.v1.Follower(
                        user_id = '', 
                        group_id = '', ), 
                    create_time = '', 
                    update_time = '', )
            )
        else:
            return TableauPulseSubscriptionserviceV1CreateSubscriptionResponse(
        )
        """

    def testTableauPulseSubscriptionserviceV1CreateSubscriptionResponse(self):
        """Test TableauPulseSubscriptionserviceV1CreateSubscriptionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
