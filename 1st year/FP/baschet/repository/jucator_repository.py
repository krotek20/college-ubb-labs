from domain.jucator import Jucator
from domain.jucator_validare import validare_jucator


class exceptie_repo(Exception):
    pass


class repo_jucator:
    def __init__(self):
        self.__jucatori = []

    def store(self, jucator):
        self.__jucatori.append(jucator)

    def update(self, jucator, inaltime):
        for i in range(len(self.__jucatori)):
            if self.__jucatori[i] == jucator:
                self.__jucatori[i].set_inaltime(inaltime)

    def clear(self):
        self.__jucatori = []

    def get_jucatori(self):
        return self.__jucatori

    def find(self, nume, prenume):
        for jucator in self.__jucatori:
            if jucator.get_nume() == nume and jucator.get_prenume() == prenume:
                return jucator
        return None


class repo_jucator_file(repo_jucator):
    def __init__(self, file_name):
        super().__init__()
        self.__file_path = file_name
        self.__load_from_file()

    def __load_from_file(self):
        try:
            file = open(self.__file_path, "r")
        except IOError:
            raise exceptie_repo("Eroare la deschiderea fisierului!")

        val = validare_jucator()
        super().clear()
        for line in file:
            elems = line.split()
            jucator = Jucator(elems[0], elems[1], int(elems[3]), elems[2])
            val.validate(jucator)
            super().store(jucator)
        file.close()

    def __store_to_file(self):
        with open(self.__file_path, "w") as file:
            jucatori = super().get_jucatori()
            for jucator in jucatori:
                jucator_file = jucator.__str__() + '\n'
                file.write(jucator_file)

    def store(self, jucator):
        super().store(jucator)
        self.__store_to_file()

    def update(self, jucator, inaltime):
        super().update(jucator, inaltime)
        self.__store_to_file()
