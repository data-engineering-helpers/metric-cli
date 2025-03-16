import yaml

from pydantic import BaseModel
from enum import Enum
from typing import List, Optional

def from_yaml(path):
    """
    Load a yaml file which respects https://docs.getdbt.com/docs/build/metrics-overview
    return a list of Metric objects
    return None if YAML does not contain 'metrics'
    """
    
    with open(path) as file:
        body = yaml.safe_load(file)
    metrics = Model(**body).metrics
    return metrics


class CalculationMethod(str, Enum):
    COUNT = 'count'
    COUNT_DISTINCT = 'count_distinct'
    SUM = 'sum'
    AVERAGE = 'average'
    MIN = 'min'
    MAX = 'max'
    MEDIAN = 'median'

class TimeGrains(str, Enum):
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    QUARTER = 'quarter'
    YEAR = 'year'
        
class Metric(BaseModel):
    name: str
    model: str
    label: Optional[str] = None
    description: Optional[str] = None
    datasource_id: Optional[str] = None
    calculation_method: CalculationMethod
    expression: str
    timestamp: str
    time_grains: List[TimeGrains]
    dimensions: List[str]


class Model(BaseModel):
    version: int
    metrics: List[Metric]

        