import yaml
from metric_transpi import Metric
from metric_transpi.metric import CALCULATION_METHOD


def from_yaml(path):
    # TODO document 
    
    with open(path) as file:
        body = yaml.safe_load(file)

    metric = Metric()
    for item in body["metrics"]:
        pass
    metric.name = body["metrics"][0]["name"]
    metric.label = body["metrics"][0]["label"]
    metric.model = body["metrics"][0]["model"].split("'")[1]
    metric.description = body["metrics"][0]["description"]
    metric.calculation_method = CALCULATION_METHOD[body["metrics"][0]["calculation_method"]]
    metric.expression = body["metrics"][0]["expression"]
    metric.timestamp = body["metrics"][0]["timestamp"]
    metric.dimensions = body["metrics"][0]["dimensions"]

    return metric