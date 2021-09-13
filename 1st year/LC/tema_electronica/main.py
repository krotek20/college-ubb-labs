# Autor : Vintila Radu - Florian

from UI import Meniu
from service import Service
from validator import validare

# validator object
val = validare()

# service object
srv = Service(val)

# meniu object
meniu = Meniu(srv)

# run application
meniu.afisare()
