from math import log


def prediction_error(real_outputs, computed_outputs):
    from math import sqrt

    return sqrt(sum([x ** 2 for x in
                     [sqrt(sum((real - computed) ** 2 for real, computed in zip(real_outputs[i], computed_outputs[i]))
                           / len(real_outputs[i])) for i in range(len(real_outputs))]]) / len(real_outputs))


def compute_dict(labels, values):
    row = {}
    for label in labels:
        if values == 'dict':
            row[label] = {}
        else:
            row[label] = 0
    return row


def confusion_matrix(real, computed, labels):
    cm = compute_dict(labels, 'dict')
    for label in labels:
        row = compute_dict(labels, 'numeric')
        for i in range(len(real)):
            if real[i] == label:
                row[computed[i]] += 1
        cm[label] = row
    return cm


def accuracy_precision_recall(real_labels, computed_labels, label_names):
    cm = confusion_matrix(real_labels, computed_labels, label_names)
    accuracy = sum([1 if real_labels[i] == computed_labels[i] else 0
                    for i in range(0, len(real_labels))]) / len(real_labels)
    precision = {}
    recall = {}
    for label in label_names:
        precision[label] = cm[label][label] / sum(x[label] for x in cm.values())
        recall[label] = cm[label][label] / sum(x for x in cm[label].values())
    return cm, accuracy, precision, recall


# using MSE = mean squared error
def regression_loss(real, computed):
    return sum([(real[i] - computed[i]) ** 2 for i in range(len(real))]) / len(real)


def binary_loss(real, computed):
    return -sum([real[i] * log(computed[i][0]) + (1 - real[i]) * log(computed[i][1]) for i in range(len(real))]) / len(
        real)


def multi_class_loss(real, computed):
    return -sum([log(1e-15 + computed[i][real[i]]) for i in range(len(real))]) / len(real)


def float_xor(a, b):
    import struct
    rtrn = []
    a = struct.pack('d', a)
    b = struct.pack('d', b)
    for ba, bb in zip(a, b):
        rtrn.append(ba ^ bb)

    return struct.unpack('d', bytes(rtrn))[0]


def multi_label_loss(real, computed):
    return sum(
        [sum([float_xor(real[i][j], computed[i][j]) for j in range(len(real[i]))]) for i in range(len(real))]) / (
                       len(real) * len(real[0]))


# prediction error
real_for_error = [[533, 1000, 89], [577, 1103, 76], [550, 1523, 43], [520, 1300, 13], [530, 1530, 65], [589, 1050, 83]]
computed_for_error = [[529, 1000, 88], [577, 1113, 76], [540, 1600, 54], [523, 1299, 13], [545, 1505, 68],
                      [601, 1065, 76]]
print(prediction_error(real_for_error, computed_for_error))
print()

# accuracy, prediction, recall
real_for_apr = ['a', 'a', 'b', 'c', 'b', 'c', 'a', 'a', 'b', 'c', 'a']
computed_for_apr = ['a', 'a', 'c', 'c', 'a', 'c', 'b', 'a', 'b', 'a', 'c']
names_for_apr = ['a', 'b', 'c']
c, a, p, r = accuracy_precision_recall(real_for_apr, computed_for_apr, names_for_apr)
print(str(c))
print(str(a))
print(str(p))
print(str(r) + '\n')

# regression loss
real_for_regloss = [15, 85, 73, 22, 35, 56, 43, 72]
computed_for_regloss = [17, 85, 78, 31, 35, 55, 43, 74]
print(regression_loss(real_for_regloss, computed_for_regloss))

# binary classifier loss
real_for_binaryloss = [1, 0, 0, 0, 1, 1, 1, 1, 0]
computed_for_binaryloss = [[.1, .9], [.7, .3], [.2, .8], [.9, .1], [.8, .2], [.5, .5], [.3, .7], [.2, .8], [.9, .1]]
print(binary_loss(real_for_binaryloss, computed_for_binaryloss))

# multiclass classifier loss
real_for_multiclassloss = [3, 1, 1, 2, 0, 0, 1, 3, 3, 2, 0]
computed_for_multiclassloss = [[.25, .25, .25, .25], [.0, .7, .2, .1], [.1, .6, .1, .2], [.3, .3, .2, .2],
                               [.7, .0, .0, .3], [.5, .5, .0, .0], [.2, .8, .0, .0], [.0, .1, .9, .0], [.0, .2, .8, .0],
                               [.1, .1, .7, .1], [.6, .2, .2, .0]]
print(multi_class_loss(real_for_multiclassloss, computed_for_multiclassloss))

# multi-label classifier loss - limit is 0.4
real_for_multilabelloss = [[1, 1, 1, 0], [0, 1, 0, 1], [0, 1, 0, 0], [1, 1, 0, 1]]
computed_for_multilabelloss = [[.9, .5, .4, .2], [.2, .7, .2, .8], [.1, .5, .2, .3], [.9, .7, .2, .4]]
print(multi_label_loss(real_for_multilabelloss, computed_for_multilabelloss))
