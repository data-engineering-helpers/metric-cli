from deepdiff import DeepDiff
import yaml

from pydantic import BaseModel
from enum import Enum
from typing import Any, Dict, List, Optional

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

    def to_dict(self) -> Dict[str, Any]:
        _dict = self.model_dump(
            by_alias=True,
            exclude_none=True,
        )
        
        return _dict


class Model(BaseModel):
    version: int
    metrics: List[Metric]



def diff(m1: Metric, m2: Metric):
    return DeepDiff(
        t1=m1.to_dict(),
        t2=m2.to_dict(), 
        exclude_paths=["model", "label"]
    )