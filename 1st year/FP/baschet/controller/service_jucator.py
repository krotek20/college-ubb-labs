from domain.jucator import Jucator


class srv_jucator:
    def __init__(self, val, repo):
        self.__val = val
        self.__repo = repo

    def creeaza_jucator(self, nume, prenume, inaltime, post):
        jucator = Jucator(nume, prenume, inaltime, post)
        self.__val.validate(jucator)
        self.__repo.store(jucator)
        return jucator

    def get_jucatori(self):
        return self.__repo.get_jucatori()

    def cauta_jucator(self, nume, prenume):
        return self.__repo.find(nume, prenume)

    def modifica_jucator(self, jucator, inaltime):
        self.__repo.update(jucator, inaltime)
