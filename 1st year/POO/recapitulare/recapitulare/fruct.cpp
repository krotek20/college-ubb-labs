#include <memory>
#include <vector>
#include <iostream>

class Fruct {
public:
	virtual void tipareste() = 0;
	virtual bool eCuSamburi() const {
		return false;
	}
	virtual ~Fruct() = default;
};

class CuSamburi : public Fruct{
private:
	std::unique_ptr<Fruct> f;
public:
	CuSamburi(std::unique_ptr<Fruct> f) : Fruct() {
		this->f = std::move(f);
	}
	bool eCuSamburi() const override {
		return true;
	}
	void tipareste() override {
		if (this->f->eCuSamburi()) {
			std::cout << " cu samburi";
		}
	}
};

class Pepene : public Fruct {
private:
	float kg;
public:
	Pepene(float kg) : Fruct(), kg{ kg } {}
	virtual void tipareste() override {
		std::cout << kg << " pepene";
	}
};

class PepeneRosu : public Pepene {
public:
	void tipareste() override {
		Pepene::tipareste();
		std::cout << " rosu";
	}
};

class PepeneGalben : public Pepene {
public:
	void tipareste() override {
		Pepene::tipareste();
		std::cout << " galben";
	}
};

class Cos {
private:
	std::vector <std::unique_ptr <Fruct> > fructe;
public:
	void add(std::unique_ptr<Pepene> p) {
		fructe.push_back(std::make_unique<Pepene>(p));
	}
	std::vector<std::unique_ptr<Fruct>> getAll(bool cuSamburi) const {
		std::vector<std::unique_ptr<Fruct>> ret;
		if (cuSamburi) {
			for (auto& f : fructe) {
				if (f->eCuSamburi()) {
					ret.push_back(f);
				}
			}
		}
		else {
			for (auto& f : fructe) {
				if (!f->eCuSamburi()) {
					ret.push_back(f);
				}
			}
		}
	}

	static Cos generateCos() {
		Cos c;
		c.add(std::make_unique<PepeneRosu>(5.0));
		c.add(std::make_unique<PepeneGalben>(std::make_unique<CuSamburi>(6.5)));
		c.add(std::make_unique<PepeneGalben>(4.2));
		c.add(std::make_unique<PepeneRosu>(std::make_unique<CuSamburi>(9.4)));
	
		return c;
	}
};

int main() {
	Cos c = Cos::generateCos();
	auto c1 = c.getAll(true);
	std::cout << "Cu samburi: \n";
	for (auto& c11 : c1) {
		c11->tipareste();
		std::cout << '\n';
	}
	auto c2 = c.getAll(false);
	std::cout << "Fara samburi: \n";
	for (auto& c22 : c2) {
		c22->tipareste();
		std::cout << '\n';
	}
	return 0;
}