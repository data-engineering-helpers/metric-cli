from enum import Enum

CALCULATION_METHOD = Enum('CalculationMethod', [
    'count', 
    'count_distinct'
])
TIME_GRAINS = Enum('TimeGrains', [
    'day'
])

class Metric:

    name = ""
    labe = ""
    model = ""
    description = ""
    calculation_method = CALCULATION_METHOD.count
    expression = ""
    timestamp = ""
    time_grains = TIME_GRAINS.day
    dimensions = []