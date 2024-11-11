import yaml
from metric_transpi import Metric
from metric_transpi.metric import CalculationMethod, TimeGrains


def from_yaml(path):
    """
    Load a yaml file which respects https://docs.getdbt.com/docs/build/metrics-overview
    return a list of Metric objects
    return None if YAML does not contain 'metrics'
    """
    
    with open(path) as file:
        body = yaml.safe_load(file)

    metrics = []
    if "metrics" not in body:
        raise ValueError('Reading YAML resulted in not finding a "metrics" section')
    
    for item in body["metrics"]:
        metric = Metric()
        metric.name = item["name"]
        metric.label = item["label"]
        metric.model = item["model"].split("'")[1]
        metric.description = item["description"]
        metric.calculation_method = CalculationMethod(item["calculation_method"])
        metric.expression = item["expression"]
        metric.timestamp = item["timestamp"]
        metric.dimensions = item["dimensions"]
        metric.time_grains = [TimeGrains(grain) for grain in item['time_grains']]
        metrics.append(metric)

    return metrics