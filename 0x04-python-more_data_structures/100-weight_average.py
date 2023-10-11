#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    weighted_sum = 0
    total_weights = 0

    for weight_pair in my_list:
        weighted_sum += weight_pair[0] * weight_pair[1]
        total_weights += weight_pair[1]

    return (weighted_sum / total_weights)
