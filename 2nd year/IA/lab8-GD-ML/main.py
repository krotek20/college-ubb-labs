import matplotlib.pyplot as plt
import random
import normalisation
from sklearn.datasets import load_linnerud
from GD_batch import Regression


def read_data(file_name, input_vars, output_vars):
    import csv

    data = []
    data_names = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for line in csv_reader:
            if line_count == 0:
                data_names = line
            else:
                data.append(line)
            line_count += 1

    returned_inputs = {}
    for var in input_vars:
        selected_variable = data_names.index(var)
        returned_inputs[var] = [float(data[i][selected_variable]) for i in range(len(data))]
    selected_output = data_names.index(output_vars)
    returned_outputs = [float(data[i][selected_output]) for i in range(len(data))]

    return returned_inputs, returned_outputs


def plot_data_histogram(x, var):
    n, bins, patches = plt.hist(x, 10)
    plt.title('Histogram of ' + var)
    plt.show()


def make_train_validation(dict_inputs, listed_outputs):
    keys = [key for key in dict_inputs.keys()]
    indexes = [i for i in range(len(dict_inputs[keys[0]]))]
    train_sample = []
    for i in range(int(0.8 * len(dict_inputs[keys[0]]))):
        index = indexes[random.randint(0, len(indexes) - 1)]
        train_sample.append(index)
        indexes.remove(index)
    validation_sample = indexes[:]

    train_inputs = {}
    validation_inputs = {}
    for k, v in dict_inputs.items():
        train_inputs[k] = [v[i] for i in train_sample]
        validation_inputs[k] = [v[i] for i in validation_sample]

    if isinstance(listed_outputs[0], list):
        train_outputs = [[listed_outputs[j][i] for i in train_sample] for j in range(len(listed_outputs))]
        validation_outputs = [[listed_outputs[j][i] for i in validation_sample] for j in range(len(listed_outputs))]
    else:
        train_outputs = [listed_outputs[i] for i in train_sample]
        validation_outputs = [listed_outputs[i] for i in validation_sample]
    return train_inputs, train_outputs, validation_inputs, validation_outputs


def plot_train_validation(inputs, outputs):
    TI, TO, VI, VO = make_train_validation(inputs, outputs)
    keys = [key for key in inputs.keys()]

    if len(inputs) > 1:
        ax = plt.axes(projection='3d')
        ax.plot3D(TI[keys[0]], TI[keys[1]], TO, 'ro', label='training data')
        ax.plot3D(VI[keys[0]], VI[keys[1]], VO, 'g^', label='validation data')
        plt.title('train and validation data')
        ax.set_xlabel('GDP capita')
        ax.set_ylabel('Freedom')
        ax.set_zlabel('Happiness')
    else:
        plt.plot(TI[keys[0]], TO, 'ro', label='training data')
        plt.plot(VI[keys[0]], VO, 'g^', label='testing data')
        plt.title('train and test data')
        plt.xlabel('GDP capita')
        plt.ylabel('happiness')

    plt.legend()
    plt.show()
    return TI, TO, VI, VO


def plot_learnt_model_bivariate(w, train_inputs, train_outputs):
    import numpy as np

    keys = [key for key in inputs.keys()]
    xref = np.linspace(min(train_inputs[keys[0]]), max(train_inputs[keys[0]]), 1000)
    yref = np.linspace(min(train_inputs[keys[1]]), max(train_inputs[keys[1]]), 1000)
    x_surf, y_surf = np.meshgrid(xref, yref)
    zref = []
    for el2 in range(len(yref)):
        for el in range(len(xref)):
            zref.append([w[0] + w[1] * xref[el] + w[2] * yref[el2]])
    z_vals = np.array(zref)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(train_inputs[keys[0]], train_inputs[keys[1]], train_outputs, label='train data')
    ax.plot_surface(x_surf, y_surf, z_vals.reshape(x_surf.shape), color='None', alpha=0.3)
    plt.legend()
    plt.xlabel('gdp capita')
    plt.ylabel('freedom')
    plt.title('train data and model')
    plt.show()


def plot_learnt_model_univariate(W, train_inputs, train_outputs):
    noOfPoints = 1000
    xref = []
    keys = [key for key in train_inputs.keys()]
    val = min(train_inputs[keys[0]])
    step = (max(train_inputs[keys[0]]) - min(train_inputs[keys[0]])) / noOfPoints
    for i in range(1, noOfPoints):
        xref.append(val)
        val += step
    yref = [W[0] + W[1] * el for el in xref]

    plt.plot(train_inputs[keys[0]], train_outputs, 'ro', label='training data')
    plt.plot(xref, yref, 'b-', label='learnt model')
    plt.title('train data and the learnt model')
    plt.xlabel(keys[0])
    plt.ylabel('happiness')
    plt.legend()
    plt.show()


