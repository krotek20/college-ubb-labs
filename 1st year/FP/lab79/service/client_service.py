"""
@@@ Vintila Radu @@@
"""

from domain.client_domain import Client
import string
import random


class srv_client:
    def __init__(self, repo, val):
        self.__repo = repo
        self.__val = val

    def creeaza_client(self, cid, nume, cnp):
        """
        service function - crearea unui client nou
        :param cid: int (ID-ul clientului)
        :param nume: string (numele clientului)
        :param cnp: int (cnp-ul clientului)
        :return: client
        """

        client = Client(cid, nume, cnp)
        self.__val.validare(client)
        self.__repo.store(client)
        return client

    def get_all(self):
        """
        service function - transfera lista tuturor clientilor
        :return: lista de clienti
        """
        return self.__repo.get_clienti()

    def get_all_cids(self):
        """
        service function - transfera lista tuturor id-urilor clientilor
        :return: list of ids
        """
        return self.__repo.get_all_ids()

    def sterge_client(self, cid):
        """
        service function - stergerea unui client dupa ID
        :param cid: int (ID client)
        """
        self.__repo.remove(cid)

    def sterge_all(self):
        """
        service function - stergerea tuturor clientilor
        """
        self.__repo.clear()

    def modifica_client(self, cid, nume, cnp):
        """
        service function - modifica un client existent in repository
        :param cid: int (ID client)
        :param nume: string (noul nume client)
        :param cnp: int (noul CNP client)
        """
        client = Client(cid, nume, cnp)
        self.__val.validare(client)
        self.__repo.update(client)

    def cauta_clienti(self, alegere, val):
        """
        service function - cautarea clientilor dupa valoarea specificata
        :param alegere: criteriul de cautare - ID / nume / CNP (string)
        :param val: valoarea de cautare - cid / nume / cnp (int / string / int)
        :return: lista clientilor gasiti
        """
        return self.__repo.find(alegere, val)

    def random_string(self, length, index=1):
        """
        generate random string
        :param length: int (length of string)
        :param index: int (index of letters in string)
        :return: the random generated string
        """

        # iterativ
        """letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))"""

        # recursiv
        if index > length:
            return ""
        return random.choice(string.ascii_letters) + self.random_string(length, index + 1)
