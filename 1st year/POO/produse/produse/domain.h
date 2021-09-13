#pragma once
#include <string>

class Produs {
private:
	int id;
	std::string nume;
	std::string tip;
	double pret;
public:
	Produs(int id, std::string nume, std::string tip, double pret);

	int getId() const;

	std::string getNume() const;
	
	int getNrVocale() const;

	std::string getTip() const;
	
	double getPret() const;

	bool operator == (const Produs& p) const;

	friend std::istream& operator >> (std::istream& is, Produs& p);

	friend std::ostream& operator << (std::ostream& os, const Produs& p);
};