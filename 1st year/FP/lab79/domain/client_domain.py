"""
@@@ Vintila Radu @@@
"""


class Client:
    """
    Clasa abstracta pentru tipul de date "client"
    Domain:
        client_id: id-ul unui client
        nume: numele unui client
        cnp: cnp-ul unui client
    """

    def __init__(self, cid, nume, cnp):
        """
        Initializarea unui client cu id, nume si cnp
        """

        self.__cid = cid
        self.__nume = nume
        self.__cnp = cnp

    def get_cid(self):
        return self.__cid

    def inc_cid(self):
        self.__cid += 1

    def get_nume(self):
        return self.__nume

    def get_cnp(self):
        return self.__cnp

    def __eq__(self, client):
        """
        Verifica egalitatea
        :return: bool (True daca clientul curent este egal cu cel dat (au acelasi ID); False in caz contrar)
        """
        return self.__cid == client.__cid

    def __str__(self):
        """
        functia care converteste obiectul client in string
        :return: un string ce contine informatiile unui client (client_id, nume, cnp)
        """
        return str(self.__cid) + " || " + self.__nume + " || " + str(self.__cnp)

    def __hash__(self):
        return hash((
            self.__cid,
            self.__nume,
            self.__cnp
        ))
