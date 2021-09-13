import random
import numpy as np


def shuffle(x):
    temp = list(zip(*x.values()))
    np.random.shuffle(temp)
    temp = list(zip(*temp))
    return {k: list(v) for k, v in zip(x, temp)}


class Regression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []
        self.partial_coef_ = []
        self.error_ = []
        self.keys = []
        self.dataset_length = 0

    def fit(self, x, y, learning_rate=0.0001, epochs=1000, for_plot=True):
        self.keys = [key for key in x.keys()]
        self.dataset_length = len(x[self.keys[0]])
        self.coef_ = [0.0 for _ in range(len(x) + 1)]
        self.partial_coef_ = [0.0 for _ in range(len(x) + 1)]
        self.error_ = [0.0 for _ in range(self.dataset_length)]
        # self.coef_ = [random.random() for _ in range(len(x) + 1)]

        errors = []
        for epoch in range(epochs):
            # x = shuffle(x)
            for i in range(self.dataset_length):
                computed = self.eval(x, i)
                self.error_[i] = computed - y[i]
            for i in range(self.dataset_length):
                for j in range(len(x)):
                    self.coef_[j] = self.coef_[j] - learning_rate * self.error_[i] * x[self.keys[j]][i]
                self.coef_[len(x)] = self.coef_[len(x)] - learning_rate * self.error_[i]

            # for printing
            error = 0
            for i in range(self.dataset_length):
                temp = self.eval(x, i)
                error += (y[i] - temp)
            errors.append(error)

        # for epoch in range(epochs):
        #     x = shuffle(x)
        #     for i in range(self.dataset_length):
        #         computed = self.eval(x, i)
        #         for j in range(len(x)):
        #             self.partial_coef_[j] += (1.0 / self.dataset_length) * ((computed - y[i]) * x[self.keys[j]][i])
        #         self.partial_coef_[len(x)] += (1.0 / self.dataset_length) * (computed - y[i])
        #     for j in range(len(x) + 1):
        #         self.coef_[j] = self.coef_[j] - (learning_rate * self.partial_coef_[j])
        #
        #     # for printing
        #     error = 0
        #     for i in range(self.dataset_length):
        #         temp = self.eval(x, i)
        #         error += (y[i] - temp)
        #     errors.append(error)

        if for_plot is True:
            with open('erori.txt', 'w') as fout:
                for error in errors:
                    fout.write(str(error) + '\n')

        self.intercept_ = self.coef_[len(x)]
        self.coef_ = self.coef_[:len(x)]

    def eval(self, x, i):
        yi = self.coef_[-1]
        for j in range(len(x)):
            yi += self.coef_[j] * x[self.keys[j]][i]
        return yi

    def predict(self, x):
        return [self.eval(x, i) for i in range(len(x[self.keys[0]]))]
