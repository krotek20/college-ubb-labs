from teste.repository.teste_repo import test_repo
from controller.controller_produs import Controller
from repository.repository_produs import Repository


class test_srv:
    @staticmethod
    def testeaza_srv():
        """
        Testare service
        """
        repo = Repository("tmp.txt")
        repo.clear()

        srv = Controller(repo)
        produs = srv.creeaza_produs(12, "nume", 90)
        assert produs.get_pid() == 12
        assert produs.get_nume() == "nume"
        assert produs.get_pret() == 90

        produs2 = srv.creeaza_produs(13, "nume", 50)
        contor = srv.sterge_produse(1)
        assert contor == 2

        srv.undo_stergere()
        produse = repo.get_produse()
        assert len(produse) == 2

        produse = srv.get_produse_filtru(("", -1))
        assert len(produse) == 2

        produse = srv.get_produse_filtru(("", 60))
        assert len(produse) == 1

    @classmethod
    def run_srv_tests(cls):
        """
        Run service + repository tests
        """
        cls.testeaza_srv()
        test_repo.testeaza_repo()
