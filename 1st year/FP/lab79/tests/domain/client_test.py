"""
@@@ Vintila Radu @@@
"""
from domain.client_domain import Client
import unittest


class TestCaseClient(unittest.TestCase):
    def test_creeaza_client(self):
        """
        functie de testare pentru crearea unui client
        """
        client = Client(1, "Tomas", 500020034567)
        self.assertIsInstance(client, Client)
        self.assertEqual(client.get_cid(), 1)
        self.assertTrue(client.get_nume() == "Tomas")
        self.assertEqual(client.get_cnp(), 500020034567)

    def test_egalitate_client(self):
        """
        functie de testare a egalitatii dintre doi clienti
        """
        client1 = Client(1, "Tomas", 500020034567)
        client2 = Client(1, "Tomas", 500020034567)
        self.assertEqual(client1, client2)

    def test_string(self):
        """
        functie de testare pentru afisarea sub forma de string a unui client
        """
        client = Client(1, "Tomas", 500020034567)
        self.assertTrue(client.__str__() == "1 || Tomas || 500020034567")


def suite():
    s = unittest.TestSuite()
    l = unittest.TestLoader().loadTestsFromTestCase(TestCaseClient)
    s.addTests(l)
    return s
