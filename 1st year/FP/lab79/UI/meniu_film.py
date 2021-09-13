"""
@@@ Vintila Radu @@@
"""

from domain.film_validare import exceptie_film
from repository.film_repo import exceptie_film_repo


class Film_meniu:
    def __init__(self, srv_film):
        self.__srv_film = srv_film
        self.__cmds = {
            "1": self.__add_film,
            "2": self.__afisare_filme,
            "3": self.__modificare_film,
            "5": self.__stergere_film,
            "6": self.__stergere_all
        }

    @staticmethod
    def __print_menu():
        """
        Afiseaza meniul filmelor
        """
        print('''
---Meniu film---
1. Adauga film
2. Afisare filme
3. Modifica date film
4. Cauta filme
5. Sterge film
6. Sterge toate filmele
0. Intoarce-te in aplicatie
        ''')

    @staticmethod
    def __print_cauta():
        """
        Afiseaza meniul cautarilor
        """
        print('''
---Cauta filme dupa---
         ID
         Titlu
         Descriere (DESC)
         Gen
Intoarce-te in aplicatie (BACK)
        ''')

    def __add_film(self):
        """
        Adauga un film
        """

        fid = int(input("Introduceti ID: "))
        titlu = input("Introduceti titlu: ")
        desc = input("Introduceti descriere: ")
        gen = input("Introduceti gen: ")
        film = self.__srv_film.creeaza_film(fid, titlu, desc, gen)
        print("Filmul " + film.get_titlu() + " a fost salvat cu succes!")

    def __afisare_filme(self):
        """
        Afiseaza toate filmele
        """

        print("---Filme---")
        print("ID  |  Titlu  |  Descriere  |  Gen")
        filme = self.__srv_film.get_all()
        if not filme:
            print("Nu exista filme!")
        for film in filme:
            print(film)

    def __stergere_film(self):
        """
        Sterge un film din repository
        """

        fid = int(input("Introduceti ID: "))
        self.__srv_film.sterge_film(fid)
        print("Film sters cu succes!")

    def __stergere_all(self):
        """
        Sterge toate filmele din repository
        """
        if not self.__srv_film.get_all():
            print("Nu exista filme!")
        else:
            self.__srv_film.sterge_all()
            print("Stergere efectuata cu succes!")

    def __modificare_film(self):
        """
        Modifica datele unui film curent
        """
        fid = int(input("Introduceti ID: "))
        if fid not in self.__srv_film.get_all_fids():
            print("Nu exista un film cu acest ID!")
        else:
            titlu = input("Introduceti noul titlu: ")
            desc = input("Introduceti noua descriere: ")
            gen = input("Introduceti noul gen: ")
            self.__srv_film.modifica_film(fid, titlu, desc, gen)
            print("Modificare efectuata cu succes!")

    def __cautare_filme(self, alegere):
        """
        Cautarea unui film dupa ID / titlu / descriere / gen
        :param alegere: string ( ID / titlu / desc / gen )
        """
        filme = []
        if alegere.lower() == "id":
            fid = int(input("Introduceti ID: "))
            filme = self.__srv_film.cauta_filme(alegere, fid)
        elif alegere.lower() == "titlu":
            titlu = input("Introduceti titlu: ")
            filme = self.__srv_film.cauta_filme(alegere, titlu)
        elif alegere.lower() == "desc":
            desc = input("Introduceti descriere: ")
            filme = self.__srv_film.cauta_filme(alegere, desc)
        elif alegere.lower() == "gen":
            gen = input("Introduceti gen: ")
            filme = self.__srv_film.cauta_filme(alegere, gen)

        if len(filme) == 0:
            if alegere.lower() == "id" or alegere.lower() == "titlu":
                print("Nu au fost gasite filme cu acest " + alegere + "!")  # mesaj pentru cautarea dupa ID sau titlu
            elif alegere.lower() == "desc":
                print("Nu au fost gasite filme cu acesta " + alegere + "!")  # mesaj pentru cautarea dupa descriere
            else:
                print("Nu au fost gasite filme de acest " + alegere + "!")  # mesaj pentru cautarea dupa gen
        else:
            print("ID  |  Titlu  |  Descriere  |  Gen")
            for film in filme:
                print(film)

    def afisare(self):
        while True:
            self.__print_menu()
            cmd = input("Alegeti optiunea dorita: ")

            if cmd == "0":
                return
            elif cmd == "4":
                while True:
                    Film_meniu.__print_cauta()
                    cmd = input("Alegeti optiunea dorita: ")
                    if cmd.lower() == "back":
                        break
                    elif cmd.lower() == "id" or cmd.lower() == "titlu" or cmd.lower() == "desc" or cmd.lower() == "gen":
                        self.__cautare_filme(cmd)
            elif cmd in self.__cmds:
                try:
                    self.__cmds[cmd]()
                except ValueError as ve:
                    print("UI Error:\n" + str(ve))
                except exceptie_film as vale:
                    print("Service Error:\n" + str(vale))
                except exceptie_film_repo as re:
                    print("Repo Error:\n" + str(re))
            else:
                print("Nu ati introdus o optiune valida!")
