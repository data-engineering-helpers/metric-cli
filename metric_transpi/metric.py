from enum import Enum

class CalculationMethod(str, Enum):
    COUNT = 'count'
    COUNT_DISTINCT = 'count_distinct'

class TimeGrains(str, Enum):
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    QUARTER = 'quarter'
    YEAR = 'year'
        
class Metric:
    name = ""
    labe = ""
    model = ""
    description = ""
    calculation_method = CalculationMethod.COUNT
    expression = ""
    timestamp = ""
    time_grains = [TimeGrains.DAY]
    dimensions = []
    filters = []