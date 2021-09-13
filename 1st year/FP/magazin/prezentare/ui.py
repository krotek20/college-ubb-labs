from domain.produs import Produs

class UI(object):
    def __init__(self, serviceProduse):
        self.__serviceProduse = serviceProduse
        self.__filterCuvant = ""
        self.__filterPret = -1

    def adaugaProdus(self):
        '''
        adauga un produs
        in: -
        out: -
        '''
        id = int(input("Da id: "))
        denumire = input("Da denumirea: ")
        pret = int(input("Da pretul: "))
        self.__serviceProduse.adaugaProdus(Produs(id, denumire, pret))
        
    def stergeProdusCifra(self):
        '''
        sterge toate produsele al caror id contine o cifra citita
        in: -
        out: -
        '''
        cifra = int(input("Da cifra: "))
        print("S-au sters " + str(self.__serviceProduse.stergeProduseCifra(cifra)) + " produse")
        
    def filter(self):
        '''
        afiseaza toate produsele folosind un filtru de cuvant si un filtru de pret
        in: -
        out: -
        '''
        print("Filtru cuvant: " + self.__filterCuvant + "\nFiltru pret: " + str(self.__filterPret))
        list = self.__serviceProduse.getRepo().getAll()
        for el in list:
            if self.__filterCuvant == "":
                if self.__filterPret == -1:
                    print(str(el))
                elif el.get_pret() == self.__filterPret:
                    print(str(el))
            else:
                if self.__filterCuvant in el.get_denumire():
                    if self.__filterPret == -1:
                        print(str(el))
                    elif el.get_pret() == self.__filterPret:
                        print(str(el))
              
    def setFilter(self):
        '''
        seteaza filterul
        in: -
        out: -
        '''
        self.__filterCuvant = input("Da filtru cuvant: ")
        self.__filterPret = int(input("Da filtru pret: "))
        
    def undo(self):
        '''
        undo la ultima operatie de stergere
        in: -
        out: -
        '''
        self.__serviceProduse.undo()
        
    def run(self):
        '''
        functie principala
        in: -
        out: -
        '''
        commands = {"adauga produs": self.adaugaProdus, "sterge produse": self.stergeProdusCifra, "filtru": self.setFilter, "undo": self.undo}
        mesajPredefinit = "adauga produs: adauga un produs nou\nsterge produse: sterge toate produsele al caror id contine o cifra citita\nfiltru: seteaza filtrul\nundo: undo la ultima operatie de stergere\n"
        self.filter()
        while(True):
            cmd = input(">>")
            if cmd in commands:
                commands[cmd]()
                self.filter()
            elif cmd == "help":
                print(mesajPredefinit)
            elif cmd == "exit":
                break
            else:
                print("Comanda invalida!")