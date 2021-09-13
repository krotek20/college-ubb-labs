"""
@@@ Vintila Radu @@@
"""

import unittest
from tests.domain import client_test, client_validare_test, film_test, film_validare_test, \
                    inchiriere_test, inchiriere_validare_test
from tests.repository import client_repo_test, film_repo_test, inchiriere_repo_test
from tests.service import client_service_test, film_service_test, inchiriere_service_test

all_suites = unittest.TestSuite([client_test.suite(), client_validare_test.suite(), film_test.suite(),
                                 film_validare_test.suite(), inchiriere_test.suite(), inchiriere_validare_test.suite(),
                                 client_repo_test.suite(), film_repo_test.suite(), inchiriere_repo_test.suite(),
                                 client_service_test.suite(), film_service_test.suite(),
                                 inchiriere_service_test.suite()])

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(all_suites)
