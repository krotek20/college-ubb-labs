import networkx
from random import seed

from GA import GA


def modularity(communities, param):
    no_nodes = param['no_nodes']
    mat = param['mat']
    degrees = param['degrees']
    no_edges = param['no_edges']
    m = 2 * no_edges
    q = 0.0
    for i in range(0, no_nodes):
        for j in range(0, no_nodes):
            if communities[i] == communities[j]:
                q += (mat[i][j] - degrees[i] * degrees[j] / m)
    return - q * 1 / m


def read_network(file_name):
    returned_network = {}
    network = networkx.read_gml(file_name, label="id")
    returned_network['no_nodes'] = len(network.nodes())
    matrix = []
    for i in range(returned_network['no_nodes']):
        matrix.append([])
        for j in range(returned_network['no_nodes']):
            matrix[-1].append(0)
    for source, dest in network.edges():
        matrix[source][dest] = matrix[dest][source] = 1
    returned_network['mat'] = matrix
    degrees = []
    no_edges = 0
    for i in range(returned_network['no_nodes']):
        d = 0
        for j in range(returned_network['no_nodes']):
            if matrix[i][j] == 1:
                d += 1
            if j > i:
                no_edges += matrix[i][j]
        degrees.append(d)
    returned_network['no_edges'] = no_edges
    returned_network['degrees'] = degrees
    return returned_network


def get_actual_communities(repres):
    returned_repres = {}
    for i in range(len(repres)):
        returned_repres[repres[i]] = returned_repres.get(repres[i], set())
        returned_repres[repres[i]].add(i)
    return returned_repres


def solve(file_name):
    # seed(1)

    # reading network
    network = read_network(file_name)
    # initialise GA parameters
    ga_param = {
        'pop_size': 100,
        'no_gen': 500
    }
    # problem parameters
    probl_param = {
        'network': network,
        'function': modularity,
        'no_dim': network['no_nodes']
    }

    ga = GA(ga_param, probl_param)
    ga.initialisation()
    ga.evaluation()

    best_chromosome = ga.best_chromosome()
    global_best_chromosome = best_chromosome
    all_fitnesses = []

    for g in range(ga_param['no_gen']):
        # logic alg
        ga.one_generation_elitism()
        best_chromosome = ga.best_chromosome()
        if best_chromosome.fitness < global_best_chromosome.fitness:
            global_best_chromosome = best_chromosome
            print('Best solution in generation ' + str(g) + ' is: ' + str(best_chromosome.repres) + ' f(x) = '
                  + str(best_chromosome.fitness))
            all_fitnesses.append(best_chromosome.fitness)

    with open("fitness.txt", "w") as fout:
        for fitness in all_fitnesses:
            fout.write(str(fitness) + '\n')

    # print output values
    communities = get_actual_communities(global_best_chromosome.repres)
    print(global_best_chromosome.fitness)
    print(len(communities))
    print(communities)


if __name__ == '__main__':
    solve("dolphins.gml")
