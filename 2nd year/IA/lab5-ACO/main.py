from Edge import Edge
from Ant import Ant


class ACO:
    def __init__(self, mode, network, alpha=1.5, beta=3.0, initial_pheromone=1.0):
        self.mode = mode
        self.network = network
        self.num_nodes = len(network)

        self.rho = 0.1
        self.iterations = 100
        self.colony_size = 40
        self.min_factor = 0.001

        self.edges = [[None] * self.num_nodes for _ in range(self.num_nodes)]
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                self.edges[i][j] = self.edges[j][i] = Edge(i, j, self.network[i][j], initial_pheromone)
        self.ants = [Ant(alpha, beta, self.num_nodes, self.edges) for _ in range(self.colony_size)]

        self.best_route = None
        self.best_distance = float("inf")
        self.distances = None

    def place_pheromone(self, route, distance):
        pheromone_to_place = 1.0 / distance
        for i in range(self.num_nodes):
            self.edges[route[i]][route[(i + 1) % self.num_nodes]].pheromone += pheromone_to_place

    def acs(self):
        self.distances = []
        for iteration in range(self.iterations):
            local_best_distance = float("inf")
            for ant in self.ants:
                self.place_pheromone(ant.find_route(), ant.get_distance())
                if ant.distance < local_best_distance:
                    local_best_distance = ant.distance
                if ant.distance < self.best_distance:
                    self.best_route = ant.route
                    self.best_distance = ant.distance
            self.distances.append(local_best_distance)
            for i in range(self.num_nodes):
                for j in range(i + 1, self.num_nodes):
                    self.edges[i][j].pheromone *= (1.0 - self.rho)

    def mmas(self):
        self.distances = []
        for iteration in range(self.iterations):
            local_best_route = None
            local_best_distance = float("inf")
            for ant in self.ants:
                ant.find_route()
                if ant.get_distance() < local_best_distance:
                    local_best_route = ant.route
                    local_best_distance = ant.distance
            if float(iteration + 1) / float(self.iterations) <= 0.75:
                self.place_pheromone(local_best_route, local_best_distance)
                max_pheromone = 1.0 / local_best_distance
            else:
                if local_best_distance < self.best_distance:
                    self.best_route = local_best_route
                    self.best_distance = local_best_distance
                self.place_pheromone(self.best_route, self.best_distance)
                max_pheromone = 1.0 / self.best_distance
            self.distances.append(local_best_distance)
            min_pheromone = max_pheromone * self.min_factor
            for i in range(self.num_nodes):
                for j in range(i + 1, self.num_nodes):
                    self.edges[i][j].pheromone *= (1.0 - self.rho)
                    if self.edges[i][j].pheromone > max_pheromone:
                        self.edges[i][j].pheromone = max_pheromone
                    elif self.edges[i][j].pheromone < min_pheromone:
                        self.edges[i][j].pheromone = min_pheromone

    def run(self):
        print('{0}:'.format(self.mode))
        if self.mode == 'ACS':
            self.acs()
            with open("acs_distances.txt", "w") as fout:
                for distance in self.distances:
                    fout.write(str(distance) + '\n')
        else:
            self.mmas()
            with open("mmas_distances.txt", "w") as fout:
                for distance in self.distances:
                    fout.write(str(distance) + '\n')
        print('Best route: {0}\nDistance: {1}\n'.format(', '.join(str(i + 1) for i in self.best_route),
                                                        round(self.best_distance, 2)))


def read_network(file_name):
    with open(file_name, "r") as fin:
        length = int(fin.readline())
        tsp = []
        for i in range(length):
            row = [float(num) for num in fin.readline().split(',')]
            tsp.append(row)
    return tsp


if __name__ == '__main__':
    _network = read_network("berlin52_formalised.txt")
    acs = ACO(mode='ACS', network=_network)
    acs.run()
    max_min = ACO(mode='MMAS', network=_network)
    max_min.run()
