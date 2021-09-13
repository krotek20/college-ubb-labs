class meniu_produse:
    def __init__(self, srv):
        """
        Contructor UI
        :param srv: Controller (instanta de controller)
        """
        self.__srv = srv
        self.cmds = {
            "1": self.__adauga_produs,
            "2": self.__sterge_produse,
            "3": self.__seteaza_filtru,
            "4": self.__undo_stergere
        }
        self.filtru = ("", -1)

    def __adauga_produs(self):
        """
        Introducerea valorilor pentru adaugarea unui nou produs si afisarea sa ulterioara
        """
        pid = int(input("Introduceti ID: "))
        nume = input("Introduceti nume: ")
        pret = int(input("Introduceti pret: "))
        produs = self.__srv.creeaza_produs(pid, nume, pret)
        print("Produsul " + produs.get_nume() + " a fost adaugat cu succes!")

    def __sterge_produse(self):
        """
        Introducerea cifrei pentru care produsele a caror ID contin aceasta cifra vor fi sterse
        """
        cifra = int(input("Introduceti cifra: "))
        contor = self.__srv.sterge_produse(cifra)
        print("Au fost sterse " + str(contor) + " produse!")

    def afisare_filtru(self):
        """
        Afisarea filtrului curent si listei de produse filtrate
        """
        if self.filtru[0] == "":
            print("Filtru vid " + str(self.filtru[1]))
        else:
            print("Filtru " + self.filtru[0] + " " + str(self.filtru[1]))
        produse = self.__srv.get_produse_filtru(self.filtru)
        for produs in produse:
            print(produs)

    def __seteaza_filtru(self):
        """
        Setarea unui nou filtru
        """
        self.filtru = (input("Introduceti denumire: "), int(input("Intrudeti pret: ")))
        self.afisare_filtru()

    def __undo_stergere(self):
        """
        Undo ultimei operatii de stergere
        """
        mesaj = self.__srv.undo_stergere()
        print(mesaj)

    def afisare(self):
        """
        Functia de afisare a meniului principal
        """
        self.afisare_filtru()
        while True:
            meniu = ('''
1. Adauga produs
2. Sterge produse
3. Setare filtru
4. Undo stergere
0. Iesire aplicatie
            ''')

            cmd = input(">>> ")

            if cmd == "0":
                print("Good bye!")
                return
            elif cmd == "meniu":
                print(meniu)
                print("------------")
                self.afisare_filtru()
            elif cmd in self.cmds:
                try:
                    self.cmds[cmd]()
                except ValueError as ve:
                    print("Value error\n" + str(ve))
            else:
                print("Comanda invalida!")
