"""
@@@ Vintila Radu @@@
"""
from domain.client_validare import exceptie_client
from repository.client_repo import exceptie_client_repo
from random import randint, seed
from sys import maxsize
import time


class Client_meniu:
    def __init__(self, srv_client):
        self.__srv_client = srv_client
        self.__cmds = {
            "1": self.__add_client,
            "2": self.__afisare_clienti,
            "3": self.__modificare_client,
            "5": self.__stergere_client,
            "6": self.__stergere_all,
            "7": self.__generare_random
        }

    @staticmethod
    def __print_menu():
        """
        Afiseaza meniul clientilor
        """
        print('''
---Meniu client---
1. Adauga client
2. Afisare clienti
3. Modifica date client
4. Cauta clienti
5. Sterge client
6. Sterge toti clientii
7. Generare random
0. Intoarce-te in aplicatie
        ''')

    @staticmethod
    def __print_cauta():
        """
        Afiseaza meniul cautarilor
        """
        print('''
---Cauta clienti dupa---
          ID
          Nume
          CNP
Intoarce-te in aplicatie (BACK)
        ''')

    def __add_client(self):
        """
        Adauga un client
        """

        cid = int(input("Introduceti ID: "))
        nume = input("Introduceti nume: ")
        cnp = int(input("Introduceti CNP: "))
        client = self.__srv_client.creeaza_client(cid, nume, cnp)
        print("Client " + client.get_nume() + " salvat cu succes!")

    def __afisare_clienti(self):
        """
        Afiseaza lista clientilor
        """

        print("---Clienti.txt---")
        print("ID  |  Nume  |  CNP")
        ok = True
        for client in self.__srv_client.get_all():
            ok = False
            print(client)

        if ok is True:
            print("Nu exista clienti!")

    def __stergere_client(self):
        """
        Sterge un client din repository
        """

        cid = int(input("Introduceti ID: "))
        self.__srv_client.sterge_client(cid)
        print("Client sters cu succes!")

    def __stergere_all(self):
        """
        Sterge toti clientii din repository
        """
        if not self.__srv_client.get_all():
            print("Nu exista clienti!")
        else:
            self.__srv_client.sterge_all()
            print("Stergere efectuata cu succes!")

    def __modificare_client(self):
        """
        Modifica datele unui client
        """
        cid = int(input("Introduceti ID: "))
        if cid not in self.__srv_client.get_all_cids():
            print("Nu exista un client cu acest ID!")
        else:
            nume = input("Introduceti noul nume: ")
            cnp = int(input("Introduceti noul CNP: "))
            self.__srv_client.modifica_client(cid, nume, cnp)
            print("Modificare efectuata cu succes!")

    def __cautare_clienti(self, alegere):
        """
        Cautarea unui client dupa ID / nume / CNP
        :param alegere: string ( ID / nume / CNP )
        """
        clienti = []
        if alegere.lower() == "id":
            cid = int(input("Introduceti ID: "))
            clienti = self.__srv_client.cauta_clienti(alegere, cid)
        elif alegere.lower() == "nume":
            nume = input("Introduceti nume: ")
            clienti = self.__srv_client.cauta_clienti(alegere, nume)
        elif alegere.lower() == "cnp":
            cnp = int(input("Introduceti CNP: "))
            clienti = self.__srv_client.cauta_clienti(alegere, cnp)

        if len(clienti) == 0:
            print("Nu au fost gasiti clienti cu acest " + alegere + "!")
        else:
            print("ID  |  Nume  |  CNP")
            for client in clienti:
                print(client)

    def __generare_random(self):
        """
        Genereaza random un numar dat de clienti
        """
        n = int(input("Introduceti numarul de generari: "))
        seed(time.clock())
        if n >= 1:
            for i in range(n):
                cid_rand = randint(1, maxsize)
                cnp_rand = randint(1, maxsize)
                str_length = randint(1, 15)
                print(str(cid_rand) + " " + str(cnp_rand))
                print(str_length)
                nume_rand = self.__srv_client.random_string(str_length, index=1)
                print(nume_rand)
                client = self.__srv_client.creeaza_client(cid_rand, nume_rand, cnp_rand)
            print("Clienti adaugati cu succes!")
        else:
            print("Trebuie introdus un numar natural, diferit de zero")

    def afisare(self):
        while True:
            self.__print_menu()
            cmd = input("Alegeti optiunea dorita: ")

            if cmd == "0":
                return
            elif cmd == "4":
                while True:
                    Client_meniu.__print_cauta()
                    cmd = input("Alegeti optiunea dorita: ")
                    if cmd.lower() == "back":
                        break
                    elif cmd.lower() == "id" or cmd.lower() == "nume" or cmd.lower() == "cnp":
                        self.__cautare_clienti(cmd)
            elif cmd in self.__cmds:
                try:
                    self.__cmds[cmd]()
                except ValueError as ve:
                    print("UI Error:\n" + str(ve))
                except exceptie_client as vale:
                    print("Service Error:\n"+str(vale))
                except exceptie_client_repo as re:
                    print("Repo Error:\n"+str(re))
            else:
                print("Nu ati introdus o optiune valida!")
