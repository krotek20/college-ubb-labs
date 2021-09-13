'''
Created on Jan 29, 2020

@author: Alex
'''
import unittest
from domain.produs import Produs
from infrastructura.repo import Repo
from business.service import ServiceProduse
class TesteDomain(unittest.TestCase):
    '''
    clasa pentru teste pentru domain
    '''
    def testProduse(self):
        '''
        test pentru setteri si getteri din clasa Produs
        in: -
        out: -
        '''
        produs = Produs(1, "nuci", 5)
        self.assertEqual(produs.get_id(), 1)
        self.assertEqual(produs.get_denumire(), "nuci")
        self.assertEqual(produs.get_pret(), 5)
        produs.set_denumire("ciocolata")
        self.assertEqual(produs.get_denumire(), "ciocolata")
        produs.set_pret(6)
        self.assertEqual(produs.get_pret(), 6)
        
class TesteRepo(unittest.TestCase):
    '''
    clasa de teste pentru repo
    '''
    def setUp(self):
        with open("tmp.txt", "w") as f: #creare fisier
            pass
        self.repo = Repo("tmp.txt", Produs.readProdus, Produs.writeProdus)
    
    def tearDown(self):
        with open("tmp.txt", "w") as f: #golire fisier
            pass
        
    def testAdauga(self):
        '''
        functie test pentru adaugare
        in: -
        out: -
        '''
        self.repo.adaugaEntitate(Produs(1, "nuci", 5))
        el = self.repo.getAll()[0]
        self.assertEqual(len(self.repo.getAll()), 1)
        self.assertEqual(el.get_id(), 1)
        self.assertEqual(el.get_denumire(), "nuci")
        self.assertEqual(el.get_pret(), 5)
        self.assertEqual(el, Produs(1, "nuci", 5))
        self.assertEqual(self.repo.getAll(), [Produs(1, "nuci", 5)])
        self.repo.adaugaEntitate(Produs(2, "ciocolata", 10))
        self.assertEqual(self.repo.getAll(), [Produs(1, "nuci", 5), Produs(2, "ciocolata", 10)])
        
    def testSterge(self):
        '''
        functie test pentru stergere
        in: -
        out: -
        '''
        self.repo.adaugaEntitate(Produs(1, "nuci", 5))
        self.repo.stergeEntitate(Produs(1, "nuci", 5))
        self.assertEqual(self.repo.getAll(), [])
        self.repo.adaugaEntitate(Produs(1, "nuci", 5))
        self.repo.adaugaEntitate(Produs(2, "ciocolata", 2))
        self.repo.stergeEntitate(Produs(1, "nuci", 5))
        self.assertEqual(self.repo.getAll(), [Produs(2, "ciocolata", 2)])
    
        
class TesteService(unittest.TestCase):
    '''
    clasa de teste pentru service
    '''
    def setUp(self):
        with open("tmp.txt", "w") as f: #creare fisier
            pass
        self.repo = Repo("tmp.txt", Produs.readProdus, Produs.writeProdus)
        self.service = ServiceProduse(self.repo)
    
    def tearDown(self):
        with open("tmp.txt", "w") as f: #golire fisier
            pass
    
    def testAdauga(self):
        '''
        functie test pentru adaugare
        in: -
        out: -
        '''
        self.service.adaugaProdus(Produs(1, "nuci", 5))
        el = self.repo.getAll()[0]
        self.assertEqual(len(self.repo.getAll()), 1)
        self.assertEqual(el.get_id(), 1)
        self.assertEqual(el.get_denumire(), "nuci")
        self.assertEqual(el.get_pret(), 5)
        self.assertEqual(el, Produs(1, "nuci", 5))
        self.assertEqual(self.repo.getAll(), [Produs(1, "nuci", 5)])
        self.service.adaugaProdus(Produs(2, "ciocolata", 10))
        self.assertEqual(self.repo.getAll(), [Produs(1, "nuci", 5), Produs(2, "ciocolata", 10)])
        
    def testStergeCifra(self):
        '''
        functie test pentru sterge element cu cifra din service
        in: -
        out: -
        '''
        self.service.adaugaProdus(Produs(4, "pizza", 21))
        self.service.adaugaProdus(Produs(12, "nuci", 5))
        self.service.adaugaProdus(Produs(21, "ciocolata", 6))
        self.service.adaugaProdus(Produs(22, "napolitana", 7))
        self.assertEqual(self.service.stergeProduseCifra(1), 2)
        self.assertEqual(self.repo.getAll(), [Produs(4, "pizza", 21), Produs(22, "napolitana", 7)])
        self.assertEqual(self.service.stergeProduseCifra(5), 0)
        
    def testUndo(self):
        '''
        functie test pentru undo
        in: -
        out: -
        '''
        self.service.adaugaProdus(Produs(4, "pizza", 21))
        self.service.adaugaProdus(Produs(12, "nuci", 5))
        self.service.adaugaProdus(Produs(21, "ciocolata", 6))
        self.service.adaugaProdus(Produs(22, "napolitana", 7))
        self.service.stergeProduseCifra(1)
        self.service.undo()
        self.assertEqual(self.service.getRepo().getAll(), [Produs(4, "pizza", 21), Produs(22, "napolitana", 7), Produs(12, "nuci", 5), Produs(21, "ciocolata", 6)])
        