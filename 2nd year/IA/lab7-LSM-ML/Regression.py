from MatrixHandler import inverse, matrix_multiply, multiply_matrices, transpose


class Regression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []

    def fit(self, x, y):
        transformed_X = [[1.0] + [x[k][i] for k in x.keys()] for i in range(len(y))]

        transpose_X = transpose(transformed_X)
        mul_X = matrix_multiply(transpose_X, transformed_X)
        inverted_X = inverse(mul_X)
        W = multiply_matrices([inverted_X, transpose_X, [[yy] for yy in y]])
        self.intercept_, self.coef_ = W[0][0], [W[1][0], W[2][0]]

    def predict(self, x):
        keys = [key for key in x.keys()]
        return [self.intercept_ + self.coef_[0] * x1 + self.coef_[1] * x2 for x1, x2 in zip(x[keys[0]], x[keys[1]])]
