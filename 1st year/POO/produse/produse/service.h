#pragma once
#include "repo.h"

class ServiceException {
private:
	std::string mesaj;
public:
	ServiceException(std::string mesaj);

	std::string getMesaj() const;
};

class Service {
private:
	Repository& repo;
public:
	
	/*constructor de initializare*/
	Service(Repository& repo);

	/*returneaza lista de produse sortata dupa pret
	in: -
	out: un vector de produse sortat*/
	std::vector<Produs> getAll();

	/*adauga un produs in service
	in: p - un produs
	out: -
	throws: daca numele este "" => ServiceException("Nume invalid!")
			daca pretul nu este in intervalul [1.0, 100.0] => ServiceException("Pret invalid!")*/
	void adauga(const Produs& p);
};