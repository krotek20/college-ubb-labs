"""
@@@ Vintila Radu @@@
"""
from domain.inchiriere_domain import Inchiriere
from domain.inchiriere_validare import validare_inchiriere, exceptie_inchiriere
from domain.film_domain import Film
from domain.client_domain import Client
import unittest


class TestCaseInchiriereValidare(unittest.TestCase):
    def setUp(self):
        self.val = validare_inchiriere()

    def test_validare(self):
        """
        functie de testare pentru validarea unei inchirieri
        """
        client = Client(1, "Vasile", 2)
        film = Film(1, "Film", "Film bun", "actiune")
        inc = Inchiriere(1, client, film, "Inchiriat")
        self.assertIsInstance(inc, Inchiriere)
        inc = Inchiriere("", client, film, "Inchiriat")
        self.assertRaises(exceptie_inchiriere, self.val.validare, inc)
        inc = Inchiriere(-1, client, film, "Inchiriat")
        self.assertRaises(exceptie_inchiriere, self.val.validare, inc)


def suite():
    s = unittest.TestSuite()
    l = unittest.TestLoader().loadTestsFromTestCase(TestCaseInchiriereValidare)
    s.addTests(l)
    return s
