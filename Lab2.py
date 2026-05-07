def calc_average_temperature(temperature_list):
    total = sum(temperature_list)
    average = total / len(temperature_list)
    return float(average)

def calc_min_max_temperature(list_temp):
    min_temp = min(list_temp)
    max_temp = max(list_temp)
    final_list = [int(min_temp), int(max_temp)]
    return final_list

def calc_median_temperature(num_list):
    sorted_list = sorted(num_list)
    n = len(sorted_list)
    
    if n % 2 == 1:   # odd
        median = sorted_list[n // 2]
    else:            # even
        mid1 = sorted_list[n // 2]
        mid2 = sorted_list[n // 2 - 1]
        median = (mid1 + mid2) / 2
    
    return median