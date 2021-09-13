class exceptie_jucator(Exception):
    def __init__(self, erori):
        self.__erori = erori

    def get_erori(self):
        return self.__erori


class validare_jucator:
    @staticmethod
    def validate(jucator):
        erori = []
        if not jucator.get_nume():
            erori.append("Trebuie introdus un nume!")
        if not jucator.get_prenume():
            erori.append("Trebuie introdus un prenume!")
        if not type(jucator.get_inaltime()) is int or jucator.get_inaltime() <= 0:
            erori.append("Inaltimea trebuie sa fie un numar pozitiv!")
        if jucator.get_post() != "Fundas" and jucator.get_post() != "Pivot" and jucator.get_post() != "Extrema":
            erori.append("Nu exista un astfel de post!")

        if len(erori) > 0:
            raise exceptie_jucator(erori)
