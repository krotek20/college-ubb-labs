"""
@@@ Vintila Radu @@@
"""

from domain.inchiriere_validare import exceptie_inchiriere
from repository.inchiriere_repo import exceptie_inchiriere_repo
from repository.client_repo import exceptie_client_repo
from repository.film_repo import exceptie_film_repo


class Inchiriere_meniu:
    def __init__(self, srv_inc):
        self.__srv_inc = srv_inc
        self.__cmds = {
            "1": self.__add_inchiriere,
            "2": self.__afiseaza_inchirieri,
            "3": self.__returneaza_film,
            "4": self.__remove_all
        }

    @staticmethod
    def __print_menu():
        """
        Afiseaza meniul inchirierilor
        """
        print('''
---Meniu inchiriere---
1. Inchiriaza film
2. Afiseaza inchirierile
3. Returneaza film
4. Sterge toate inchirierile
0. Intoarce-te in aplicatie
        ''')

    def __add_inchiriere(self):
        """
        Inchiriaza un film
        """

        incid = int(input("Introduceti ID inchiriere: "))
        cid = int(input("Introduceti ID client: "))
        fid = int(input("Introduceti ID film: "))
        inc = self.__srv_inc.creeaza_inchiriere(incid, cid, fid)
        print("Filmul " + inc.get_film().get_titlu() + " a fost inchiriat de catre clientul " + inc.get_client().get_nume())

    def __afiseaza_inchirieri(self):
        """
        Afiseaza toate inchirierile facute
        """

        print("---Inchirieri---")
        ok = True
        for inc in self.__srv_inc.get_all():
            ok = False
            print(inc)

        if ok is True:
            print("Nu exista inchirieri!")

    def __returneaza_film(self):
        """
        Returneaza un film
        """
        incid = int(input("Introduceti ID: "))
        (client, film) = self.__srv_inc.returneaza_film(incid)
        print("Clientul " + client.get_nume() + " a returnat filmul " + film.get_titlu())

    def __remove_all(self):
        """
        Sterge toate inchirierile din repository
        """
        if not self.__srv_inc.get_all():
            print("Nu exista inchirieri!")
        else:
            self.__srv_inc.remove_all()
            print("Stergere efectuata cu succes!")

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
                except exceptie_inchiriere as vale:
                    print("Service Error:\n" + str(vale))
                except exceptie_inchiriere_repo as exir:
                    print("Repo Error:\n" + str(exir))
                except exceptie_client_repo as excr:
                    print("Repo Error:\n" + str(excr))
                except exceptie_film_repo as exfr:
                    print("Repo Error:\n" + str(exfr))
            else:
                print("Nu ati introdus o optiune valida!")
