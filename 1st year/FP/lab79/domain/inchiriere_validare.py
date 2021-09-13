"""
@@@ Vintila Radu @@@
"""


class exceptie_inchiriere(Exception):
    def __init__(self, erori):
        self.__erori = erori

    def get_erori(self):
        return self.__erori


class validare_inchiriere:
    @staticmethod
    def validare(inc):
        """
        functia care verifica validitatea unei inchirieri
        :raise exceptie_inchiriere: Oricare dintre string-urile de mai jos
        """

        erori = []
        if not inc.get_id():
            erori.append("Trebuie introdus un ID!")
        if not type(inc.get_id()) is int or inc.get_id() <= 0:
            erori.append("ID-ul inchirierii trebuie sa fie un numar intreg mai mare sau egal decat 1!")

        if len(erori) > 0:
            raise exceptie_inchiriere(erori)
