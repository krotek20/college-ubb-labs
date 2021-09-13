from GA import GA


def fitness(route, adj_matrix):
    fit = 0
    for i in range(len(route)):
        if i + 1 == len(route):
            fit += adj_matrix[route[i]][route[0]]
        else:
            fit += adj_matrix[route[i]][route[i + 1]]
    return fit


def read_network(file_name):
    with open(file_name, "r") as fin:
        length = int(fin.readline())
        tsp = []
        for i in range(length):
            row = [int(num) for num in fin.readline().split(',')]
            tsp.append(row)
    return tsp


def solve(file_name):
    # seed(1)

    # reading network
    network = read_network(file_name)
    # initialise GA parameters
    ga_param = {
        'pop_size': 100,
        'no_gen': 3000,
        'rm': 0.6
    }
    # problem parameters
    probl_param = {
        'network': network,
        'function': fitness,
        'rm': 0.01
    }

    ga = GA(ga_param, probl_param)
    ga.initialisation()
    ga.evaluation()

    best_chromosome = ga.best_chromosome()
    global_best_chromosome = best_chromosome
    all_fitnesses = []

    for g in range(ga_param['no_gen']):
        # logic alg
        ga.one_generation()
        best_chromosome = ga.best_chromosome()
        if best_chromosome.fitness < global_best_chromosome.fitness:
            global_best_chromosome = best_chromosome
            print('Best solution in generation ' + str(g) + ' is: ' + str(best_chromosome.repres) + ' f(x) = '
                  + str(best_chromosome.fitness))
            all_fitnesses.append(best_chromosome.fitness)

    with open("fitness.txt", "w") as fout:
        for fit in all_fitnesses:
            fout.write(str(fit) + '\n')

    # print output values
    print("Best " + str(global_best_chromosome))
    repres = [0, 24, 23, 22, 25, 21, 20, 16, 17, 19, 18, 15, 10, 11, 12, 14, 13, 9, 8, 7, 6, 4, 5, 3, 2, 1]

    print(fitness(repres, network))


if __name__ == '__main__':
    solve("hard_01_tsp.txt")
