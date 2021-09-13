"""
@@@ Vintila Radu @@@
"""
from domain.film_domain import Film
from domain.film_validare import validare_film, exceptie_film
import unittest


class TestCaseFilmValidare(unittest.TestCase):
    def setUp(self):
        self.val = validare_film()

    def test_validare(self):
        """
        functie de testare pentru validarea unui film
        """
        self.val.validare(Film(1, "Legend", "This movie is legendary", "action"))
        self.assertRaises(exceptie_film, self.val.validare, Film(-1, "f", "f", "f"))
        self.assertRaises(exceptie_film, self.val.validare, Film("", "f", "f", "f"))
        self.assertRaises(exceptie_film, self.val.validare, Film(1, "", "f", "f"))
        self.assertRaises(exceptie_film, self.val.validare, Film(1, "f", "", "f"))
        self.assertRaises(exceptie_film, self.val.validare, Film(1, "f", "f", ""))


def suite():
    s = unittest.TestSuite()
    t = unittest.TestLoader().loadTestsFromTestCase(TestCaseFilmValidare)
    s.addTests(t)
    return s
