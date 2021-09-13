"""
@@@ Vintila Radu @@@
"""
from repository.client_repo import exceptie_client_repo
from repository.film_repo import exceptie_film_repo


class Rapoarte_meniu:
    def __init__(self, srv_client, srv_film, srv_inchiriere):
        self.__srv_client = srv_client
        self.__srv_film = srv_film
        self.__srv_inchiriere = srv_inchiriere
        self.__cmds = {
            "1": self.__clienti_dupa_nume,
            "2": self.__clienti_dupa_numar,
            "3": self.__filme_inchiriate,
            "4": self.__primii_clienti,
            "5": self.__gen_numar_incs
        }

    @staticmethod
    def __print_menu():
        """
        Afiseaza meniul rapoartelor
        """
        print('''
---Meniu rapoarte---
1. Lista clientilor cu filme inchiriate ordonati dupa nume
2. Lista clientilor cu filme inchiriate ordonati dupa nuamrul de filme inchiriate
3. Top 5 cele mai inchiriate filme
4. Primii 30% clienti cu cele mai multe filme
5. Statistica in functie de genul filmului
0. Intoarce-te in aplicatie
        ''')

    def __clienti_dupa_nume(self):
        """
        Afiseaza lista clientilor cu filme inchiriate ordonati dupa nume
        """
        result = self.__srv_inchiriere.get_clienti_activi()
        print("---Clienti.txt ordonati dupa nume---")
        print("ID  |  Nume  |  CNP")
        if not result:
            print("Nu exista clienti cu filme inchiriate!")
        for res in result:
            print(res[0] + " (" + str(res[1]) + ")")

    def __clienti_dupa_numar(self):
        """
        Afiseaza lista clientilor cu filme inchiriate ordonati dupa numarul de filme inchiriate
        """
        result = self.__srv_inchiriere.get_clienti_activi(numar=True)
        print("---Clienti.txt ordonati dupa numarul de filme inchiriate---")
        print("ID  |  Nume  |  CNP  (nr. filme inchiriate)")
        if not result:
            print("Nu exista clienti cu filme inchiriate!")
        for res in result:
            print(res[0] + " (" + str(res[1]) + ")")

    def __filme_inchiriate(self):
        """
        Afiseaza top 5 cele mai inchiriate filme
        """
        result = self.__srv_inchiriere.get_top_filme_inchiriate()
        print("---Top 5 filme inchiriate---")
        if not result:
            print("Nu exista filme inchiriate!")
        i = 0
        for res in result[:5]:
            i += 1
            print(str(i) + ". " + res[0])

    def __primii_clienti(self):
        """
        Afiseaza primii 30% clienti cu cele mai multe filme inchiriate
        """
        result = self.__srv_inchiriere.get_clienti_activi(numar=True)
        print("---Primii 30% clienti---")
        if not result:
            print("Nu exista clienti cu filme inchiriate!")
        for res in result[:int(len(result)*0.3)]:
            print(str(res[0]) + " (" + str(res[1]) + ")")

    def __gen_numar_incs(self):
        """
        Afiseaza fiecare gen si numarul de inchirieri corespunzator genului
        """
        (genuri, incs) = self.__srv_inchiriere.get_gen_incs()
        print("Gen  |  Numarul de inchirieri de acest gen")
        for i in range(len(genuri)):
            print(genuri[i] + ": " + str(incs[i]))

    def afisare(self):
        while True:
            self.__print_menu()
            cmd = input("Introduceti comanda dorita: ")

            if cmd == "0":
                return
            elif cmd in self.__cmds:
                try:
                    self.__cmds[cmd]()
                except ValueError as ve:
                    print("UI Error:\n" + str(ve))
                except exceptie_client_repo as excr:
                    print("Repo Error:\n" + str(excr))
                except exceptie_film_repo as exfr:
                    print("Repo Error:\n" + str(exfr))
            else:
                print("Nu ati introdus o optiune valida!")
