#include "tests.h"
#include "repo.h"
#include <assert.h>
#include "service.h"
#include <fstream>

void testDomain() {
	assert(Produs(1, "ade23ca", "", 2.3).getNrVocale() == 3);
	assert(Produs(1, "cvbb", "", 23.3).getNrVocale() == 0);
	assert(Produs(1, "aeiou", "", 1).getNrVocale() == 5);
	assert(Produs(1, "adasewa", "", 3).getNrVocale() == 4);
}

void testRepo() {
	Repository r;
	assert(r.getAll().size() == 0);
	r.adauga(Produs(1, "ceva", "tip", 23.4));
	auto v = r.getAll();
	assert(v.size() == 1);
	assert(v[0] == Produs(1, "ceva", "tip", 23.4));

	try {
		r.adauga(Produs(1, "ceva2", "tip3", 23.34));
		assert(false);
	}
	catch (const RepoException& ex) {
		assert(ex.getMesaj() == "Id duplicat!");
	}

	v = { Produs(1, "ceva", "tip", 2), Produs(2, "ceva", "tip", 2), Produs(3, "ceva", "tip", 3) };
	std::ofstream fout("testRepo.txt");
	for (auto it : v)
		fout << it;
	fout.close();
	Repository repo("testRepo.txt");
	assert(v == repo.getAll());
}

void testService() {
	Repository r;
	Service service(r);

	try {
		service.adauga(Produs(1, "", "ceva", 2));
		assert(false);
	}
	catch (const ServiceException& ex) {
		assert(ex.getMesaj() == "Nume invalid!");
	}

	try {
		service.adauga(Produs(1, "ceva", "ceva", 0));
		assert(false);
	}
	catch (const ServiceException& ex) {
		assert(ex.getMesaj() == "Pret invalid!");
	}

	service.adauga(Produs(1, "ceva", "tip", 3));
	service.adauga(Produs(2, "ceva", "tip", 2));
	service.adauga(Produs(3, "ceva", "tip", 1));
	service.adauga(Produs(4, "ceva", "tip", 5));
	service.adauga(Produs(5, "ceva", "tip", 4));

	auto v = service.getAll();
	assert(v.size() == 5);
	assert(v[0] == Produs(3, "ceva", "tip", 1));
	assert(v[1] == Produs(2, "ceva", "tip", 2));
	assert(v[2] == Produs(1, "ceva", "tip", 3));
	assert(v[3] == Produs(5, "ceva", "tip", 4));
	assert(v[4] == Produs(4, "ceva", "tip", 5));

	std::ofstream fout("testService.txt");
	for (auto it : v)
		fout << it;
	fout.close();

	v.clear();
	std::ifstream fin("testService.txt");
	for (int i = 0; i < 5; i++) {
		Produs p(0, "", "", 0);
		fin >> p;
		v.push_back(p);
	}
	fin.close();
	assert(v.size() == 5);
	assert(v[0] == Produs(3, "ceva", "tip", 1));
	assert(v[1] == Produs(2, "ceva", "tip", 2));
	assert(v[2] == Produs(1, "ceva", "tip", 3));
	assert(v[3] == Produs(5, "ceva", "tip", 4));
	assert(v[4] == Produs(4, "ceva", "tip", 5));
}

void testAll()
{
	testDomain();
	testRepo();
	testService();
}
