"""
@@@ Vintila Radu @@@
"""
from domain.film_domain import Film
import unittest


class TestCaseFilm(unittest.TestCase):
    def test_creeaza_film(self):
        """
        functie de testare pentru crearea unui film
        """
        film = Film(1, "Legend", "This movie is legendary", "action")
        self.assertIsInstance(film, Film)
        self.assertEqual(film.get_fid(), 1)
        self.assertTrue(film.get_titlu() == "Legend")
        self.assertTrue(film.get_desc() == "This movie is legendary")
        self.assertTrue(film.get_gen() == "action")

    def test_egalitate_film(self):
        """
        functie de testare a egalitatii dintre doua filme
        """
        film1 = Film(1, "Legend", "This movie is legendary", "action")
        film2 = Film(1, "Legend", "This movie is legendary", "action")
        self.assertEqual(film1, film2)

    def test_string(self):
        """
        functie de testare pentru afisarea sub forma de string a unui film
        """
        film = Film(1, "Legend", "This movie is legendary", "action")
        self.assertTrue(film.__str__() == "1 || Legend || This movie is legendary || action")


def suite():
    s = unittest.TestSuite()
    l = unittest.TestLoader().loadTestsFromTestCase(TestCaseFilm)
    s.addTests(l)
    return s
