#include "repo.h"
#include <fstream>

RepoException::RepoException(std::string mesaj) : mesaj{mesaj}
{
}

Repository::Repository(std::string fileName) : fileName{fileName} {
	std::ifstream fin(fileName);
	Produs p(0, "", "", 0);
	while (fin >> p) {
		this->produse.push_back(p);
	}
	fin.close();
}

std::string RepoException::getMesaj() const
{
	return this->mesaj;
}

const std::vector<Produs>& Repository::getAll() const
{
	return this->produse;
}

void Repository::adauga(const Produs& p)
{
	if (std::find(this->produse.begin(), this->produse.end(), p) != this->produse.end())
		throw RepoException("Id duplicat!");
	this->produse.push_back(p);

	if (this->fileName == "")
		return;
	std::ofstream fout(this->fileName);
	for (auto it : this->produse)
		fout << it;
	fout.close();
}
