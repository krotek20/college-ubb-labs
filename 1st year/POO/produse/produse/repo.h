#pragma once
#include "domain.h"
#include <vector>

class RepoException {
private:
	std::string mesaj;
public:
	RepoException(std::string mesaj);

	std::string getMesaj() const;
};

class Repository {
private:
	std::vector <Produs> produse;
	std::string fileName = "";
public:
	/*constructor default*/
	Repository() = default;

	/*constructor de citire din fisier*/
	Repository(std::string fileName);

	/*returneaza toate produsele din repo
	in: -
	out: un vector de produse*/
	const std::vector <Produs>& getAll() const;

	/*adauga un produs in repo
	in: p - un produs
	out: -
	raises: RepoException("Id duplicat") daca exista deja in repo*/
	void adauga(const Produs& p);
};