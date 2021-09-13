from domain.Produs import Produs


class Repository:
    def __init__(self, file_name):
        self.__file_path = file_name
        self.__produse = []

    def __load_from_file(self):
        """
        Functia care incarca produsele din fisier intr-o lista din memorie (self.__produse)
        """
        with open(self.__file_path, "r") as file:
            self.__produse = []
            for line in file:
                elems = line.strip().split(";")
                produs = Produs(int(elems[0]), elems[1], int(elems[2]))
                self.__produse.append(produs)

    def __store_to_file(self):
        """
        Functia care salveaza in fisier produsele din memorie
        """
        with open(self.__file_path, "w") as file:
            for produs in self.__produse:
                file.write(produs.to_string())

    def store(self, produs):
        """
        Functia incarca fisierul in lista din memorie;
        stocheaza un nou produs in lista de produse din memorie;
        incarca lista din memorie, inapoi in fisier
        :param produs: Produs (instanta de produs nou creata)
        """
        self.__load_from_file()
        self.__produse.append(produs)
        self.__store_to_file()

    def remove(self, produs):
        """
        Functia sterge produsul parsat ca parametru din lista din memorie si se incarca in fisier lista nou obtinuta
        :param produs: Produs (instanta de produs)
        """
        if produs in self.__produse:
            self.__produse.remove(produs)
        self.__store_to_file()

    def clear(self):
        """
        Functia de steregere a intregii liste din fisier si din memorie
        """
        self.__produse = []
        self.__store_to_file()

    def get_produse(self):
        """
        Functia preia toate entitatile din fisier si le incarca in memorie
        :return: lista de produse din memorie
        """
        self.__load_from_file()
        return self.__produse

    def set_produse(self, undo_list):
        """
        Functia sterge toate produsele curente din lista din memorie si
        stocarea in memorie, respectiv in fisier, a produselor retinute in undo_list (lista inainte de ultima steregere)
        :param undo_list: lista de produse
        """
        self.__produse = []
        for produs in undo_list:
            self.__produse.append(produs)
        self.__store_to_file()
