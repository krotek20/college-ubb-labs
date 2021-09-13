#pragma once
#include <string>

class Student {
private:
	std::string nume;
	std::string prenume;
	int id;

public:
	Student(std::string nume, std::string prenume, int id) : nume{ nume }, prenume{ prenume }, id{ id }{};

	std::string getNume() const {
		return this->nume;
	}

	std::string getPrenume() const {
		return this->prenume;
	}

	int getId() const {
		return this->id;
	}

	std::string toString() const {
		return this->nume + " " + this->prenume + " " + std::to_string(this->id);
	}
};