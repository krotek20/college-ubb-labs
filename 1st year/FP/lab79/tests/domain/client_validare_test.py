"""
@@@ Vintila Radu @@@
"""
from domain.client_domain import Client
from domain.client_validare import validare_client, exceptie_client
import unittest


class TestCaseClientValidare(unittest.TestCase):
    def setUp(self):
        self.val = validare_client()

    def test_validare(self):
        """
        functie de testare pentru validarea unui client
        """
        self.val.validare(Client(1, "Tomas", 500020034567))
        self.assertRaises(exceptie_client, self.val.validare, Client(-1, "Tomas", 500020034567))
        self.assertRaises(exceptie_client, self.val.validare, Client("", "Tomas", 500020034567))
        self.assertRaises(exceptie_client, self.val.validare, Client(1, "", 500020034567))
        self.assertRaises(exceptie_client, self.val.validare, Client(1, "Tomas", ""))


def suite():
    s = unittest.TestSuite()
    l = unittest.TestLoader().loadTestsFromTestCase(TestCaseClientValidare)
    s.addTests(l)
    return s
