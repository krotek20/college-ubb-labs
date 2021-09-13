from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

from normalisation import normalisation_min_max, normalisation_z, normalisation_log
from kmeans import Kmeans


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


def compute_kmeans(train_inputs, validation_inputs, validation_outputs, epochs, n_clusters, n_features):
    nn = Kmeans(n_clusters=n_clusters, n_features=n_features)
    nn.fit(train_inputs, epochs=epochs)

    # store silhouette coefs
    with open("silhouette.txt", 'w') as fout:
        for coef in nn.coef_silhouette:
            fout.write(str(coef) + '\n')

    computed = nn.predict(validation_inputs)
    returned_computed = [-1 for _ in range(len(computed))]
    for i in range(n_clusters):
        groups = [0 for _ in range(n_clusters)]
        for j in range(len(computed)):
            groups[validation_outputs[j]] += 1 if computed[j] == i else 0
        cluster = groups.index(max(groups))
        for j in range(len(computed)):
            if computed[j] == i:
                returned_computed[j] = cluster
    return returned_computed


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
        try:
            precision[ln] = cm[lv][lv] / sum(x[lv] for x in cm.values())
        except ZeroDivisionError:
            precision[ln] = 0.0
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

# compute kmeans
CO = compute_kmeans(TI, VI, VO, epochs=100, n_clusters=3, n_features=4)

# Predict accuracy, precision, recall
a, p, r = accuracy_precision_recall(VO, CO, [0, 1, 2], ['setosa', 'versicolor', 'virginica'])
print(f'Accuracy: {a}')
print(f'Precision: {p}')
print(f'Recall: {r}')