def compute_gd_batch(train_inputs, train_outputs):
    regressor = Regression()
    regressor.fit(train_inputs, train_outputs)

    w = [regressor.intercept_]
    for coef in regressor.coef_:
        w.append(coef)
    print(f'the learnt model: f(x) = {regressor.intercept_}', end='')
    for i in range(len(regressor.coef_)):
        print(f' + {regressor.coef_[i]} * x{i + 1}', end='')
    print()

    # plot_learnt_model_univariate(w, train_inputs, train_outputs)
    plot_learnt_model_bivariate(w, train_inputs, train_outputs)
    return regressor


def lets_predict(regressor, validation_inputs, validation_outputs):
    keys = [key for key in validation_inputs.keys()]
    computed_validation_outputs = regressor.predict(validation_inputs)

    # univariate
    if len(keys) == 1:
        plt.plot(validation_inputs[keys[0]], computed_validation_outputs, 'yo',
                 label='computed test data')
        plt.plot(validation_inputs[keys[0]], validation_outputs, 'g^', label='real test data')
        plt.title('computed test and real test data')
        plt.xlabel(keys[0])
        plt.ylabel('happiness')
        plt.legend()
        plt.show()

    # bivariate
    else:
        ax = plt.axes(projection='3d')
        ax.plot3D(validation_inputs[keys[0]], validation_inputs[keys[1]], computed_validation_outputs, 'yo',
                  label='computed test data')
        ax.plot3D(validation_inputs[keys[0]], validation_inputs[keys[1]], validation_outputs, 'g^',
                  label='real test data')
        plt.title('Computed validation and real validation data')
        ax.set_xlabel(keys[0])
        ax.set_ylabel(keys[1])
        ax.set_zlabel('Happiness')
        plt.legend()
        plt.show()

    return computed_validation_outputs


def prediction_error(computed_validation_outputs, validation_outputs):
    error = 0.0
    for t1, t2 in zip(computed_validation_outputs, validation_outputs):
        error += (t1 - t2) ** 2
    error = error / len(validation_outputs)
    print('Prediction error: ', error)

    # by using sklearn
    # from sklearn.metrics import mean_squared_error
    #
    # error = mean_squared_error(validation_outputs, computed_validation_outputs)
    # print('prediction error (tool):  ', error)


def transform_data(inputs, outputs):
    dict_inputs = {}
    listed_outputs = []
    for i in range(len(inputs[0])):
        dict_inputs[i] = []
        listed_outputs.append([])
        for j in range(len(inputs)):
            dict_inputs[i].append(inputs[j][i])
            listed_outputs[-1].append(outputs[j][i])
    return make_train_validation(dict_inputs, listed_outputs)


def compute_multi_target_regression(train_inputs, train_outputs):
    regressors = []
    for output_set in train_outputs:
        regressor = Regression()
        regressor.fit(train_inputs, output_set, for_plot=False)
        regressors.append(regressor)
    return regressors


def predict_multi_target(regressors, validation_inputs):
    computed_validation_outputs = []
    for regressor in regressors:
        computed_validation_outputs.append(regressor.predict(validation_inputs))
    return computed_validation_outputs


def prediction_error_multi_target(computed_validation_outputs, validation_outputs):
    from math import sqrt

    return sqrt(sum([x ** 2 for x in [sqrt(sum(
        (real - computed) ** 2 for real, computed in zip(validation_outputs[i], computed_validation_outputs[i])) / len(
        validation_outputs[i])) for i in range(len(validation_outputs))]]) / len(validation_outputs))


input_labels = ['Economy..GDP.per.Capita.', 'Freedom']
inputs, outputs = read_data('world-happiness-report-2017.csv', input_labels, 'Happiness.Score')
print(inputs)
print(outputs)
print()

# plot data
[plot_data_histogram(v, k) for k, v in inputs.items()]
plot_data_histogram(outputs, 'Happiness score')

# plot train and validation data
TI, TO, VI, VO = plot_train_validation(inputs, outputs)

# normalize train and validation data
minim = [min(TI[key]) for key in TI.keys()]
maxim = [max(TI[key]) for key in TI.keys()]
# keys = [key for key in TI.keys()]
# mean = [sum(TI[key]) / len(TI[key]) for key in TI.keys()]
# std = [(1.0 / len(TI[keys[i]]) * sum([(d - mean[i]) ** 2 for d in TI[keys[i]]])) ** 0.5 for i in range(len(keys))]
TI = normalisation.normalisation_min_max(TI, minim, maxim)
VI = normalisation.normalisation_min_max(VI, minim, maxim)

# compute w = [w0, w1, ...] and then predict
CVO = lets_predict(compute_gd_batch(TI, TO), VI, VO)

# predict error
prediction_error(CVO, VO)

# Multi-target regression
print()
print('Starting multi-target regression ...')
X, y = load_linnerud(return_X_y=True)
TI, TO, VI, VO = transform_data(X, y)
TI = normalisation.normalisation_log(TI)
VI = normalisation.normalisation_log(VI)
CVO = predict_multi_target(compute_multi_target_regression(TI, TO), VI)
print('Prediction loss for multi-target: ', prediction_error_multi_target(CVO, VO))
