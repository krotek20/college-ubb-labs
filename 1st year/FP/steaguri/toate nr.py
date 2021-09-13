def consistent(sol):
    if len(sol) != k:
        return False
    return True


def solutie(sol):
    if len(sol) != len(set(sol)):
        return False
    for i in range(k-1):
        if sol[i] > sol[i+1]:
            return False
    return True


def solutieFound(sol):
    print(*sol)


def back(sol):
    sol.append(0)
    for i in range(1, n+1):
        sol[-1] = i
        if consistent(sol):
            if solutie(sol):
                solutieFound(sol)
        else:
            back(sol)
    sol.pop()


n = int(input("n="))
k = int(input("k="))
back([])
