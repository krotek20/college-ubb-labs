"""
@@@ Vintila Radu @@@
"""


class exceptie_client(Exception):
    def __init__(self, erori):
        self.erori = erori

    def get_erori(self):
        return self.erori


class validare_client:

    @staticmethod
    def validare(client):
        """
        functia care verifica validitatea unui client
        :raise exceptie_client: Oricare dintre string-urile de mai jos
        """

        erori = []
        if not client.get_cid():
            erori.append("Trebuie introdus un ID!")
        if not type(client.get_cid()) is int or client.get_cid() < 0:
            erori.append("ID-ul clientului trebuie sa fie un numar intreg mai mare sau egal decat 1!")
        if not client.get_nume():
            erori.append("Trebuie introdus un nume!")
        if not client.get_cnp():
            erori.append("Trebuie introdus un CNP!")
        if not type(client.get_cnp()) is int or client.get_cnp() < 0:
            erori.append("CNP-ul clientului trebuie sa fie numar intreg!")

        if len(erori) > 0:
            raise exceptie_client(erori)
