from enum import Enum

CALCULATION_METHOD = Enum('CalculationMethod', [
    'COUNT', 
    'COUNT_DISTINCT'
])
TIME_GRAINS = Enum('TimeGrains', [
    'DAY'
])

class Metric:

    name = ""
    labe = ""
    model = ""
    description = ""
    calculation_method = CALCULATION_METHOD.COUNT
    expression = ""
    timestamp = ""
    time_grains = TIME_GRAINS.DAY
    dimensions = []