def eliminate(r1, r2, col, target=0):
    fac = (r2[col] - target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]


def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i + 1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i + 1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a


def inverse(a):
    tmp = [[] for _ in a]
    for i, row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0] * i + [1] + [0] * (len(a) - i - 1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i]) // 2:])
    return ret


def matrix_multiply(x, y):
    rows_x = len(x)
    cols_x = len(x[0])
    # rows_y = len(y)
    if isinstance(y[0], list):
        cols_y = len(y[0])
    else:
        cols_y = 1

    C = zeros_matrix(rows_x, cols_y)
    for i in range(rows_x):
        for j in range(cols_y):
            total = 0
            for k in range(cols_x):
                total += x[i][k] * y[k][j]
            C[i][j] = total

    return C


def multiply_matrices(matrix_list):
    matrix_product = matrix_list[0]
    for matrix in matrix_list[1:]:
        matrix_product = matrix_multiply(matrix_product, matrix)
    return matrix_product


def zeros_matrix(rows, cols):
    x = []
    while len(x) < rows:
        x.append([])
        while len(x[-1]) < cols:
            x[-1].append(0.0)
    return x


def transpose(x):
    if not isinstance(x[0], list):
        x = [x]
    rows = len(x)
    cols = len(x[0])
    xT = zeros_matrix(cols, rows)
    for i in range(rows):
        for j in range(cols):
            xT[j][i] = x[i][j]
    return xT
