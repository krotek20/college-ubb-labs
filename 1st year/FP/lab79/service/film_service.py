"""
@@@ Vintila Radu @@@
"""

from domain.film_domain import Film


class srv_film:
    def __init__(self, repo, val):
        self.__repo = repo
        self.__val = val

    def creeaza_film(self, fid, titlu, desc, gen):
        """
        service function - adaugare film nou
        :param fid: int (ID-ul filmului)
        :param titlu: string (titlul filmului)
        :param desc: string (descrierea filmului)
        :param gen: string (genul filmului)
        :return: film
        """

        film = Film(fid, titlu, desc, gen)
        self.__val.validare(film)
        self.__repo.store(film)

        return film

    def get_all(self):
        """
        service function - transfera lista tuturor filmelor
        :return: lista de filme
        """
        return self.__repo.get_filme()

    def get_all_fids(self):
        """
        service function - transfera lista tuturor id-urilor filmelor
        :return: list of ids
        """
        return self.__repo.get_all_ids()

    def sterge_film(self, fid):
        """
        service function - stergerea unui film dupa ID
        :param fid: int (ID film)
        """
        self.__repo.remove(fid)

    def sterge_all(self):
        """
        service function - stergerea tuturor filmelor
        """
        self.__repo.clear()

    def modifica_film(self, fid, titlu, desc, gen):
        """
        service function - modifica un film existent in repository
        :param fid: int (ID film)
        :param titlu: string (noul titlu film)
        :param desc: string (noua descriere film)
        :param gen: string (noul gen film)
        """
        film = Film(fid, titlu, desc, gen)
        self.__val.validare(film)
        self.__repo.update(film)

    def cauta_filme(self, alegere, val):
        """
        service function - cautarea filmelor dupa valoarea specificata
        :param alegere: criteriul de cautare - ID / titlu / desc / gen (string)
        :param val: valoarea de cautare - fid / titlu / desc / gen (int / string / string / string)
        :return: lista filmelor gasite
        """
        return self.__repo.find(alegere, val)
