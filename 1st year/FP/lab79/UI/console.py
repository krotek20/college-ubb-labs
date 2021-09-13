"""
@@@ Vintila Radu @@@
"""

from UI.meniu_client import Client_meniu
from UI.meniu_film import Film_meniu
from UI.meniu_inchiriere import Inchiriere_meniu
from UI.meniu_rapoarte import Rapoarte_meniu


class Console:
    def __init__(self, srv_client, srv_film, srv_inc):
        self.__srv_client = srv_client
        self.__srv_film = srv_film
        self.__srv_inc = srv_inc

    @staticmethod
    def printeaza_optiuni():
        print('''
1. Meniu clienti
2. Meniu filme
3. Meniu inchirieri
4. Meniu rapoarte
0. Iesire aplicatie
        ''')

    def show(self):
        while True:
            self.printeaza_optiuni()
            cmd = input("Introduceti optiunea dorita: ")

            try:
                if cmd == "0":
                    print("Ai iesit din aplicatie!")
                    return
                elif cmd == "1":
                    Client_meniu(self.__srv_client).afisare()
                elif cmd == "2":
                    Film_meniu(self.__srv_film).afisare()
                elif cmd == "3":
                    Inchiriere_meniu(self.__srv_inc).afisare()
                elif cmd == "4":
                    Rapoarte_meniu(self.__srv_client, self.__srv_film, self.__srv_inc).afisare()
                else:
                    print("Nu ati introdus o optiune valida!")
            except ValueError:
                print("Nu ati introdus o optiune valida!")
            except KeyError:
                print("Nu ati introdus o optiune valida!")
