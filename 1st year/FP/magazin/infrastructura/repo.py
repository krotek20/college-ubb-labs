from copy import deepcopy
import copy
class Repo(object):
    '''
    clasa generala de repo
    '''
    def __init__(self, fileName, readEntity, writeEntity):
        '''
        constructor pentru clasa de repo
        in: fileName - nume de fisier, readEntity - functie de conversie din linie de fisier in entitate, writeEntity - functie de conversie din entitate in linie de fisier
        '''
        self.__fileName = fileName
        self.__readEntity = readEntity
        self.__writeEntity = writeEntity
        self.__list = []
    
    def __readFromFile(self):
        '''
        citeste din fisier
        in: -
        out: -
        '''
        self.__list = []
        with open(self.__fileName, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    self.__list.append(self.__readEntity(line))

    def __writeToFile(self):
        '''
        functie de scriere in fisier
        in: -
        out: -
        '''
        with open(self.__fileName, "w") as f:
            for entitate in self.__list:
                f.write(self.__writeEntity(entitate)+'\n')
        
    def adaugaEntitate(self, entitate):
        '''
        functie de adaugare a unei entitati in lista
        in: entitate - o entitate
        out: -
        '''
        self.__readFromFile()
        self.__list.append(entitate)
        self.__writeToFile()
        
    def getAll(self):
        '''
        returneaza toata lista de entitati
        in: -
        out: o lista de entitati
        '''
        self.__readFromFile()
        return self.__list
    
    def stergeEntitate(self, entitate):
        '''
        functie de stergere a unei entitati
        in: entitate - o entitate
        out: -
        '''
        self.__readFromFile()
        self.__list.remove(entitate)
        self.__writeToFile()
        
        