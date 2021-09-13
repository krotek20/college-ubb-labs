from math import log


def normalisation_min_max(data, minim, maxim):
    flag = 0
    for key in data.keys():
        data[key] = [(d - minim[flag] / maxim[flag] - minim[flag]) for d in data[key]]
        flag += 1
    return data


def normalisation_z(data, mean, std):
    flag = 0
    for key in data.keys():
        data[key] = [(d - mean[flag]) / std[flag] for d in data[key]]
        flag += 1
    return data


def normalisation_log(data):
    for key in data.keys():
        data[key] = [log(d) for d in data[key]]
    return data
