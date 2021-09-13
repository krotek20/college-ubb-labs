import math


col = []


def read():
    method = input("Method(iterative/recursive): ")
    if method not in ["iterative", "recursive"]:
        raise ValueError("invalid method: " + method)

    n = int(input("N = "))
    if n <= 1:
        raise ValueError("n should be greater than 1")

    my_list = []
    for i in range(n):
        x = float(input("x = "))
        y = float(input("y = "))
        point = (x, y)
        my_list.append(point)

    return method, my_list


def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))


def verif(x, y, z):
    a = dist(x, y)
    b = dist(y, z)
    c = dist(z, x)
    if a == b + c or b == a + c or c == b + a:
        return True
    return False


def coliniare(points):
    if len(points) < 3:
        return False
    for i in range(0, len(points)-2):
        for j in range(i+1, len(points)-1):
            for k in range(j+1, len(points)):
                if verif(points[i], points[j], points[k]):
                    col.append([i, j, k])


def consistent(rez):
    if len(rez) != len(set(rez)):
        return False
    for i in range(len(col)):
        if len(rez) < 3:
            if all(x in col[i] for x in rez):
                return True
        else:
            if all(x in rez for x in col[i]):
                return True
    return False


def solution(rez, dim):
    return 3 <= len(rez) <= dim


def solutionFound(rez, my_list):
    final_list = []
    for i in range(len(rez)):
        final_list.append(my_list[rez[i]])
    print(final_list)


def back_rec(rez, my_list, dim):
    rez.append(0)
    for i in range(0, dim):
        rez[-1] = i
        if consistent(rez):
            if solution(rez, dim):
                solutionFound(rez, my_list)
            back_rec(rez, my_list, dim)
    rez.pop()


def back_itr(my_list, dim):
    rez = [-1]
    while len(rez) > 0:
        choosed = False
        while not choosed and rez[-1] < dim - 1:
            rez[-1] = rez[-1] + 1  # increase the last component
            choosed = consistent(rez)
        if choosed:
            if solution(rez, dim):
                solutionFound(rez, my_list)
            rez.append(-1)  # expand candidate solution
        else:
            rez = rez[:-1]  # go back one component


def main():
    method, my_list = read()
    coliniare(my_list)
    if len(col) == 0:
        print("Nu exista puncte coliniare in lista!")
    else:
        if method == "recursive":
            back_rec([], my_list, len(my_list))
        if method == "iterative":
            back_itr(my_list, len(my_list))


main()
