from random import randint


class Chromosome:
    def __init__(self, probl_param=None):
        self.__problParam = probl_param
        self.__repres = [0] * probl_param['no_dim']
        self.__fitness = 0.0
        self.generate_representation()

    def normalise(self):
        local_communities = 0
        helper = {}
        for i in range(self.__problParam['no_dim']):
            if not self.__repres[i] in helper:
                local_communities += 1
                helper[self.__repres[i]] = local_communities
                self.__repres[i] = local_communities
            else:
                self.__repres[i] = helper[self.__repres[i]]

    def generate_representation(self):
        percentage = 0.2
        communities = 1
        for i in range(1, int(self.__problParam['no_dim'] * percentage) + 1):
            node = randint(0, self.__problParam['no_dim'] - 1)
            if self.__repres[node] != 0:
                continue
            self.__repres[node] = communities
            # searching for its neighbors
            for j in self.__problParam['network']['mat'][node]:
                if self.__problParam['network']['mat'][node][j] == 1:
                    self.__repres[j] = communities
            communities += 1

        for i in range(self.__problParam['no_dim']):
            if self.__repres[i] == 0:
                self.__repres[i] = communities
                communities += 1

        self.normalise()

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
        self.normalise()

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        r = randint(0, len(self.__repres) - 1)
        new_repres = [0] * len(c.__repres)
        for i in range(len(self.__repres)):
            if self.__repres[i] == self.__repres[r]:
                new_repres[i] = self.__repres[r]
            else:
                new_repres[i] = c.__repres[i]
        offspring = Chromosome(self.__problParam)
        offspring.repres = new_repres
        return offspring

    def mutation(self):
        random_pos = randint(0, len(self.__repres) - 1)
        random_com = randint(0, len(self.__repres) - 1)
        self.__repres[random_pos] = random_com
        self.normalise()

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
