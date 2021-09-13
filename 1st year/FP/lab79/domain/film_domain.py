"""
@@@ Vintila Radu @@@
"""


class Film:
    """
    Clasa abstracta pentru tipul de date "film"
    Domain:
        film_id: id-ul unui film
        titlu: titlul unui film
        desc: descrierea unui film
        gen: genul unui film
    """

    def __init__(self, fid, titlu, desc, gen):
        """
        Initializarea unui film cu id, titlu, descriere si gen
        """

        self.__fid = fid
        self.__titlu = titlu
        self.__desc = desc
        self.__gen = gen

    def get_fid(self):
        return self.__fid

    def inc_fid(self):
        self.__fid += 1

    def get_titlu(self):
        return self.__titlu

    def get_desc(self):
        return self.__desc

    def get_gen(self):
        return self.__gen

    def __eq__(self, film):
        """
        Verificare egalitate
        :return: bool (True daca filmul curent este egal cu cel dat (au acelasi ID); False in caz contrar)
        """
        return self.get_fid() == film.get_fid()

    def __str__(self):
        """
        Convertirea obiectului la string
        """
        return str(self.get_fid()) + " || " + str(self.get_titlu()) + " || " + str(self.get_desc()) + " || " + str(self.get_gen())
