# coding: utf-8

"""
    Tableau Services APIs

    Open API specification for Tableau Services APIs

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.metric_definitions_api import MetricDefinitionsApi


class TestMetricDefinitionsApi(unittest.TestCase):
    """MetricDefinitionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MetricDefinitionsApi()

    def tearDown(self) -> None:
        pass

    def test_metric_query_service_batch_get_definitions(self) -> None:
        """Test case for metric_query_service_batch_get_definitions

        Gets a batch of definition and metrics available on a server.
        """
        pass

    def test_metric_query_service_batch_get_definitions_by_post(self) -> None:
        """Test case for metric_query_service_batch_get_definitions_by_post

        Gets a batch of definition and metrics available on a server.
        """
        pass

    def test_metric_query_service_batch_get_metrics(self) -> None:
        """Test case for metric_query_service_batch_get_metrics

        Gets a batch of metrics available on a server.
        """
        pass

    def test_metric_query_service_create_definition(self) -> None:
        """Test case for metric_query_service_create_definition

        Creates a metric definition.
        """
        pass

    def test_metric_query_service_create_metric(self) -> None:
        """Test case for metric_query_service_create_metric

        Creates a metric.
        """
        pass

    def test_metric_query_service_delete_definition(self) -> None:
        """Test case for metric_query_service_delete_definition

        Deletes a metric definition.
        """
        pass

    def test_metric_query_service_delete_metric(self) -> None:
        """Test case for metric_query_service_delete_metric

        Deletes a metric.
        """
        pass

    def test_metric_query_service_get_definition(self) -> None:
        """Test case for metric_query_service_get_definition

        Gets a metric definition based on the specified id.
        """
        pass

    def test_metric_query_service_get_metric(self) -> None:
        """Test case for metric_query_service_get_metric

        Gets the metric by ID.
        """
        pass

    def test_metric_query_service_get_or_create_metric(self) -> None:
        """Test case for metric_query_service_get_or_create_metric

        Creates a metric and returns boolean indicating whether the new metric was created or not.
        """
        pass

    def test_metric_query_service_list_definitions(self) -> None:
        """Test case for metric_query_service_list_definitions

        Lists the definitions available on a server.
        """
        pass

    def test_metric_query_service_list_metrics(self) -> None:
        """Test case for metric_query_service_list_metrics

        Lists the metrics available on a server.
        """
        pass

    def test_metric_query_service_update_definition(self) -> None:
        """Test case for metric_query_service_update_definition

        Updates a metric definition.
        """
        pass

    def test_metric_query_service_update_metric(self) -> None:
        """Test case for metric_query_service_update_metric

        Updates a metric.
        """
        pass

    def test_pulse_subscription_service_list_followed_metrics_groups(self) -> None:
        """Test case for pulse_subscription_service_list_followed_metrics_groups

        List followed metrics groups
        """
        pass


if __name__ == '__main__':
    unittest.main()
