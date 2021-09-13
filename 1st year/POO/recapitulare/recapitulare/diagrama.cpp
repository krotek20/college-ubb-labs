#include <string>
#include <vector>
#include <memory>
#include <iostream>
#include <assert.h>
#include <typeinfo>

class Payable {
private:
	std::string ID;
public:
	Payable(const std::string& id) : ID{ id } { };

	Payable() = default;

	std::string getID() const {
		return this->ID;
	}

	virtual double monthlyIncome() const = 0;

	std::string toString() {
		return this->ID + " " + std::to_string(this->monthlyIncome());
	}

	virtual ~Payable() = default;
};

class Student : public Payable{
private:
	double scholarship;
public:
	Student(const std::string& id, double scholarship) : Payable(id), scholarship{ scholarship } {};

	Student(const Student&) = default;

	double monthlyIncome() const override {
		return this->scholarship;
	}
};

class Teacher : public Payable {
private:
	double salary;
public:
	Teacher(std::string id, double salary) : Payable(id), salary{ salary } {};

	Teacher(const Teacher&) = default;

	double monthlyIncome() const override {
		return this->salary;
	}
};

class DuplicatedIDException {
private:
	std::string msg;
public:
	DuplicatedIDException(const std::string& msg) : msg{ msg } {};

	std::string gteMessage() const {
		return this->msg;
	}
};

class University {
private:
	std::string name;
	std::vector <std::unique_ptr<Payable>> arr;
public:
	University(std::string name) : name{ name } {};
	
	const Payable& findPayableByID(std::string id) const {
		for (const auto& p : this->arr)
			if (p->getID() == id)
				return *p;
	}

	void addPayable(const Payable& p) {
		for (const auto& pays : this->arr)
			if (pays->getID() == p.getID())
				throw DuplicatedIDException("ID duplicat!");
		
		if (typeid(p) == typeid(Student))
			this->arr.push_back(std::make_unique<Student>(p.getID(), p.monthlyIncome()));
		else if (typeid(p) == typeid(Teacher))
			this->arr.push_back(std::make_unique<Teacher>(p.getID(), p.monthlyIncome()));
	}

	const std::vector<std::unique_ptr<Payable>>& getAllPayables() {
		return this->arr;
	}

	double totalAmountToPay() {
		double sum = 0;
		for (const auto& p : this->arr) {
			sum += p->monthlyIncome();
		}
		return sum;
	}
};

int oldMain1() {
	Student s("0", 12);
	Teacher t("1", 123);
	Teacher tErr("0", 12341);
	University u("Ceva");
	u.addPayable(s);
	u.addPayable(t);

	try {
		u.addPayable(t);
		assert(false);
	}
	catch (const DuplicatedIDException& ex) {
		assert(ex.gteMessage() == "ID duplicat!");
	}

	for (const auto& p : u.getAllPayables())
		std::cout << p->toString() << '\n';

	std::cout << u.totalAmountToPay() << '\n';
	return 0;
}