#include <iostream>
#include <string>
#include <fstream>
#include <vector>

class Student {
private:
	std::string nume;
	int id;
	std::string uni;
public:
	Student(std::string nume, int id, std::string uni) : nume{ nume }, id{ id }, uni{ uni } { };

	Student() = default;

	friend std::istream& operator >> (std::istream& in, Student& s) {
		in >> s.nume >> s.id >> s.uni;
		return in;
	}

	friend std::ostream& operator << (std::ostream& out, const Student& s) {
		out << "Nume: " << s.nume << "\tId: " << s.id << "\tUniversitate: " << s.uni << '\n';
		return out;
	}
};

class Array{
private:
	std::vector<Student> arr;
public:
	void push_back(Student s) {
		arr.push_back(s);
	}

	class iterator {
	private:
		const Array& arr;
		int poz = 0;
	public:
		iterator(const Array& arr, int poz) : arr{ arr }, poz{ poz } {};

		bool operator != (const iterator& it) {
			return this->poz != it.poz;
		}

		Student operator * () {
			return this->arr.arr[this->poz];
		}

		void operator ++ () {
			this->poz++;
		}
	};

	iterator begin() {
		return iterator(*this, 0);
	}

	iterator end() {
		return iterator(*this, this->arr.size());
	}
};

int main1() {
	Student s("Adi", 2822, "UBB");
	Student n;
	std::ofstream fout("out.txt");
	fout << "Alin 2826 UBB\n";
	fout.close();

	std::ifstream fin("out.txt");
	fin >> n;
	fin.close();
	//std::cin >> n;

	Array arr;
	arr.push_back(s);
	arr.push_back(n);

	for (auto st : arr) {
		std::cout << st << '\n';
	}
	return 0;
}