#include <iostream>
#include <vector>

template <typename TElem>
class Expresie {
private:
	TElem val;
	std::vector <TElem> op;
public:
	Expresie(TElem t) : val{ t } { };

	Expresie& operator +(TElem elem) {
		this->op.push_back(this->val);
		this->val += elem;
		return *this;
	}

	Expresie& operator -(TElem elem) {
		this->op.push_back(this->val);
		this->val -= elem;
		return *this;
	}

	TElem valoare() const {
		return val;
	}

	Expresie& undo() {
		if (op.size() == 0)
			return *this;
		this->val = this->op[this->op.size() - 1];
		this->op.pop_back();
		return *this;
	}
};

void operatii() {
	Expresie <int> exp{ 3 };
	exp = exp + 7 + 3;
	exp = exp - 8;
	std::cout << exp.valoare() << '\n';
	exp.undo();
	std::cout << exp.valoare() << '\n';
	exp.undo().undo();
	std::cout << exp.valoare() << '\n';
}

int main6() {
	operatii();
	return 0;
}