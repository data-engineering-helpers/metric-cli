
import json
from logging import log
import logging

import jsondiff
from metric_transpi import tableau
from metric_transpi.metric import Metric, TimeGrains


def test_to_pulse_payload_should_return_dic_with_pulse_structure():
    # given
    metric = Metric()
    metric.name = "GMV Amount in Euros"
    metric.model = "d9b941fc-f134-4772-8088-b0e2b1f0f78b"
    metric.expression = "02972a33-fc19-353f-a209-5a5b3f423d8d"
    metric.calculation_method = "AGGREGATION_SUM"
    metric.timestamp = "6ee0624f-9f9a-3c73-a002-2c9748f5a04a"
    metric.dimensions = [
        "1589d05d-f022-34de-ac30-b1cba2d1cd8f",
        "1174a807-af10-38eb-8f8f-408a1da58ce9",
        "c4861818-df8c-3267-bc6a-0086d885ffed"
    ]
    metric.time_grains = []

    # when
    json_r = tableau.to_pulse_payload(metric)

    # then
    with open("metric_transpi/tests/validated_payload.json") as example:
        assert json.loads(json_r) == json.load(example)