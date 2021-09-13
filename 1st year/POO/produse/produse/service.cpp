#include "service.h"
#include <algorithm>

Service::Service(Repository& repo) : repo {repo}
{
}

std::vector<Produs> Service::getAll()
{
	auto v = this->repo.getAll();
	std::sort(v.begin(), v.end(), [](const Produs& p1, const Produs p2) {
		return p1.getPret() < p2.getPret();
		});
	return v;
}

void Service::adauga(const Produs& p)
{
	if (p.getNume() == "")
		throw ServiceException("Nume invalid!");
	if (p.getPret() < 1.0 || p.getPret() > 100.0)
		throw ServiceException("Pret invalid!");
	this->repo.adauga(p);
}

ServiceException::ServiceException(std::string mesaj) : mesaj{mesaj}
{
}

std::string ServiceException::getMesaj() const
{
	return this->mesaj;
}
