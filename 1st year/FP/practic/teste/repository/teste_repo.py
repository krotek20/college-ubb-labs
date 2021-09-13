from teste.domain.teste_produs import test_produs
from repository.repository_produs import Repository
from domain.Produs import Produs


class test_repo:
    @staticmethod
    def testeaza_repo():
        """
        Testare repository
        """
        repo = Repository("tmp.txt")
        repo.clear()
        produse = repo.get_produse()
        assert len(produse) == 0

        produs1 = Produs(21, "nume", 20)
        produs2 = Produs(20, "cartofi", 10)
        repo.store(produs1)
        repo.store(produs2)
        assert len(repo.get_produse()) == 2
        undo = repo.get_produse()

        repo.remove(repo.get_produse()[1])
        repo.remove(repo.get_produse()[0])
        assert len(repo.get_produse()) == 0

        repo.set_produse(undo)
        assert len(repo.get_produse()) == 2

    @classmethod
    def run_repo_tests(cls):
        """
        Run repository + domain tests
        """
        cls.testeaza_repo()
        test_produs.run_test()
