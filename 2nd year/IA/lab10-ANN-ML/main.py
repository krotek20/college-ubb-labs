from sklearn.datasets import load_iris, load_digits
import matplotlib.pyplot as plt
import numpy as np

from normalisation import normalisation_min_max, normalisation_z, normalisation_log
from NeuralNetwork import NeuralNetwork


def plot_data_histogram(x, var):
    n, bins, patches = plt.hist(x, 10)
    plt.title('Histogram of ' + var)
    plt.show()


def compute_train_validation(inputs, outputs):
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    validationSample = [i for i in indexes if i not in trainSample]

    train_inputs = [inputs[i] for i in trainSample]
    train_outputs = [outputs[i] for i in trainSample]
    validation_inputs = [inputs[i] for i in validationSample]
    validation_outputs = [outputs[i] for i in validationSample]

    return train_inputs, train_outputs, validation_inputs, validation_outputs


def normalize(inputs):
    features_norm = []
    for i in range(len(features)):
        feat_norm = [ex[i] for ex in inputs]
        features_norm.append(normalisation_z(feat_norm, np.nanmean(feat_norm), np.nanstd(feat_norm)))

    [plot_data_histogram(features_norm[i], featureNames[i] + ' normalised') for i in range(len(featureNames))]

    return [[features_norm[0][i], features_norm[1][i], features_norm[2][i], features_norm[3][i]] for i in
            range(len(features_norm[0]))]


def normalize_digits(inputs):
    return [[inputs[i][j] / 255.0 for j in range(len(inputs[i]))] for i in range(len(inputs))]


def flatten(mat):
    x = []
    for line in mat:
        for el in line:
            x.append(el)
    return x


def one_hot_encoding(outputs):
    reformed_outputs = [[0] * (max(outputs) + 1) for _ in range(len(outputs))]
    for i in range(len(outputs)):
        reformed_outputs[i][outputs[i]] = 1
    return reformed_outputs


def one_hot_decoding(outputs):
    formed_outputs = [0 for _ in range(len(outputs))]
    for i in range(len(outputs)):
        formed_outputs[i] = outputs[i].index(max(outputs[i]))
    return formed_outputs


def compute_neural_network(train_inputs, train_outputs, validation_inputs, num_input, num_hidden, num_output,
                           activation_type, learning_rate, epochs, file):
    nn = NeuralNetwork(num_input, num_hidden, num_output, activation_type)
    nn.fit(train_inputs, train_outputs, learning_rate=learning_rate, epochs=epochs, file=file)
    return nn.predict(validation_inputs)


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


def accuracy_precision_recall(real_labels, computed_labels, label_values, label_names):
    cm = confusion_matrix(real_labels, computed_labels, label_values)
    accuracy = sum([1 if real_labels[i] == computed_labels[i] else 0
                    for i in range(0, len(real_labels))]) / len(real_labels)
    precision = {}
    recall = {}
    for lv, ln in zip(label_values, label_names):
        precision[ln] = cm[lv][lv] / sum(x[lv] for x in cm.values())
        recall[ln] = cm[lv][lv] / sum(x for x in cm[lv].values())
    return accuracy, precision, recall


# iris
print("IRIS:")
data = load_iris()
inputs = data['data']
outputs = data['target']
outputNames = data['target_names']
featureNames = list(data['feature_names'])
feature1 = [feat[featureNames.index('sepal length (cm)')] for feat in inputs]
feature2 = [feat[featureNames.index('sepal width (cm)')] for feat in inputs]
feature3 = [feat[featureNames.index('petal length (cm)')] for feat in inputs]
feature4 = [feat[featureNames.index('petal width (cm)')] for feat in inputs]
features = [feature1, feature2, feature3, feature4]
inputs = [[feat[featureNames.index('sepal length (cm)')], feat[featureNames.index('sepal width (cm)')],
           feat[featureNames.index('petal length (cm)')], feat[featureNames.index('petal width (cm)')]]
          for feat in inputs]
min_max = []

# plot the data distribution
[plot_data_histogram(features[i], featureNames[i]) for i in range(len(featureNames))]
plot_data_histogram(outputs, 'iris class')

# normalize data
inputs = normalize(inputs)

# compute train and validation data
TI, TO, VI, VO = compute_train_validation(inputs, outputs)

# display outputs as 0 (false) and 1 (true)
# 2 -> [0, 0, 1], 1 -> [0, 1, 0] (if there are only 3 output values)
NTO = one_hot_encoding(TO)

# compute ANN
computed = compute_neural_network(TI, NTO, VI, num_input=4, num_hidden=5, num_output=3, activation_type='swish',
                                  learning_rate=0.01, epochs=1000, file='erori_iris.txt')

# get back to initial form
CO = one_hot_decoding(computed)

# Predict accuracy, precision, recall
a, p, r = accuracy_precision_recall(VO, CO, [0, 1, 2], ['setosa', 'versicolor', 'virginica'])
print(f'Accuracy: {a}')
print(f'Precision: {p}')
print(f'Recall: {r}')

# digits
print("DIGITS:")
data = load_digits()
inputs_digits = data.images
outputs_digits = data['target']
outputNames_digits = data['target_names']

# flatten data
inputs_digits = [flatten(el) for el in inputs_digits]

# normalize data
inputs_digits = normalize_digits(inputs_digits)

# compute train and validation data
TI, TO, VI, VO = compute_train_validation(inputs_digits, outputs_digits)

# display outputs as 0 (false) and 1 (true)
NTO = one_hot_encoding(TO)

# compute ANN
computed = compute_neural_network(TI, NTO, VI, num_input=64, num_hidden=30, num_output=10, activation_type='identity',
                                  learning_rate=0.01, epochs=300, file='erori_digits.txt')

# get back to initial form
CO = one_hot_decoding(computed)

# Predict accuracy, precision, recall
a, p, r = accuracy_precision_recall(VO, CO, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                                    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
print(f'Accuracy: {a}')
print(f'Precision: {p}')
print(f'Recall: {r}')
