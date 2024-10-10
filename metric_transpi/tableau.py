
from enum import Enum
import json
import string
from jinja2 import Environment, PackageLoader, select_autoescape
from metric_transpi.metric import Metric

env = Environment(
    loader=PackageLoader('metric_transpi', 'templates'),
    autoescape=select_autoescape()
)
env.filters['jsonify'] = json.dumps

def to_pulse_payload(metric: Metric) -> string:
    """
    Serialize a Metric object into a JSON using jinja2
    return JSON string
    """
    template = env.get_template('payload.json.jinja')
    return template.render(metric=metric)

class TableauAggregation(Enum):
    AGGREGATION_UNSPECIFIED = "AGGREGATION_UNSPECIFIED"
    AGGREGATION_SUM = "AGGREGATION_SUM"
    AGGREGATION_AVERAGE = "AGGREGATION_AVERAGE"
    AGGREGATION_MEDIAN = "AGGREGATION_MEDIAN"
    AGGREGATION_MAX ="AGGREGATION_MAX"
    AGGREGATION_MIN = "AGGREGATION_MIN"
    AGGREGATION_COUNT = "AGGREGATION_COUNT"
    AGGREGATION_COUNT_DISTINCT = "AGGREGATION_COUNT_DISTINCT"

class TableauGranularity(Enum):
    GRANULARITY_UNSPECIFIED = "GRANULARITY_UNSPECIFIED"
    GRANULARITY_BY_YEAR= "GRANULARITY_BY_YEAR"
    GRANULARITY_BY_QUARTER = "GRANULARITY_BY_QUARTER"
    GRANULARITY_BY_MONTH = "GRANULARITY_BY_MONTH"
    GRANULARITY_BY_WEEK = "GRANULARITY_BY_WEEK"
    GRANULARITY_BY_DAY = "GRANULARITY_BY_DAY"