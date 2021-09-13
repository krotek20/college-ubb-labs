"""
@@@ Vintila Radu @@@
"""
from domain.client_domain import Client
from domain.film_domain import Film
from domain.inchiriere_validare import validare_inchiriere
from repository.client_repo import repo_client
from repository.film_repo import repo_film
from repository.inchiriere_repo import repo_inchiriere
from service.inchiriere_service import srv_inchiriere
import unittest


class TestCaseInchiriereService(unittest.TestCase):
    def setUp(self):
        self.rc = repo_client()
        self.rf = repo_film()
        self.ri = repo_inchiriere()
        self.val = validare_inchiriere()

        self.rc.store(Client(1, "Andrew", 1))
        self.rc.store(Client(2, "Tomas", 2))
        self.rf.store(Film(1, "Titlu1", "Desc1", "Gen1"))
        self.rf.store(Film(2, "Titlu2", "Desc2", "Gen2"))

        self.srv = srv_inchiriere(self.rc, self.rf, self.ri, self.val)

    def test_creeaza_inchiriere(self):
        """
        functie de testare pentru crearea unei inchirieri
        """
        inc = self.srv.creeaza_inchiriere(1, 1, 1)
        self.assertEqual(inc.get_id(), 1)
        self.assertEqual(inc.get_client().get_cid(), 1)
        self.assertEqual(inc.get_film().get_fid(), 1)
        incs = self.srv.get_all()
        self.assertEqual(len(incs), 1)
        self.assertTrue(incs[0] == inc)

    def test_returneaza_film(self):
        """
        functia de testare pentru returnarea unui film
        """
        inc = self.srv.creeaza_inchiriere(1, 1, 1)
        incs = self.srv.get_all()
        self.assertTrue(incs[0].get_stare() == "Inchiriat")
        (client, film) = self.srv.returneaza_film(1)
        self.assertEqual(client.get_cid(), 1)
        self.assertEqual(film.get_fid(), 1)
        self.assertTrue(incs[0].get_stare() == "Returnat")

    def test_remove_all(self):
        """
        functia de testare pentru stergerea tuturor inchirierilor
        """
        inc1 = self.srv.creeaza_inchiriere(1, 1, 1)
        inc2 = self.srv.creeaza_inchiriere(2, 2, 2)
        self.assertEqual(len(self.srv.get_all()), 2)
        self.srv.remove_all()
        self.assertEqual(len(self.srv.get_all()), 0)

    def test_get_clienti_dupa_nume(self):
        """
        functia de testare pentru raport (lista clientilor care au inchiriat filme ordonata dupa nume)
        """
        inc1 = self.srv.creeaza_inchiriere(1, 1, 1)
        inc2 = self.srv.creeaza_inchiriere(2, 2, 2)

        clienti = self.srv.get_clienti_dupa_nume()
        self.assertTrue(clienti[0].get_nume() == "Andrew")
        self.assertTrue(clienti[1].get_nume() == "Tomas")

    def test_get_clienti_dupa_numar(self):
        """
        functia de testare pentru raport
        (lista clientilor care au inchiriat filme ordonata dupa numarul de filme inchiriate)
        """
        inc1 = self.srv.creeaza_inchiriere(1, 1, 1)
        inc2 = self.srv.creeaza_inchiriere(2, 2, 2)
        inc2 = self.srv.creeaza_inchiriere(3, 2, 1)

        (clienti, freq) = self.srv.get_clienti_dupa_numar()
        self.assertTrue(clienti[0].get_nume() == "Tomas")
        self.assertEqual(freq[0], 2)
        self.assertTrue(clienti[1].get_nume() == "Andrew")
        self.assertEqual(freq[1], 1)

    def test_get_top_filme_inchiriate(self):
        """
        functia de testare pentru raport (top 5 filme inchiriate)
        """
        inc1 = self.srv.creeaza_inchiriere(1, 1, 1)
        inc2 = self.srv.creeaza_inchiriere(2, 2, 2)
        inc2 = self.srv.creeaza_inchiriere(3, 2, 1)

        filme = self.srv.get_top_filme_inchiriate()
        self.assertTrue(filme[0].get_titlu() == "Titlu1")
        self.assertTrue(filme[1].get_titlu() == "Titlu2")


def suite():
    s = unittest.TestSuite()
    t = unittest.TestLoader().loadTestsFromTestCase(TestCaseInchiriereService)
    s.addTests(t)
    return s
