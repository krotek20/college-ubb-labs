"""
@@@ Vintila Radu @@@
"""
from domain.inchiriere_domain import Inchiriere
from util.sorting import sorted_custom


class srv_inchiriere:
    def __init__(self, repo_client, repo_film, repo_inchiriere, val):
        self.__repo_client = repo_client
        self.__repo_film = repo_film
        self.__repo_inchiriere = repo_inchiriere
        self.__val = val

    def creeaza_inchiriere(self, incid, cid, fid):
        """
        service function - inchirierea unui nou film
        :param incid: int (ID inchiriere)
        :param cid: int (ID client)
        :param fid: int (ID film)
        :return: inchiriere
        """
        client = self.__repo_client.find_id(cid)
        film = self.__repo_film.find_id(fid)
        inchiriere = Inchiriere(incid, client, film, "Inchiriat")
        self.__val.validare(inchiriere)
        self.__repo_inchiriere.store(inchiriere)
        return inchiriere

    def get_all(self):
        """
        service function - afisarea tuturor inchirierilor efectuate
        :return: lista inchirierilor
        """

        return self.__repo_inchiriere.get_incs()

    def returneaza_film(self, incid):
        """
        service function - returneaza un film inchiriat de catre un client
        :param incid: int (ID inchiriere)
        :return: tuplu cid + fid
        """

        return self.__repo_inchiriere.returneaza_film(incid)

    def remove_all(self):
        """
        service function - stergerea tuturor inchirierilor
        """
        self.__repo_inchiriere.clear()

    def get_clienti_activi(self, numar=False):
        """
        service function - transfera o lista de clienti cu filme inchiriate sortata dupa nume
        :return: lista de clienti sortata dupa nume
        """
        incs = self.__repo_inchiriere.get_incs()
        cids = []
        for inc in incs:
            cid = inc.get_client().get_cid()
            if cids.count(cid) == 0:
                cids.append(cid)
        result = []
        for cid in cids:
            freq = 0
            for inc in incs:
                if inc.get_client().get_cid() == cid and inc.get_stare() == "Inchiriat":
                    freq += 1
            if freq > 0:
                name = self.__repo_client.find_id(cid).get_nume()
                result.append([name, freq])
        if not numar:
            result = sorted_custom(result, "selection", key=lambda x: x[0])
        else:
            result = sorted_custom(result, "selection_rec", key=lambda x: x[1], reverse=True)
        return result

    def get_top_filme_inchiriate(self):
        """
        service function - gaseste cele mai inchiriate filme (top5)
        :return: lista de filme inchiriate
        """
        incs = self.__repo_inchiriere.get_incs()
        fids = []
        for inc in incs:
            fid = inc.get_film().get_fid()
            if fids.count(fid) == 0:
                fids.append(fid)
        result = []
        for fid in fids:
            freq = 0
            for inc in incs:
                if inc.get_film().get_fid() == fid and inc.get_stare() == "Inchiriat":
                    freq += 1
            if freq > 0:
                titlu = self.__repo_film.find_id(fid).get_titlu()
                result.append([titlu, freq])
        result = sorted_custom(result, "shake", key=lambda x: x[1], reverse=True)
        return result

    def get_gen_incs(self):
        """
        service function - returneaza lista cu genurile de filme existente si inchirierile corespunzatoare fiecarui gen
        :return: lista de genuri + nr inchirieri
        """
        filme = self.__repo_film.get_filme()
        all_gen = []
        for film in filme:
            genuri = film.get_gen().split(", ")
            for gen in genuri:
                if gen not in all_gen:
                    all_gen.append(gen)
        incs = self.__repo_inchiriere.get_incs()
        all_incs = [0] * len(all_gen)
        for inc in incs:
            genuri = inc.get_film().get_gen().split(", ")
            for gen in genuri:
                for i in range(len(all_gen)):
                    if all_gen[i] == gen:
                        all_incs[i] += 1

        return all_gen, all_incs
