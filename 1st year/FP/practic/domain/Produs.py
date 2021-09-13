class Produs:
    """
    Clasa abstracta pentru produse
    """
    def __init__(self, pid, nume, pret):
        """
        Constructor clasa Produs
        :param pid: int (ID produs)
        :param nume: string (denumire produs)
        :param pret: int (pret produs)
        """
        self.__pid = pid
        self.__nume = nume
        self.__pret = pret

    def get_pid(self):
        """
        Functie de get pentru ID produs
        :return: int (ID produs)
        """
        return self.__pid

    def get_nume(self):
        """
        Functie de get pentru nume produs
        :return: string (nume produs)
        """
        return self.__nume

    def get_pret(self):
        """
        Functie de get pentru pretul produsului
        :return: int (pret produs)
        """
        return self.__pret

    def __str__(self):
        """
        Convert Produs to string (pentru afisarea pe ecran)
        :return: string
        """
        return str(self.__pid) + " " + self.__nume + " " + str(self.__pret)

    def to_string(self):
        """
        Convert Produs to string (pentru scriere in fisier)
        :return: string
        """
        return "{};{};{}\n".format(self.__pid, self.__nume, self.__pret)
