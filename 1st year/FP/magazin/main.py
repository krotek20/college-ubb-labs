'''
Created on Jan 29, 2020

@author: Alex
'''
from domain.produs import Produs
from prezentare.ui import UI
from business.service import ServiceProduse
from infrastructura.repo import Repo

repo = Repo("produse.txt", Produs.readProdus, Produs.writeProdus)
service = ServiceProduse(repo)
ui = UI(service)
ui.run()