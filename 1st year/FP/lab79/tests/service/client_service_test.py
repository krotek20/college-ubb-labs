"""
@@@ Vintila Radu @@@
"""
from repository.client_repo import repo_client, exceptie_client_repo
from domain.client_validare import validare_client
from service.client_service import srv_client
import unittest


class TestCaseClientService(unittest.TestCase):
    def setUp(self):
        self.rc = repo_client()
        self.val = validare_client()
        self.srv = srv_client(self.rc, self.val)

    def test_creeaza_client(self):
        """
        functie de testare pentru adaugarea unui client nou
        """
        client = self.srv.creeaza_client(1, "nume", 2)
        self.assertEqual(client.get_cid(), 1)
        self.assertTrue(client.get_nume() == "nume")
        self.assertEqual(client.get_cnp(), 2)
        all_clienti = self.srv.get_all()
        self.assertEqual(len(all_clienti), 1)
        self.assertTrue(all_clienti[0] == client)
        self.assertRaises(exceptie_client_repo, self.srv.creeaza_client, 1, "nume2", 3)

    def test_sterge_client(self):
        """
        functie de testare pentru stergerea unui client existent
        """
        client1 = self.srv.creeaza_client(1, "nume", 2)
        client2 = self.srv.creeaza_client(2, "nume2", 3)
        self.assertEqual(len(self.srv.get_all()), 2)
        self.srv.sterge_client(1)
        self.assertEqual(len(self.srv.get_all()), 1)

    def test_sterge_all(self):
        """
        functie de testare pentru stergerea tuturor clientilor
        """
        client1 = self.srv.creeaza_client(1, "nume", 2)
        client2 = self.srv.creeaza_client(2, "nume2", 3)
        self.assertEqual(len(self.srv.get_all()), 2)
        self.srv.sterge_all()
        self.assertEqual(len(self.srv.get_all()), 0)

    def test_modifica_client(self):
        """
        functia de testare pentru modificarea unui client existent
        """
        client = self.srv.creeaza_client(1, "nume", 2)
        self.assertTrue(client.__str__() == "1 || nume || 2")
        self.srv.modifica_client(1, "nume_nou", 3)
        clienti = self.srv.get_all()
        self.assertTrue(clienti[0].__str__() == "1 || nume_nou || 3")

    def test_cauta_clienti(self):
        """
        functia de testare pentru cautarea clientilor
        """
        client1 = self.srv.creeaza_client(1, "nume", 2)
        client2 = self.srv.creeaza_client(2, "nume2", 3)

        # test cautare dupa ID
        clienti = self.srv.cauta_clienti("id", 2)
        self.assertTrue(clienti[0].__str__() == "2 || nume2 || 3")

        # test cautare dupa nume
        clienti = self.srv.cauta_clienti("nume", "nume")
        self.assertTrue(clienti[0].__str__() == "1 || nume || 2")

        # test cautare dupa CNP
        clienti = self.srv.cauta_clienti("cnp", 2)
        self.assertTrue(clienti[0].__str__() == "1 || nume || 2")


def suite():
    s = unittest.TestSuite()
    t = unittest.TestLoader().loadTestsFromTestCase(TestCaseClientService)
    s.addTests(t)
    return s
