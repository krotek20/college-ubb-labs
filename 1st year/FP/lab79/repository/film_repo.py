"""
@@@ Vintila Radu @@@
"""
from domain.film_domain import Film


class exceptie_film_repo(Exception):
    pass


class repo_film:
    """
    clasa care salveaza filme in memorie
    """

    def __init__(self):
        self.__filme = {}

    def store(self, film):
        """
        salvare __filme
        :param film: instanta de film
        :raise exceptie_film_repo: Daca exista un film cu acelasi ID
        """

        erori = []
        if film.get_fid() in self.__filme:
            erori.append("Exista deja un film cu acest ID!")

        if len(erori) > 0:
            raise exceptie_film_repo(erori)
        else:
            self.__filme[film.get_fid()] = film

    def size(self):
        """
        numarul total de __filme din repository
        :return: numar intreg
        """
        return len(self.__filme)

    def update(self, film):
        """
        update film
        :param film: instanta de film
        :exception exceptie_film_repo: Nu exista un film cu ID-ul specificat
        """
        try:
            self.__filme[film.get_fid()] = film
        except KeyError:
            raise exceptie_film_repo("Nu exista un film cu acest ID!")

    def find(self, alegere, val):
        """
        find filme
        :param alegere: string ( ID / titlu / desc / gen )
        :param val: valoarea dupa care se face cautarea ( ID / titlu / desc / gen)
        :return: lista filmelor gasite
        """
        filme = list(self.__filme.values())
        filme_gasite = []
        for film in filme:
            if alegere.lower() == "id" and film.get_fid() == val or \
               alegere.lower() == "titlu" and film.get_titlu().lower() == val.lower() or \
               alegere.lower() == "gen" and film.get_gen().lower() == val.lower():
                filme_gasite.append(film)
            elif alegere.lower() == "desc":
                vals = val.lower().split()
                des = film.get_desc().lower().split()
                result = all(items in des for items in vals)
                if result:
                    filme_gasite.append(film)
        return filme_gasite

    def find_id(self, fid):
        """
        find film by id
        :param fid: int (ID film)
        :return: film instance
        """
        filme = list(self.__filme.values())
        if fid not in self.__filme:
            raise exceptie_film_repo("Nu exista un film cu acest ID in repository!")
        for film in filme:
            if film.get_fid() == fid:
                return film

    def get_filme(self):
        """
        functie de get
        :return: lista tuturor filmelor din repozitory
        """
        return list(self.__filme.values())

    def get_all_ids(self):
        """
        functie de get
        :return: lista cu toate id-urile filmelor
        """
        return self.__filme

    def clear(self):
        """
        stergerea tuturor filmelor
        """
        self.__filme = {}

    def remove(self, fid):
        """
        stergerea unui film dupa un ID dat
        :param fid: int (ID film)
        """

        try:
            self.__filme.pop(fid)
        except KeyError:
            raise exceptie_film_repo("Nu exista un film cu acest ID in repository!")


class repo_film_file(repo_film):
    def __init__(self, file_name):
        super().__init__()
        self.__path_file = "./repository/text_files/" + file_name
        self.__load_from_file()

    def __load_from_file(self):
        """
        Citeste toate filmele din fisier
        """
        try:
            file = open(self.__path_file, "r")
        except IOError:
            raise exceptie_film_repo("Eroare la deschiderea fisierului!")
        for line in file:
            elems = line.split("|")
            film = Film(int(elems[0]), elems[1], elems[2], elems[3])
            super().store(film)
        file.close()

    def __store_to_file(self):
        """
        Adauga toate filmele in fisier
        """
        with open(self.__path_file, "w") as file:
            filme = super().get_filme()
            for film in filme:
                film_file = str(film.get_fid()) + "|" + film.get_titlu() + "|"
                film_file += film.get_desc() + "|" + film.get_gen() + "\n"
                file.write(film_file)

    def clear(self):
        """
        Sterge toate filmele din memorie si din fisier
        """
        super().clear()
        self.__store_to_file()

    def store(self, film):
        """
        salvare film in memorie si in fisier
        :param film: instanta de film
        """
        super().store(film)
        self.__store_to_file()

    def update(self, film):
        """
        Modifica datele unui film existent
        :param film: instanta de film
        """
        super().update(film)
        self.__store_to_file()

    def remove(self, fid):
        """
        Sterge un film dupa ID
        :param fid: int (film ID)
        """
        super().remove(fid)
        self.__store_to_file()

    def get_filme(self):
        """
        functie de get
        :return: lista tuturor filmelor din repozitory
        """
        super().clear()
        self.__load_from_file()
        return super().get_filme()
