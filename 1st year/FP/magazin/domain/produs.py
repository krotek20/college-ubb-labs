class Produs(object):
    
    '''
    clasa de produse
    '''
    
    def __init__(self, id, denumire, pret):
        '''
        constructor pentru clasa de produse
        in: id - int, denumire - string, pret - int
        out: -
        '''
        self.__id = id
        self.__denumire = denumire
        self.__pret = pret
    
    def get_id(self):
        '''
        returneaza id-ul unui produs
        in: -
        out: id - int
        '''
        return self.__id


    def get_denumire(self):
        '''
        returneaza denumirea unui produs
        in: -
        out: denumire - string
        '''
        return self.__denumire


    def get_pret(self):
        '''
        returneaza pretul unui produs
        in: -
        out: pret - int
        '''
        return self.__pret


    def set_denumire(self, value):
        '''
        seteaza denumirea unui produs
        in: value - string
        out: -
        '''
        self.__denumire = value


    def set_pret(self, value):
        '''
        seteaza pretul unui produs
        in: value - int
        out: -
        '''
        self.__pret = value
        
    def __eq__(self, other):
        '''
        suprascriere ==
        '''
        return self.__id == other.get_id() and self.__denumire == other.get_denumire() and self.__pret == other.get_pret()
        
    def __str__(self):
        '''
        suprascriere str()
        '''
        return str(self.__id) + " " + self.__denumire + " " + str(self.__pret)
        
    @staticmethod
    def readProdus(line):
        '''
        functie de conversie dintr-o linie de fisier intr-un produs
        in: line - string
        out: un produs
        '''
        line = line.split(";")
        return Produs(int(line[0]), line[1], int(line[2]))
    
    @staticmethod
    def writeProdus(produs):
        '''
        functie de conversie dintr-un produs intr-o linie de fisier
        in: produs - un produs
        out: un string
        '''
        return str(produs.get_id()) + ";" + produs.get_denumire() + ";" + str(produs.get_pret())

