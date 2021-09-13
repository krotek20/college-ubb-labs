from random import randint
import random


class Chromosome:
    def __init__(self, probl_param=None):
        self.__probl_param = probl_param
        repres = [i for i in range(len(self.__probl_param['network']))]
        self.__repres = random.sample(repres, len(repres))
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, representation=None):
        if representation is None:
            representation = []
        self.__repres = representation

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        # cutting section in relative position
        # pos1 = int(random.random() * len(self.__repres))
        # pos2 = int(random.random() * len(c.__repres))
        # if pos1 > pos2:
        #     pos1, pos2 = pos2, pos1
        # new_repres = [-1] * len(self.__repres)
        # for i in range(pos1, pos2):
        #     new_repres[i] = self.__repres[i]
        # holder = [item for item in c.__repres if item not in new_repres]
        # k = 0
        # for i in range(len(new_repres)):
        #     if new_repres[i] == -1:
        #         new_repres[i] = holder[k]
        #         k += 1

        # cut at random position
        # receive the first half of the first parent and
        # add unused genes from the second parent
        cut = randint(0, len(self.__repres))
        new_repres = self.__repres[:cut]
        for elem in c.__repres[cut:]:
            if elem not in new_repres:
                new_repres.append(elem)
        i = 0
        while len(self.__repres) != len(new_repres):
            if c.__repres[i] not in new_repres:
                new_repres.append(c.__repres[i])
            i += 1

        # cutting section in fixed position
        # pos1 = randint(-1, len(self.__probl_param['network']) - 1)
        # pos2 = randint(-1, len(self.__probl_param['network']) - 1)
        # if pos2 < pos1:
        #     pos1, pos2 = pos2, pos1
        # k = 0
        # new_repres = self.__repres[pos1: pos2]
        # for el in c.__repres[pos2:] + c.__repres[:pos2]:
        #     if el not in new_repres:
        #         if len(new_repres) < len(self.__probl_param['network']) - pos1:
        #             new_repres.append(el)
        #         else:
        #             new_repres.insert(k, el)
        #             k += 1

        offspring = Chromosome(self.__probl_param)
        offspring.repres = new_repres
        return offspring

    def mutation(self):
        # get a gene from a random position and
        # insert it in another random position
        pos1 = randint(0, len(self.__probl_param['network']) - 1)
        pos2 = randint(pos1, len(self.__probl_param['network']) - 1)
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)

        # for first in range(len(self.__repres)):
        #     if random.random() < self.__probl_param['rm']:
                # randomly swap two genes with probability
                # second = int(random.random() * len(self.__repres))
                # self.__repres[first], self.__repres[second] = self.__repres[second], self.__repres[first]

                # random insertion with probability
                # second = randint(first, len(self.__probl_param['network']) - 1)
                # el = self.__repres[second]
                # del self.__repres[second]
                # self.__repres.insert(first + 1, el)

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
