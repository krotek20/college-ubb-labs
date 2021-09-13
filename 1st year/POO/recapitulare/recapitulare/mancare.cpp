#include <string>
#include <memory>
#include <vector>
#include <iostream>
#include <algorithm>
#include <crtdbg.h>

class Mancare {
private:
	int pret;
public:
	Mancare(int pret) : pret{ pret } { };

	virtual std::string descriere() = 0;

	virtual int getPret() const {
		return this->pret;
	}

	virtual ~Mancare() = default;
};

class Burger : public Mancare {
private:
	std::string nume;
public:
	Burger(std::string nume, int pret) : Mancare(pret), nume{ nume } {};

	std::string descriere() override {
		return nume;
	}
};

class CuCartof : public Mancare {
private:
	std::unique_ptr<Mancare> m;
public:
	CuCartof(std::unique_ptr<Mancare> m) : Mancare(m->getPret()) {
		this->m = std::move(m);
	}

	std::string descriere() override {
		return m->descriere() + " cu cartof";
	}

	int getPret() const override {
		return m->getPret() + 3;
	}
};

class CuSos : public Mancare {
private:
	std::unique_ptr<Mancare> m;
public:
	CuSos(std::unique_ptr<Mancare> m) : Mancare(m->getPret()) {
		this->m = std::move(m);
	}

	std::string descriere() override {
		return m->descriere() + " cu sos";
	}

	int getPret() const override {
		return m->getPret() + 2;
	}
};

std::vector <std::unique_ptr <Mancare> > getMancaruri() {
	std::vector <std::unique_ptr <Mancare> > v;
	v.push_back(std::make_unique<Burger>("BigMac", 5));

	v.push_back(std::make_unique<CuSos>(std::make_unique<CuCartof>(std::make_unique<Burger>("BigMac", 5))));

	v.push_back(std::make_unique<CuCartof>(std::make_unique<Burger>("Zinger", 6)));

	v.push_back(std::make_unique<CuSos>(std::make_unique<Burger>("Zinger", 6)));

	return v;
}

int ceva() {
	{
		auto v = getMancaruri();
		std::sort(v.begin(), v.end(), [](std::unique_ptr <Mancare>& m1, std::unique_ptr <Mancare>& m2) {
			return m1->getPret() > m2->getPret();
			});
		for (auto& m : v) {
			std::cout << m->descriere() << "\t" << m->getPret() << '\n';
		}
	}
	_CrtDumpMemoryLeaks();
	return 0;
}
