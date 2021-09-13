#include "domain.h"
#include <vector>
#include <fstream>

Produs::Produs(int id, std::string nume, std::string tip, double pret) : id {id}, nume{nume}, tip{tip}, pret{pret}
{

}

int Produs::getId() const
{
	return this->id;
}

std::string Produs::getNume() const
{
	return this->nume;
}

int Produs::getNrVocale() const
{
	std::string voc("aeiou");
	int count = 0;
	for (auto c : this->nume) {
		if (std::find(voc.begin(), voc.end(), c) != voc.end())
			count++;
	}
	return count;
}

std::string Produs::getTip() const
{
	return this->tip;
}

double Produs::getPret() const
{
	return this->pret;
}

bool Produs::operator==(const Produs& p) const
{
	return this->id == p.id;
}

std::istream& operator>>(std::istream& is, Produs& p)
{
	std::string text;
	is >> text;
	if (text == "")
		return is;
	std::vector < std::string > splittedText;
	std::string current = "";
	for (auto c : text) {
		if (c == ';') {
			splittedText.push_back(current);
			current = "";
		}
		else
			current.push_back(c);
	}
	splittedText.push_back(current);
	p.id = std::stoi(splittedText[0]);
	p.nume = splittedText[1];
	p.tip = splittedText[2];
	p.pret = std::stod(splittedText[3]);
	return is;
}

std::ostream& operator<<(std::ostream& os, const Produs& p)
{
	const std::string text = std::to_string(p.id) + ";" + p.nume + ";" + p.tip + ";" + std::to_string(p.pret) + "\n";
	os << text;
	return os;
}
