#include <map>
#include <string>
#include <iostream>
#include <vector>

template <typename TElem>
class Carnet {
private:
	std::map < std::string, TElem > note;
	std::vector <std::string> lastAdded;
public:
	Carnet& add(std::string s, TElem nota) {
		this->note[s] = nota;
		this->lastAdded.push_back(s);
		return *this;
	}

	Carnet& removeLast() {
		if (this->lastAdded.size() == 0)
			return *this;
		this->note.erase(this->lastAdded[this->lastAdded.size() - 1]);
		this->lastAdded.pop_back();
		return *this;
	}

	TElem operator [] (std::string s) {
		if (this->note.find(s) == this->note.end())
			throw std::exception();
		return this->note[s];
	}
};

void anscolar() {
	Carnet <int> cat;
	cat.add("SDA", 9);
	cat.add("OOP", 7).add("FP", 9);
	std::cout << cat["OOP"] << '\n';
	cat.removeLast().removeLast();
	try {
		std::cout << cat["OOP"] << '\n';
	}
	catch (std::exception& ex) {
		std::cout << "Nu exista nota pentru OOP";
	}
}



int main65() {
	anscolar();
	return 0;
}