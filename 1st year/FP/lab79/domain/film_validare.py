"""
@@@ Vintila Radu @@@
"""


class exceptie_film(Exception):
    def __init__(self, erori):
        self.__erori = erori

    def get_erori(self):
        return self.__erori

    def __str__(self):
        return self.__erori


class validare_film:

    @staticmethod
    def validare(film):
        """
        functia care verifica validitatea unui film
        :raise exceptie_film: Oricare dintre string-urile de mai jos
        """

        erori = []
        if not film.get_fid():
            erori.append("Trebuie introdus un ID!")
        if not type(film.get_fid()) is int or film.get_fid() <= 0:
            erori.append("ID-ul filmului trebuie sa fie un numar intreg mai mare sau egal decat 1!")
        if not film.get_titlu():
            erori.append("Trebuie introdus un titlu!")
        if not film.get_desc():
            erori.append("Trebuie introdusa o descriere!")
        if not film.get_gen():
            erori.append("Trebuie introdus un gen!")

        if len(erori) > 0:
            raise exceptie_film(erori)
