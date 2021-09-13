"""
@@@ Vintila Radu @@@
"""

from domain.inchiriere_domain import Inchiriere
from domain.client_domain import Client
from domain.film_domain import Film
import unittest


class TestCaseInchiriere(unittest.TestCase):
    @staticmethod
    def set_up():
        """
        set up dummy data for tests
        :return: tuple of two Inchiriere instances
        """
        client1 = Client(1, "Vasile", 2)
        client2 = Client(2, "Ion", 3)
        film1 = Film(1, "Film", "Film bun", "actiune")
        film2 = Film(2, "Joker", "Bun film", "nu stiu")
        inc1 = Inchiriere(1, client1, film1, "Inchiriat")
        inc2 = Inchiriere(2, client2, film2, "Inchiriat")
        return inc1, inc2

    def test_creeaza_inchiriere(self):
        """
        functie de testare pentru crearea unei inchirieri
        """
        (inc1, inc2) = self.set_up()
        self.assertEqual(inc1.get_id(), 1)
        self.assertTrue(inc1.get_client().get_nume() == "Vasile")
        self.assertTrue(inc1.get_film().get_titlu() == "Film")
        self.assertTrue(inc1.get_stare() == "Inchiriat")
        inc1.returneaza_film()
        self.assertTrue(inc1.get_stare() == "Returnat")

    def test_egalitate_inchiriere(self):
        """
        functie de testare a egalitatii dintre doua inchirieri
        """
        (inc1, inc2) = self.set_up()
        inc3 = Inchiriere(1, Client(1, "", 2), Film(1, "", "", ""), "Inchiriat")
        self.assertEqual(inc1, inc3)
        self.assertNotEqual(inc1, inc2)

    def test_string(self):
        """
        functie de testare pentru afisarea sub forma de string a unei inchirieri
        """
        (inc1, inc2) = self.set_up()
        self.assertTrue(inc1.__str__() == "1 || Vasile || Film || Inchiriat")
        self.assertTrue(inc2.__str__() == "2 || Ion || Joker || Inchiriat")


def suite():
    s = unittest.TestSuite()
    l = unittest.TestLoader().loadTestsFromTestCase(TestCaseInchiriere)
    s.addTests(l)
    return s
