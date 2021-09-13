import random
import math


def initialize_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def soft_max(o_sums):
    all_sum = 0.0
    for i in range(len(o_sums)):
        all_sum = all_sum + math.exp(o_sums[i])
    result = [0 for _ in range(len(o_sums))]
    for i in range(len(o_sums)):
        result[i] = math.exp(o_sums[i]) / all_sum
    return result


class NeuralNetwork:
    def __init__(self, num_input, num_hidden, num_output, activation_type):
        self.num_input = num_input
        self.num_hidden = num_hidden
        self.num_output = num_output

        self.inputs = [0 for _ in range(num_input)]
        self.ih_weights = initialize_matrix(num_input, num_hidden)

        self.h_outputs = [0 for _ in range(num_hidden)]
        self.ho_weights = initialize_matrix(num_hidden, num_output)

        self.outputs = [0 for _ in range(num_output)]

        self.activation_type = activation_type

        self.initialize_weights()

    def set_weights(self, weights):
        k = 0
        for i in range(self.num_input):
            for j in range(self.num_hidden):
                self.ih_weights[i][j] = weights[k]
                k += 1
        for i in range(self.num_hidden):
            for j in range(self.num_output):
                self.ho_weights[i][j] = weights[k]
                k += 1

    def initialize_weights(self):
        num_wts = ((self.num_input * self.num_hidden) + (self.num_hidden * self.num_output))
        wts = [random.random() for _ in range(num_wts)]
        self.set_weights(wts)

    def activation_function(self, h_sum):
        if self.activation_type == 'swish':
            return (1.25 * h_sum) / (1.0 - math.exp(-h_sum))
        else:
            return h_sum

    def get_computed_outputs(self, x_values):
        h_sums = [0 for _ in range(self.num_hidden)]
        o_sums = [0 for _ in range(self.num_output)]

        for i in range(self.num_hidden):
            for j in range(self.num_input):
                h_sums[i] += (x_values[j] * self.ih_weights[j][i])

        for i in range(self.num_hidden):
            self.h_outputs[i] = self.activation_function(h_sums[i])

        for j in range(self.num_output):
            for i in range(self.num_hidden):
                o_sums[j] += (self.h_outputs[i] * self.ho_weights[i][j])

        soft_out = soft_max(o_sums)
        self.outputs = [soft_out[i] for i in range(self.num_output)]

        return [self.outputs[i] for i in range(self.num_output)]

    def fit(self, train_inputs, train_outputs, learning_rate, epochs, file):
        h_errors = [0 for _ in range(self.num_hidden)]
        sequence = [i for i in range(len(train_inputs))]
        losses = []

        for _ in range(epochs):
            random.shuffle(sequence)
            printing_loss = 0.0
            for i in range(len(train_inputs)):
                index = sequence[i]
                x_values = [train_inputs[index][j] for j in range(self.num_input)]
                y_values = [train_outputs[index][j] for j in range(self.num_output)]
                self.get_computed_outputs(x_values)

                printing_loss += sum([((y_values[j] - self.outputs[j]) ** 2) / 2.0 for j in range(self.num_output)])

                # ----- back-propagation -----
                # compute output errors
                if self.activation_type == 'swish':
                    o_errors = [
                        (self.outputs[j] + (1.0 / (1.0 + math.exp(-self.outputs[j]))) * (1.25 - self.outputs[j])) * (
                                y_values[j] - self.outputs[j]) for j in range(self.num_output)]
                else:
                    o_errors = [(y_values[j] - self.outputs[j]) for j in range(self.num_output)]
                    # o_errors = [(1 - self.outputs[j]) * self.outputs[j] * (y_values[j] - self.outputs[j]) for j in
                    #             range(self.num_output)]

                # compute hidden errors
                for j in range(self.num_hidden):
                    holder = 0
                    for k in range(self.num_output):
                        holder += o_errors[k] * self.ho_weights[j][k]
                    h_errors[j] = (1 - self.h_outputs[j]) * self.h_outputs[j] * holder

                # update input-hidden weights
                for j in range(self.num_input):
                    for k in range(self.num_hidden):
                        self.ih_weights[j][k] += learning_rate * h_errors[k] * self.inputs[j]

                # update hidden-output weights
                for j in range(self.num_hidden):
                    for k in range(self.num_output):
                        self.ho_weights[j][k] += learning_rate * o_errors[k] * self.h_outputs[j]

            losses.append(printing_loss)

        with open(file, 'w') as fout:
            for loss in losses:
                fout.write(str(loss) + '\n')

    def predict(self, test_data):
        computed = []
        for i in range(len(test_data)):
            x_values = [test_data[i][j] for j in range(self.num_input)]
            computed.append(self.get_computed_outputs(x_values))
        return computed
