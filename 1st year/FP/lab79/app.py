"""
@@@ Vintila Radu @@@
"""

from repository.client_repo import repo_client, repo_client_file
from repository.film_repo import repo_film, repo_film_file
from repository.inchiriere_repo import repo_inchiriere, repo_inchirieri_file
from domain.client_validare import validare_client
from domain.film_validare import validare_film
from domain.inchiriere_validare import validare_inchiriere
from service.client_service import srv_client
from service.film_service import srv_film
from service.inchiriere_service import srv_inchiriere
from UI.console import Console

# Repositories
rc = repo_client()
rf = repo_film()
ri = repo_inchiriere()

# Repositories (files)
rcf = repo_client_file("Clienti.txt")
rff = repo_film_file("Filme.txt")
rif = repo_inchirieri_file(rcf, rff, "Inchirieri.txt")

# Validators
vc = validare_client()
vf = validare_film()
vi = validare_inchiriere()

# Services
sc = srv_client(rcf, vc)
sf = srv_film(rff, vf)
si = srv_inchiriere(rcf, rff, rif, vi)

# Main UI console
ui = Console(sc, sf, si)

# application start
ui.show()
