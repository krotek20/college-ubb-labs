#include <string>

class Masina {
private:
	std::string culoare;
protected:
	std::string model;
public:
	std::string nume;

	Masina(std::string c, std::string m, std::string n) : culoare{ c }, model{ m }, nume{ n } {};
};

class Limuzina : private Masina {
public:
	Limuzina(std::string c, std::string m, std::string n) : Masina(c, m, n) {};

	void acces() {
		this->model;
		this->nume;
	}
};

class SuperCar : public Limuzina {
public:
	SuperCar(std::string c, std::string m, std::string n) : Limuzina(c, m, n) { };

	void acces() {

	}
};

class Decapotabila : protected Masina {
public:
	Decapotabila(std::string c, std::string m, std::string n) : Masina(c, m, n) {};

	void acces() {
		this->model;
		this->nume;
	}
};

class DouaDecapotabile : public Decapotabila {
public:
	DouaDecapotabile(std::string c, std::string m, std::string n) : Decapotabila(c, m, n) {};

	void acces() {
		this->model;
		this->nume;
	}
};

int main2() {
	Masina m("rosu", "vechi", "Masinuta");
	Limuzina l("neagra", "nou", "Limuzina");
	Decapotabila d("albastru", "misto", "Deca");
	
	m.nume;
	return 0;
}