"""
@@@ Vintila Radu @@@
"""
from domain.film_domain import Film
from repository.film_repo import repo_film, exceptie_film_repo
import unittest


class TestCaseFilmRepo(unittest.TestCase):
    def setUp(self):
        """
        setarea unor date dummy pentru teste
        :return: repository instance
        """
        self.repo = repo_film()
        self.repo.store(Film(1, "Titlu1", "Desc1", "Gen1"))
        self.repo.store(Film(2, "Titlu2", "Desc2", "Gen2"))
        self.repo.store(Film(3, "Titlu3", "Desc3", "Gen3"))

    def test_store(self):
        """
        functia de testare pentru salvarea unui film
        """
        film4 = Film(4, "Titlu4", "Desc4", "Gen4")
        self.repo.store(film4)
        self.assertEqual(self.repo.size(), 4)
        self.assertRaises(exceptie_film_repo, self.repo.store, Film(4, "Titlu5", "Desc5", "Gen5"))

    def test_get_filme(self):
        """
        functia de testare pentru preluarea tuturor filmelor
        """
        my_list = self.repo.get_filme()
        self.assertEqual(len(my_list), 3)

    def test_clear(self):
        """
        functia de testare pentru stergerea tuturor filmelor
        """
        self.repo.clear()
        self.assertEqual(self.repo.size(), 0)

    def test_update(self):
        """
        functia de testare pentru modificarea unui film
        """
        film = Film(1, "titlu", "desc", "gen")
        self.repo.update(film)
        filme = self.repo.get_filme()
        self.assertTrue(filme[0].__str__() == "1 || titlu || desc || gen")

    def test_find(self):
        """
        functia de testare pentru cautare unui film dupa un anumit criteriu (ID / titlu / descriere / gen)
        """
        # test cautare dupa ID
        filme = self.repo.find("id", 1)
        self.assertTrue(filme[0].__str__() == "1 || Titlu1 || Desc1 || Gen1")

        # test cautare dupa titlu
        film = Film(4, "Titlu1", "desc", "gen")
        self.repo.store(film)
        filme = self.repo.find("titlu", "titlu1")
        self.assertTrue(filme[0].__str__() == "1 || Titlu1 || Desc1 || Gen1")
        self.assertTrue(filme[1].__str__() == "4 || Titlu1 || desc || gen")

        # test cautare dupa descriere
        film = Film(5, "Titlu1", "Cel mai bun desc", "gen")
        self.repo.store(film)
        filme = self.repo.find("desc", "mai desc")
        self.assertTrue(filme[0].__str__() == "5 || Titlu1 || Cel mai bun desc || gen")

        # test cautare dupa gen
        filme = self.repo.find("gen", "gen2")
        self.assertTrue(filme[0].__str__() == "2 || Titlu2 || Desc2 || Gen2")


def suite():
    s = unittest.TestSuite()
    t = unittest.TestLoader().loadTestsFromTestCase(TestCaseFilmRepo)
    s.addTests(t)
    return s
