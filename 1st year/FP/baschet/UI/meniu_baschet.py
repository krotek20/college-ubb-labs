from repository.jucator_repository import exceptie_repo
from domain.jucator_validare import exceptie_jucator


class MeniuBaschet:
    def __init__(self, srv):
        self.__srv = srv

    def __adauga_jucator(self):
        nume = input("Introduceti nume: ")
        prenume = input("Introduceti prenume: ")
        inaltime = int(input("Introduceti inaltime: "))
        post = input("Introduceti post(Fundas/Extrema/Pivot): ")
        jucator = self.__srv.creeaza_jucator(nume, prenume, inaltime, post)
        print("Jucatorul " + jucator.get_nume() + " " + jucator.get_prenume() + " a fost adaugat cu succes!")

    def __modifica_inaltime(self):
        nume = input("Introduceti nume: ")
        prenume = input("Introduceti prenume: ")
        jucator = self.__srv.cauta_jucator(nume, prenume)
        if jucator is None:
            print("Nu exista acest jucator!")
        else:
            inaltime = int(input("Introduceti inaltime noua: "))
            if inaltime <= 0:
                print("Inaltime invalida!")
            else:
                self.__srv.modifica_jucator(jucator, inaltime)
                print("Modificare realizata cu succes!")

    def __afisare_jucatori(self):
        jucatori = self.__srv.get_jucatori()
        print("Nume   Prenume   Post   Inaltime")
        print("--------------------------------")
        for jucator in jucatori:
            print(jucator)

    def afisare(self):
        while True:
            print('''
1. Adauga jucator
2. Modifica inaltime
3. Afisare jucatori
0. Iesire aplicatie
            ''')

            cmd = input(">>> ")

            try:
                if cmd == "0":
                    print("Good bye!")
                    return
                elif cmd == "1":
                    self.__adauga_jucator()
                elif cmd == "2":
                    self.__modifica_inaltime()
                elif cmd == "3":
                    self.__afisare_jucatori()
            except ValueError as ve:
                print("UI error\n" + str(ve))
            except exceptie_repo as er:
                print("Repo error\n" + str(er))
            except exceptie_jucator as ej:
                print(str(ej))
