"""
@@@ Vintila Radu @@@
"""
from domain.client_domain import Client
from domain.film_domain import Film
from domain.inchiriere_domain import Inchiriere
from repository.inchiriere_repo import repo_inchiriere, exceptie_inchiriere_repo
from repository.client_repo import repo_client
from repository.film_repo import repo_film
import unittest


class TestCaseInchiriereRepo(unittest.TestCase):
    def setUp(self):
        self.rc = repo_client()
        self.rf = repo_film()
        self.ri = repo_inchiriere()

        client1 = Client(1, "Tomas", 2)
        client2 = Client(2, "David", 3)
        self.rc.store(client1)
        self.rc.store(client2)

        film1 = Film(1, "titlu", "desc", "gen")
        film2 = Film(2, "titlu2", "desc", "gen")
        self.rf.store(film1)
        self.rf.store(film2)

        self.ri.store(Inchiriere(1, client1, film1, "Inchiriat"))
        self.ri.store(Inchiriere(2, client2, film2, "Inchiriat"))

    def test_store(self):
        """
        functia de testare pentru salvarea unei inchirieri
        """
        self.assertEqual(self.ri.size(), 2)
        inc = Inchiriere(1, self.rc.get_clienti()[1], self.rf.get_filme()[1], "Inchiriat")
        self.assertRaises(exceptie_inchiriere_repo, self.ri.store, inc)

    def test_get_incs(self):
        """
        functia de testare pentru preluarea tuturor inchirierilor
        """
        my_list = self.ri.get_incs()
        self.assertEqual(len(my_list), 2)

    def test_clear(self):
        """
        functia de testare pentru stergerea tuturor inchirierilor
        """
        self.ri.clear()
        self.assertEqual(self.ri.size(), 0)

    def test_returneaza_film(self):
        """
        functia de testare pentru returnarea unui film
        """
        incs = self.ri.get_incs()
        self.assertTrue(incs[0].get_stare() == "Inchiriat")
        self.ri.returneaza_film(1)
        self.assertTrue(incs[0].get_stare() == "Returnat")


def suite():
    s = unittest.TestSuite()
    t = unittest.TestLoader().loadTestsFromTestCase(TestCaseInchiriereRepo)
    s.addTests(t)
    return s
