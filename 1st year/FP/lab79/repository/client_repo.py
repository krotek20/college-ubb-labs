"""
@@@ Vintila Radu @@@
"""
from domain.client_domain import Client


class exceptie_client_repo(Exception):
    pass


class repo_client:
    """
    clasa care salveaza clienti in memorie
    """

    def __init__(self):
        self.__clienti = {}

    def store(self, client):
        """
        salvare client in lista de clienti
        :param client: instanta de client
        :raise exceptie_client_repo: daca exista un client cu acelasi ID sau cu acelasi CNP
        """
        erori = []
        for cl in self.__clienti.values():
            if client.get_cid() == cl.get_cid():
                erori.append("Exista deja un client cu acest ID!")
            if client.get_cnp() == cl.get_cnp():
                erori.append("Exista deja un client cu acest CNP!")

        if len(erori) > 0:
            raise exceptie_client_repo(erori)
        else:
            self.__clienti[client.get_cid()] = client

    def size(self):
        """
        nuamrul total de __clienti din repository
        :return: numar intreg
        """

        return len(self.__clienti)

    def update(self, client):
        """
        update client
        :param client: instanta de client
        :exception exceptie_client_repo: Nu exista un client cu ID-ul specificat
        """
        try:
            self.__clienti[client.get_cid()] = client
        except KeyError:
            raise exceptie_client_repo("Nu exista un client cu acest ID!")

    def find(self, alegere, val):
        """
        find clienti
        :param alegere: string ( ID / nume / CNP )
        :param val: valoarea dupa care se face cautarea ( ID / nume / CNP)
        :return: lista clientilor gasiti
        """
        clienti = list(self.__clienti.values())
        clienti_gasiti = []
        for client in clienti:
            if alegere.lower() == "id" and client.get_cid() == val or \
                    alegere.lower() == "nume" and client.get_nume().lower() == val.lower() or \
                    alegere.lower() == "cnp" and client.get_cnp() == val:
                clienti_gasiti.append(client)
        return clienti_gasiti

    def find_id(self, cid):
        """
        find client by id
        :param cid: int (ID client)
        :return: client instance
        """
        clienti = list(self.__clienti.values())
        if cid not in self.__clienti:
            raise exceptie_client_repo("Nu exista un client cu acest ID in repository!")
        for client in clienti:
            if client.get_cid() == cid:
                return client

    def get_clienti(self):
        """
        functie de get
        :return: lista tuturor clientilor
        """

        return list(self.__clienti.values())

    def get_all_ids(self):
        """
        functie de get
        :return: lista cu toate id-urile clientilor
        """
        return self.__clienti

    def clear(self):
        """
        stergerea tuturor clientilor
        """

        self.__clienti.clear()

    def remove(self, cid):
        """
        stergerea unui client dupa un ID dat
        :param cid: int (ID client)
        """

        try:
            self.__clienti.pop(cid)
        except KeyError:
            raise exceptie_client_repo("Nu exista un client cu acest ID in repository!")


class repo_client_file(repo_client):
    def __init__(self, file_name):
        super().__init__()
        self.__path_file = "./repository/text_files/" + file_name
        self.__load_from_file()

    def __load_from_file(self):
        """
        Citeste toti clientii din fisier
        """
        try:
            file = open(self.__path_file, "r")
        except IOError:
            raise exceptie_client_repo("Eroare la deschiderea fisierului!")
        super().clear()
        for line in file:
            elems = line.split("|")
            client = Client(int(elems[0]), elems[1], int(elems[2]))
            super().store(client)
        file.close()

    def __store_to_file(self):
        """
        Adauga toti clientii in fisier
        """
        with open(self.__path_file, "w") as file:
            clienti = super().get_clienti()
            for client in clienti:
                client_file = str(client.get_cid()) + "|" + client.get_nume() + "|" + str(client.get_cnp()) + "\n"
                file.write(client_file)

    def clear(self):
        """
        Sterge toti clientii din memorie si din fisier
        """
        super().clear()
        self.__store_to_file()

    def store(self, client):
        """
        salvare client in memorie si in fisier
        :param client: instanta de client
        """
        super().store(client)
        self.__store_to_file()

    def update(self, client):
        """
        Modifica datele unui client existent
        :param client: instanta de client
        """
        super().update(client)
        self.__store_to_file()

    def remove(self, cid):
        """
        Sterge un client dupa ID
        :param cid: int (client ID)
        """
        super().remove(cid)
        self.__store_to_file()

    def get_clienti(self):
        """
        functie de get
        :return: lista tuturor clientilor
        """
        self.__load_from_file()
        return super().get_clienti()
