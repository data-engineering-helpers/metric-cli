import yaml
from metric_transpi import Metric
from metric_transpi.metric import CALCULATION_METHOD


def from_yaml(path):
    """
    @return
    """
    
    with open(path) as file:
        body = yaml.safe_load(file)

    metrics = []
    for item in body["metrics"]:
        metric = Metric()
        metric.name = item["name"]
        metric.label = item["label"]
        metric.model = item["model"].split("'")[1]
        metric.description = item["description"]
        metric.calculation_method = CALCULATION_METHOD[item["calculation_method"]]
        metric.expression = item["expression"]
        metric.timestamp = item["timestamp"]
        metric.dimensions = item["dimensions"]
        metrics.append(metric)

    return metrics