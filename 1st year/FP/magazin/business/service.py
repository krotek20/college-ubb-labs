import copy

class ServiceProduse(object):
    def __init__(self, repoProduse):
        '''
        constructor pentru clasa de service
        in: repoProduse - un repository de produse
        out: -
        '''
        self.__repoProduse = repoProduse
        self.__trashCan = []
    
    def getRepo(self):
        '''
        returneaza un repo de produse
        in: -
        out: un repo de produse
        '''
        return self.__repoProduse
    
    def adaugaProdus(self, produs):
        '''
        functie de adaugare unui produs
        in: produs - un produs
        out: -
        '''
        self.__repoProduse.adaugaEntitate(produs)

    def stergeProduseCifra(self, cifra):
        '''
        sterge toate produsele al caror id contine cifra cifra
        in: cifra - o cifra(int)
        out: numarul de produse sterse(int)
        '''
        self.__trashCan = []
        counter = 0
        for i in range(len(self.__repoProduse.getAll())-1, -1, -1):
            produs = self.__repoProduse.getAll()[i]
            id = produs.get_id()
            while(id>0):
                if id%10 == cifra:
                    self.__trashCan.append(produs)
                    self.__repoProduse.stergeEntitate(produs)
                    counter += 1
                    break
                id = id//10
        return counter
    
    def undo(self):
        '''
        undo la ultima operatie de stergere
        in: -
        out: -
        '''
        for produs in reversed(self.__trashCan):
            self.__repoProduse.adaugaEntitate(produs)
        self.__trashCan = []