from controller.controller_produs import Controller
from repository.repository_produs import Repository
from ui.ui import meniu_produse
from teste.controller.teste_controller import test_srv

# repository file object
repo = Repository("produse.txt")

# controller object
srv = Controller(repo)

# ui object
meniu = meniu_produse(srv)

# run tests
test = test_srv()
test.run_srv_tests()

# start aplicatie
meniu.afisare()
