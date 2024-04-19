
from statistics import mean

def calc_average(values):
    float_values = []
    for value in values:
        float_values.append(float(value))

    average = mean(float_values)
    round_average = round(average, 2)
    return round_average
