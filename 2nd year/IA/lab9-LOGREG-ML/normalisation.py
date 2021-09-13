from math import log


def normalisation_min_max(data, minim, maxim):
    return [(d - minim) / (maxim - minim) for d in data]


def normalisation_z(data, mean, std):
    return [(d - mean) / std for d in data]


def normalisation_log(data):
    return [log(d) for d in data]
