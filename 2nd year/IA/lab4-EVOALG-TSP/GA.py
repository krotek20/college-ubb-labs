import random
from Chromosome import Chromosome


class GA:
    def __init__(self, param=None, probl_param=None):
        self.__param = param
        self.__probl_param = probl_param
        self.__population = []

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__param['pop_size']):
            c = Chromosome(self.__probl_param)
            self.__population.append(c)

    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__probl_param['function'](c.repres, self.__probl_param['network'])

    def best_chromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness < best.fitness:
                best = c
        return best

    def worst_chromosome(self):
        worst = self.__population[0]
        pos = 0
        for i in range(len(self.__population)):
            if self.__population[i].fitness < worst.fitness:
                worst = self.__population[i]
                pos = i
        return pos, worst

    def selection(self, selection_len):
        # tournament selection
        # selection_len = int(0.02 * self.__param['pop_size'])
        best = random.randint(0, self.__param['pop_size'] - 1)
        for i in range(selection_len + 1):
            current = random.randint(0, self.__param['pop_size'] - 1)
            if self.__population[best].fitness > self.__population[current].fitness:
                best = current
        return best

        # roulette wheel selection
        # selection_len = int(self.__param['pop_size'] * 0.5 + 1)
        # pos = []
        # fitness = []
        # for i in range(selection_len):
        #     pos.append(random.randint(0, self.__param['pop_size'] - 1))
        #     fitness.append(1 / self.__population[pos[-1]].fitness)
        # fitness_sum = sum(fitness)
        # for i in range(len(fitness)):
        #     fitness[i] /= fitness_sum
        # cum_sum = 0
        # value = random.random()
        # for i in range(len(fitness)):
        #     if cum_sum <= value < cum_sum + fitness[i]:
        #         return pos[i]
        #     cum_sum += fitness[i]
        # return pos[-1]

    def one_generation(self):
        new_pop = []
        for _ in range(self.__param['pop_size']):
            p1 = self.__population[self.selection(int(0.02 * self.__param['pop_size']))]
            p2 = self.__population[self.selection(int(0.02 * self.__param['pop_size']))]
            off = p1.crossover(p2)
            off.mutation()
            new_pop.append(off)
        self.__population = new_pop
        self.evaluation()

    def one_generation_elitism(self):
        new_pop = [self.best_chromosome()]
        for _ in range(self.__param['pop_size'] - 1):
            p1 = self.__population[self.selection(int(0.02 * self.__param['pop_size']))]
            p2 = self.__population[self.selection(int(0.02 * self.__param['pop_size']))]
            off = p1.crossover(p2)
            off.mutation()
            new_pop.append(off)
        self.__population = new_pop
        self.evaluation()

    def one_generation_steady_state(self):
        for _ in range(self.__param['pop_size']):
            p1 = self.__population[self.selection(int(0.01 * self.__param['pop_size']))]
            p2 = self.__population[self.selection(int(0.01 * self.__param['pop_size']))]
            off = p1.crossover(p2)
            off.mutation()
            off.fitness = self.__probl_param['function'](off.repres, self.__probl_param['network'])
            pos, worst = self.worst_chromosome()
            if off.fitness < worst.fitness:
                self.__population[pos] = off
