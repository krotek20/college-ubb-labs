from math import exp


def sigmoid(x):
    return 1 / (1 + exp(-x))


class LogisticRegression:
    def __init__(self):
        self.coef_ = []

    def fit(self, x, y, learning_rate=0.001, epochs=1000, reg=0):
        self.coef_ = [0.0 for _ in range(1 + len(x[0]))]
        print_errors = []
        # self.coef_ = [random.random() for _ in range(len(x[0]) + 1)]
        for epoch in range(epochs):
            errors = [sigmoid(self.eval(x[i])) - y[i] for i in range(len(x))]
            for i in range(len(x)):
                for j in range(len(x[0])):
                    self.coef_[j] = self.coef_[j] - learning_rate * errors[i] * x[i][j]
                self.coef_[len(x[0])] = self.coef_[len(x[0])] - learning_rate * errors[i]

            # for printing
            error = 0
            for i in range(len(x)):
                temp = sigmoid(self.eval(x[i]))
                error += (temp - y[i])
            print_errors.append(error)

        with open(f'erori{reg}.txt', 'a') as fout:
            for error in print_errors:
                fout.write(str(error) + '\n')

    def eval(self, xi):
        yi = self.coef_[len(xi)]
        for j in range(len(xi)):
            yi += self.coef_[j] * xi[j]
        return yi

    def probability(self, test_inputs):
        return [sigmoid(self.eval(sample)) for sample in test_inputs]

    def predict(self, test_inputs, threshold=0.5):
        return [0 if sigmoid(self.eval(sample)) < threshold else 1 for sample in test_inputs]
