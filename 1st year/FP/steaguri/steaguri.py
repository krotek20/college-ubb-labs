culori = ["alb", "galben", "rosu", "verde", "albastru", "negru"]


def consistent(sol):
    if len(sol) != 3:
        return False
    return True


def solutie(sol):
    if (culori[sol[1]] == "galben" or culori[sol[1]] == "verde") and len(sol) == len(set(sol)):
        return True
    return False


def solutieFound(sol):
    for i in range(3):
        print(culori[sol[i]] + " ")
    print()


def back(sol):
    sol.append(0)
    for i in range(0, 6):
        sol[-1] = i
        if consistent(sol):
            if solutie(sol):
                solutieFound(sol)
        else:
            back(sol)
    sol.pop()


back([])
