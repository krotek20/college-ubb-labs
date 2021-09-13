from random import randint
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
        best = self.__population[0]
        for c in self.__population:
            if c.fitness > best.fitness:
                best = c
        return best

    def selection(self, selection_len):
        best = randint(0, self.__param['pop_size'] - 1)
        for i in range(selection_len + 1):
            current = randint(0, self.__param['pop_size'] - 1)
            if self.__population[best].fitness > self.__population[current].fitness:
                best = current
        return best

    def one_generation(self):
        new_pop = []
        for _ in range(self.__param['pop_size']):
            p1 = self.__population[self.selection(int(0.01 * self.__param['pop_size']))]
            p2 = self.__population[self.selection(int(0.01 * self.__param['pop_size']))]
            off = p1.crossover(p2)
            off.mutation()
            new_pop.append(off)
        self.__population = new_pop
        self.evaluation()

    def one_generation_elitism(self):
        new_pop = [self.best_chromosome()]
        for _ in range(self.__param['pop_size'] - 1):
            p1 = self.__population[self.selection(int(0.01 * self.__param['pop_size']))]
            p2 = self.__population[self.selection(int(0.01 * self.__param['pop_size']))]
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
            off.fitness = self.__probl_param['function'](off.repres)
            worst = self.worst_chromosome()
            if off.fitness < worst.fitness:
                worst = off
