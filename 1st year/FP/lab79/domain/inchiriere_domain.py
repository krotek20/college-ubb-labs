"""
@@@ Vintila Radu @@@
"""


class Inchiriere:
    def __init__(self, incid, client, film, stare):
        """
        Initializarea unei inchirieri
        :param incid: int (ID inchiriere)
        :param client: Client (instanta de client)
        :param film: Film (instanta de film)
        :param stare: string (stare inchiriere)
        """
        self.__incid = incid
        self.__client = client
        self.__film = film
        self.__stare = stare

    def get_id(self):
        return self.__incid

    def get_client(self):
        return self.__client

    def get_film(self):
        return self.__film

    def get_stare(self):
        """
        functie de get
        :return: starea inchirierii ( Inchiriat / Returnat )
        """
        return self.__stare

    def returneaza_film(self):
        self.__stare = "Returnat"
        return self.__client, self.__film

    def __eq__(self, inc):
        """
        Verifica egalitatea
        :param inc: Inchirierea
        :return: bool (True daca inchirierea curenta este egala cu cea data (au acelasi ID), False in caz contrar)
        """
        return self.get_id() == inc.get_id()

    def __str__(self):
        """
        Converteste obiectul inchiriere in string
        """
        return str(self.__incid) + " || " + self.__client.get_nume() + " || " + self.__film.get_titlu() + " || " + self.__stare
