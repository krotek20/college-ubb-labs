"""
@@@ Vintila Radu @@@
"""
from domain.inchiriere_domain import Inchiriere


class exceptie_inchiriere_repo(Exception):
    pass


class repo_inchiriere:
    """
    clasa prin care se salveaza inchirieri in memorie
    """
    def __init__(self):
        self.__incs = {}

    def store(self, inc):
        """
        salvare inchirieri
        :param inc: inchiriere
        :raise exceptie_inchiriere_repo: daca exista o inchiriere cu acelasi ID
        """
        erori = []

        if inc.get_id() in self.__incs:
            erori.append("Exista deja o inchiriere cu acest ID!")

        if len(erori) > 0:
            raise exceptie_inchiriere_repo(erori)
        else:
            self.__incs[inc.get_id()] = inc

    def size(self):
        """
        numarul total de inchirieri din repository
        :return: numar intreg
        """
        return len(self.__incs)

    def returneaza_film(self, incid):
        """
        returneaza un film inchiriat de catre un client
        :param incid: int (ID inchiriere)
        :return: tuplu cid + fid
        :raise exceptie_inchiriere_repo: In cazul in care nu exista o inchiriere cu acest ID in repository!
        """
        if self.__incs[incid].get_stare() == "Returnat":
            raise exceptie_inchiriere_repo("Acest film a fost deja returnat")
        try:
            return self.__incs[incid].returneaza_film()
        except KeyError:
            raise exceptie_inchiriere_repo("Nu exista o inchiriere cu acest ID in repository!")

    def get_incs(self):
        """
        lista cu toate inchirierile
        """
        return list(self.__incs.values())

    def clear(self):
        """
        stergerea tuturor inchirierilor
        """
        self.__incs = {}


class repo_inchirieri_file(repo_inchiriere):
    def __init__(self, repo_client, repo_film, file_name):
        super().__init__()
        self.__repo_client = repo_client
        self.__repo_film = repo_film
        self.__path_file = "./repository/text_files/" + file_name
        self.__load_from_file()

    def __load_from_file(self):
        """
        Citeste toate inchirierile din fisier
        """
        try:
            file = open(self.__path_file, "r")
        except IOError:
            raise exceptie_inchiriere_repo("Eroare la deschiderea fisierului!")
        for line in file:
            elems = line.split("|")
            client = self.__repo_client.find_id(int(elems[1]))
            film = self.__repo_film.find_id(int(elems[2]))
            inc = Inchiriere(int(elems[0]), client, film, elems[3].strip())
            super().store(inc)
        file.close()

    def __store_to_file(self):
        """
        Adauga toate inchirierile in fisier
        """
        with open(self.__path_file, "w") as file:
            incs = super().get_incs()
            for inc in incs:
                inc_file = str(inc.get_id()) + "|" + str(inc.get_client().get_cid()) + "|"
                inc_file += str(inc.get_film().get_fid()) + "|" + inc.get_stare() + "\n"
                file.write(inc_file)

    def clear(self):
        """
        Sterge toate inchirierile din memorie si din fisier
        """
        super().clear()
        self.__store_to_file()

    def store(self, inc):
        """
        salvare inchiriere in memorie si in fisier
        :param inc: instanta de inchiriere
        """
        super().store(inc)
        self.__store_to_file()

    def returneaza_film(self, incid):
        """
        returneaza un film inchiriat de catre un client
        :param incid: int (inchiriere ID)
        """
        (client, film) = super().returneaza_film(incid)
        self.__store_to_file()
        return client, film

    def get_incs(self):
        """
        lista cu toate inchirierile
        """
        super().clear()
        self.__load_from_file()
        return super().get_incs()
