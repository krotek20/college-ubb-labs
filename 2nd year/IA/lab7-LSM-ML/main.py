import matplotlib.pyplot as plt
import Regression


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


def plot_train_validation(inputs, outputs):
    import random

    keys = []
    for key in inputs.keys():
        keys.append(key)
    indexes = [i for i in range(len(inputs[keys[0]]))]
    train_sample = []
    for i in range(int(0.8 * len(inputs[keys[0]]))):
        index = indexes[random.randint(0, len(indexes) - 1)]
        train_sample.append(index)
        indexes.remove(index)

    validation_sample = indexes[:]

    train_inputs = {}
    validation_inputs = {}
    for k, v in inputs.items():
        train_inputs[k] = [v[i] for i in train_sample]
        validation_inputs[k] = [v[i] for i in validation_sample]

    train_outputs = [outputs[i] for i in train_sample]
    validation_outputs = [outputs[i] for i in validation_sample]

    ax = plt.axes(projection='3d')
    ax.plot3D(train_inputs[keys[0]], train_inputs[keys[1]], train_outputs, 'ro', label='training data')
    ax.plot3D(validation_inputs[keys[0]], validation_inputs[keys[1]], validation_outputs, 'g^', label='validation data')
    plt.title('train and validation data')
    ax.set_xlabel('GDP capita')
    ax.set_ylabel('Freedom')
    ax.set_zlabel('Happiness')
    plt.legend()
    plt.show()
    return train_inputs, train_outputs, validation_inputs, validation_outputs


def plot_learnt_model(w, train_inputs, train_outputs):
    import numpy as np

    keys = []
    for key in inputs.keys():
        keys.append(key)
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


def compute(train_inputs, train_outputs):
    from sklearn import linear_model

    # transformed_inputs = [[train_inputs[k][i] for k in train_inputs.keys()] for i in range(len(train_outputs))]
    # regressor = linear_model.LinearRegression()
    # regressor.fit(transformed_inputs, train_outputs)
    regressor = Regression.Regression()
    regressor.fit(train_inputs, train_outputs)

    w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
    w = [w0, w1, w2]
    print('the learnt model: f(x) = ', w0, ' + ', w1, ' * x1 + ', w2, ' * x2')

    plot_learnt_model(w, train_inputs, train_outputs)
    return regressor


def lets_predict(regressor, validation_inputs, validation_outputs):
    keys = [key for key in validation_inputs.keys()]
    computed_validation_outputs = regressor.predict(validation_inputs)

    ax = plt.axes(projection='3d')
    ax.plot3D(validation_inputs[keys[0]], validation_inputs[keys[1]], computed_validation_outputs, 'yo',
              label='computed test data')
    ax.plot3D(validation_inputs[keys[0]], validation_inputs[keys[1]], validation_outputs, 'g^',
              label='real test data')
    plt.title('Computed validation and real validation data')
    ax.set_xlabel('GDP capita')
    ax.set_ylabel('Freedom')
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


input_labels = ['Economy..GDP.per.Capita.', 'Freedom']
inputs, outputs = read_data('world-happiness-report-2017.csv', input_labels, 'Happiness.Score')
print(inputs)
print(outputs)
print()

# plot data
[plot_data_histogram(v, k) for k, v in inputs.items()]
plot_data_histogram(outputs, 'Happiness score')

# plot train and validation
TI, TO, VI, VO = plot_train_validation(inputs, outputs)

# compute w = [w0, w1, ...] and then predict
CVO = lets_predict(compute(TI, TO), VI, VO)

# predict error
prediction_error(CVO, VO)
