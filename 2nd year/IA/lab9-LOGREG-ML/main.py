from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC

from logistic_regression import LogisticRegression
from normalisation import normalisation_min_max, normalisation_z, normalisation_log

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


def plot_data_histogram(x, var):
    n, bins, patches = plt.hist(x, 10)
    plt.title('Histogram of ' + var)
    plt.show()


def compute_train_validation():
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    validationSample = [i for i in indexes if i not in trainSample]

    train_inputs = [inputs[i] for i in trainSample]
    train_outputs = [outputs[i] for i in trainSample]
    validation_inputs = [inputs[i] for i in validationSample]
    validation_outputs = [outputs[i] for i in validationSample]

    return train_inputs, train_outputs, validation_inputs, validation_outputs


def normalise(inputs, train=True):
    features_norm = []
    for i in range(len(features)):
        feat_norm = [ex[i] for ex in inputs]
        features_norm.append(normalisation_z(feat_norm, np.nanmean(feat_norm), np.nanstd(feat_norm)))

    [plot_data_histogram(features_norm[i], featureNames[i] + ' normalised') for i in range(len(featureNames))]

    return [[features_norm[0][i], features_norm[1][i], features_norm[2][i], features_norm[3][i]] for i in
            range(len(features_norm[0]))]


def compute_logistic_regression(train_inputs, train_outputs, validation_inputs):
    # ovr = OneVsRestClassifier(LinearSVC(random_state=0))
    # pred = ovr.fit(train_inputs, train_outputs).predict(validation_inputs)
    # return pred
    computed = []
    probabilities = []
    for i in range(len(outputNames)):
        binary_train = [1 if train_outputs[j] == i else 0 for j in range(len(train_outputs))]
        regressor = LogisticRegression()
        regressor.fit(train_inputs, binary_train, reg=i)
        probabilities.append(regressor.probability(validation_inputs))

    for i in range(len(probabilities[0])):
        best = 0.0
        k = 0
        for j in range(len(probabilities)):
            if probabilities[j][i] > best:
                best = probabilities[j][i]
                k = j
        computed.append(k)

    return computed


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


# plot the data distribution
[plot_data_histogram(features[i], featureNames[i]) for i in range(len(featureNames))]
plot_data_histogram(outputs, 'iris class')

inputs = normalise(inputs)

# compute train and validation data
TI, TO, VI, VO = compute_train_validation()

# compute logistic regression
computed = compute_logistic_regression(TI, TO, VI)

# Predict accuracy, precision, recall
a, p, r = accuracy_precision_recall(VO, computed, [0, 1, 2], ['setosa', 'versicolor', 'virginica'])
print(f'Accuracy: {a}')
print(f'Precision: {p}')
print(f'Recall: {r}')
