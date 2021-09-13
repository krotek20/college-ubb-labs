from UI.meniu_baschet import MeniuBaschet
from controller.service_jucator import srv_jucator
from domain.jucator_validare import validare_jucator
from repository.jucator_repository import repo_jucator_file


repo = repo_jucator_file("Jucatori.txt")
val = validare_jucator()
srv = srv_jucator(val, repo)
meniu = MeniuBaschet(srv)

meniu.afisare()
