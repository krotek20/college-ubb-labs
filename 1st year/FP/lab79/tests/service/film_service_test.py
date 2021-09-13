"""
@@@ Vintila Radu @@@
"""
from repository.film_repo import repo_film, exceptie_film_repo
from domain.film_validare import validare_film
from service.film_service import srv_film
import unittest


class TestCaseFilmService(unittest.TestCase):
    def setUp(self):
        self.rf = repo_film()
        self.val = validare_film()
        self.srv = srv_film(self.rf, self.val)

    def test_creeaza_film(self):
        """
        functie de testare pentru adaugarea unui film nou
        """
        film = self.srv.creeaza_film(1, "titlu", "desc", "gen")
        self.assertEqual(film.get_fid(), 1)
        self.assertTrue(film.get_titlu() == "titlu")
        self.assertTrue(film.get_desc() == "desc")
        self.assertTrue(film.get_gen() == "gen")
        all_filme = self.srv.get_all()
        self.assertEqual(len(all_filme), 1)
        self.assertTrue(all_filme[0] == film)
        self.assertRaises(exceptie_film_repo, self.srv.creeaza_film, 1, "titlu2", "desc2", "gen2")

    def test_sterge_film(self):
        """
        functie de testare pentru stergerea unui film existent
        """
        film1 = self.srv.creeaza_film(1, "titlu", "desc", "gen")
        film2 = self.srv.creeaza_film(2, "titlu2", "desc2", "gen2")
        self.assertEqual(len(self.srv.get_all()), 2)
        self.srv.sterge_film(1)
        self.assertEqual(len(self.srv.get_all()), 1)

    def test_sterge_all(self):
        """
        functie de testare pentru stergerea tuturor filmelor
        """
        film1 = self.srv.creeaza_film(1, "titlu", "desc", "gen")
        film2 = self.srv.creeaza_film(2, "titlu2", "desc2", "gen2")
        self.assertEqual(len(self.srv.get_all()), 2)
        self.srv.sterge_all()
        self.assertEqual(len(self.srv.get_all()), 0)

    def test_modifica_film(self):
        """
        functia de testare pentru modificarea unui film
        """
        film = self.srv.creeaza_film(1, "titlu", "desc", "gen")
        self.assertTrue(film.__str__() == "1 || titlu || desc || gen")
        self.srv.modifica_film(1, "titlu_nou", "desc_nou", "gen_nou")
        filme = self.srv.get_all()
        self.assertTrue(filme[0].__str__() == "1 || titlu_nou || desc_nou || gen_nou")

    def test_cauta_filme(self):
        """
        functia de testare pentru cautare unui film dupa un anumit criteriu (ID / titlu / descriere / gen)
        """
        film1 = self.srv.creeaza_film(1, "titlu", "desc", "gen")
        film2 = self.srv.creeaza_film(2, "titlu2", "desc2", "gen2")

        # test cautare dupa ID
        filme = self.srv.cauta_filme("id", 1)
        self.assertTrue(filme[0].__str__() == "1 || titlu || desc || gen")

        # test cautare dupa titlu
        filme = self.srv.cauta_filme("titlu", "titlu2")
        self.assertTrue(filme[0].__str__() == "2 || titlu2 || desc2 || gen2")

        # test cautare dupa descriere
        filme = self.srv.cauta_filme("desc", "desc")
        self.assertTrue(filme[0].__str__() == "1 || titlu || desc || gen")

        # test cautare dupa gen
        filme = self.srv.cauta_filme("gen", "gen2")
        self.assertTrue(filme[0].__str__() == "2 || titlu2 || desc2 || gen2")


def suite():
    s = unittest.TestSuite()
    t = unittest.TestLoader().loadTestsFromTestCase(TestCaseFilmService)
    s.addTests(t)
    return s
