import random


class Ant:
    def __init__(self, alpha, beta, num_nodes, edges):
        self.alpha = alpha
        self.beta = beta
        self.num_nodes = num_nodes
        self.edges = edges
        self.route = []
        self.distance = 0.0

    def next_node(self):
        total = 0.0
        roulette = 0.0
        unvisited_nodes = [node for node in range(self.num_nodes) if node not in self.route]
        for unvisited_node in unvisited_nodes:
            total += self.edges[self.route[-1]][unvisited_node].weight
        for unvisited_node in unvisited_nodes:
            roulette += self.edges[self.route[-1]][unvisited_node].pheromone ** self.alpha * \
                        (total / self.edges[self.route[-1]][unvisited_node].weight) ** self.beta
        random_value = random.uniform(0.0, roulette)
        pos = 0.0
        for unvisited_node in unvisited_nodes:
            pos += self.edges[self.route[-1]][unvisited_node].pheromone ** self.alpha * \
                    (total / self.edges[self.route[-1]][unvisited_node].weight) ** self.beta
            if pos >= random_value:
                return unvisited_node

    def find_route(self):
        self.route = [random.randint(0, self.num_nodes - 1)]
        while len(self.route) < self.num_nodes:
            self.route.append(self.next_node())
        return self.route

    def get_distance(self):
        self.distance = 0.0
        for i in range(self.num_nodes):
            self.distance += self.edges[self.route[i]][self.route[(i + 1) % self.num_nodes]].weight
        return self.distance
