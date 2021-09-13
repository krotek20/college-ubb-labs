from domain.Produs import Produs


class test_produs:
    @staticmethod
    def testeaza_produs():
        """
        Testarea unui Produs
        """
        produs = Produs(12, "nume", 20)
        assert produs.get_pid() == 12
        assert produs.get_nume() == "nume"
        assert produs.get_pret() == 20
        assert produs.__str__() == "12 nume 20"

    @classmethod
    def run_test(cls):
        """
        concat tests
        """
        cls.testeaza_produs()
