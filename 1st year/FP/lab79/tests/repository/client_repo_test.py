"""
@@@ Vintila Radu @@@
"""
from domain.client_domain import Client
from repository.client_repo import repo_client, exceptie_client_repo
import unittest


class TestCaseClientRepo(unittest.TestCase):
    def setUp(self):
        self.repo = repo_client()
        self.repo.store(Client(1, "Andrew", 1))
        self.repo.store(Client(2, "Tomas", 2))
        self.repo.store(Client(3, "John", 3))

    def test_store(self):
        """
        functia de testare pentru salvarea unui client
        """
        self.assertEqual(self.repo.size(), 3)
        self.assertTrue(self.repo.find_id(1) == Client(1, "Andrew", 1))
        self.assertRaises(exceptie_client_repo, self.repo.store, Client(1, "Tony", 600052342364))

    def test_get_clienti(self):
        """
        functia de testare pentru preluarea tuturor clientilor
        """
        lista = self.repo.get_clienti()
        self.assertEqual(len(lista), 3)

    def test_update(self):
        """
        functia de testare pentru modificarea unui client existent
        """
        clienti = self.repo.get_clienti()
        self.assertTrue(clienti[0].__str__() == "1 || Andrew || 1")
        self.repo.update(Client(2, "nume2", 3))
        clienti = self.repo.get_clienti()
        self.assertTrue(clienti[1].__str__() == "2 || nume2 || 3")

    def test_find(self):
        """
        functia de testare pentru cautare unui client dupa un anumit criteriu (ID / nume / CNP)
        """
        # test cautare dupa ID
        clienti = self.repo.find("ID", 2)
        self.assertTrue(clienti[0].__str__() == "2 || Tomas || 2")

        # test cautare dupa nume
        self.repo.store(Client(4, "John", 4))
        clienti = self.repo.find("nume", "John")
        self.assertTrue(clienti[0].__str__() == "3 || John || 3")
        self.assertTrue(clienti[1].__str__() == "4 || John || 4")

        # test cautare dupa CNP
        clienti = self.repo.find("CNP", 3)
        self.assertTrue(clienti[0].__str__() == "3 || John || 3")

    def test_remove(self):
        """
        functie de testare pentru stergerea unui client existent
        """
        self.repo.remove(1)
        self.assertEqual(self.repo.size(), 2)

    def test_clear(self):
        """
        functia de testare pentru stergerea tuturor clientilor
        """
        self.repo.clear()
        self.assertEqual(self.repo.size(), 0)


def suite():
    s = unittest.TestSuite()
    t = unittest.TestLoader().loadTestsFromTestCase(TestCaseClientRepo)
    s.addTests(t)
    return s
