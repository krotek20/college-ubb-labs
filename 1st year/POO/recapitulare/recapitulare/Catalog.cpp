#include <iostream>
#include <vector>
#include <map>
#include <string>

class Group : public Catalog {
private:
	int gid;
	std::map<int, std::vector<std::string>> elevi;
public:
	Group(int gid) {
		this->gid = gid;
		elevi[gid].assign({});
	}
	Group& operator +(std::string elev) {
		this->elevi[gid].push_back(elev);
		return *this;
	}
	std::vector<std::string> select(char selected) {
		std::vector<std::string> rez;
		for (auto e : elevi[gid]) {
			if (e[0] == selected) {
				rez.push_back(e);
			}
		}
		return rez;
	}
};

class Catalog : public Group {
private:
	int gid;
	Group group;
public:
	Catalog() : group(gid) {}
};


int main() {
	Catalog an1;
	//add ion and aron to 211
	an1.group(211) + "Ion" + "aron";
	//add ana and aurora to 212
	an1.group(212) + "ana" + "aurora";
	//print all students from group 211
	for (auto name : an1.group(211)) {
		std::cout << name << ",";
	}
	//find and print all names from 211 that start with 'a'
	vector<string> v = an1.group(212).select('a');
	for (auto name : v) {
		std::cout << name << ",";
	}
}