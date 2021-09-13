from domain.Produs import Produs


class Controller:
    def __init__(self, repo):
        """
        Contructor service
        :param repo: Repository (instanta de repository)
        """
        self.__repo = repo
        self.__undo_list = []

    def creeaza_produs(self, pid, nume, pret):
        """
        Service function - creearea unui nou produs
        :param pid: int (ID produs)
        :param nume: string (denumire produs)
        :param pret: int (pret produs)
        :return: produs nou creat (entitate de Produs)
        """
        produs = Produs(pid, nume, pret)
        self.__repo.store(produs)
        return produs

    def sterge_produse(self, cifra):
        """
        Service function - stergerea produselor cu un ID care contine cifra data
        :param cifra: int (cifra intre 0 si 9)
        :return: contor - numarul de entitati sterse
        """
        contor = 0
        produse = self.__repo.get_produse()
        self.__undo_list = produse[:]
        for i in range(len(produse) - 1, -1, -1):
            if str(cifra) in str(produse[i].get_pid()):
                self.__repo.remove(produse[i])
                contor += 1
        return contor

    def get_produse_filtru(self, filtru):
        """
        Service function - preluare tuturor produselor dupa filtrul parsat
        :param filtru: tuplu (string,int) - denumire,pret
            ("", -1) - nu se doreste filtrare nici dupa denumire si nici dupa pret
        :return: lista de produse
        """
        new_produse = []
        produse = self.__repo.get_produse()
        if filtru[0] == "" and filtru[1] == -1:
            return produse
        else:
            for produs in produse:
                if filtru[0] in produs.get_nume() and produs.get_pret() >= filtru[1]:
                    new_produse.append(produs)

        return new_produse

    def undo_stergere(self):
        """
        Service function - refacerea listei inainte de ultima operatie de stergere
        :return: mesaj specific:
            Daca nu au fost facute stergeri inainte de undo - "Nu s-a facut nicio operatie de stergere!"
            Daca au fost facute stergeri inainte de undo - "Undo realizat!"
        """
        if not self.__undo_list:
            return "Nu s-a facut nicio operatie de stergere!"
        self.__repo.set_produse(self.__undo_list)
        return "Undo realizat!"
