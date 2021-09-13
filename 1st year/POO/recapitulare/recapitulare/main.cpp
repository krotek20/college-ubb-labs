#include <vector>
#include <string>
#include <iostream>
#include <assert.h>


using std::vector;

class MyException {
private:
	std::string mesaj;
public:
	MyException(const std::string& mesaj) : mesaj{ mesaj } { };
	const std::string& getMesaj() const {
		return this->mesaj;
	}
};

//vector<int> f(int a) {
//	/*
//	gaseste divizorii lui a
//	in: a - intreg
//	out: rez - un vector de intregi
//	throws: daca a < 0 => MyException("Illegal argument")
//	*/
//	if (a < 0)
//		throw MyException{ "Illegal argument" };
//	vector<int> rez;
//	for (int i = 1; i <= a; i++) {
//		if (a % i == 0) {
//			rez.push_back(i);
//		}
//	}
//	return rez;
//}

//void testF() {
//	try {
//		f(-1);
//		assert(false);
//	}
//	catch (const MyException& ex) {
//		assert(ex.getMesaj() == "Illegal argument");
//		assert(true);
//	}
//	try {
//		f(-2);
//		assert(false);
//	}
//	catch (const MyException&) {
//		assert(true);
//	}
//	assert(f(0).size() == 0);
//	auto v = f(1);
//	assert(v.size() == 1 && v[0] == 1);
//	v = f(15);
//	assert(v.size() == 4 && v[0] == 1 && v[1] == 3 && v[2] == 5 && v[3] == 15);
//}

//class A {
//public:
//	virtual void print() = 0;
//};
//class B : public A {
//public:
//	virtual void print() {
//		std::cout << "printB";
//	}
//};
//class C : public B {
//public:
//	virtual void print() {
//		std::cout << "printC";
//	}
//};


//class A {
//public:
//	A() { std::cout << "A" << std::endl; }
//	~A() { std::cout << "~A" << std::endl; }
//	void print() { std::cout << "print" << std::endl; }
//};
//void f() {
//	A a[2];
//	a[1].print();
//}

vector<int> f2(vector<int> a, vector<int> b) {
	vector<int> rez;
	int poza = 0;
	int pozb = 0;
	while (poza < a.size() && pozb < b.size()) {
		if (a[poza] < b[pozb]) rez.push_back(a[poza++]);
		else rez.push_back(b[pozb++]);
	}
	for (int i = poza; i < a.size(); i++) rez.push_back(a[i]);
	for (int i = pozb; i < b.size(); i++) rez.push_back(b[i]);
	return rez;
}


int main() {
	////testF();
	//std::vector<B> v;
	//B b; C c;
	//v.push_back(b);
	//v.push_back(c);
	//for (auto e : v) {
	//	//e.print();
	//}
	//f();
	vector<int> c = f2({ 2,5,8,10 }, { 2,4,6,7 });
	vector<int> e = f2({ 2,4,6,7 }, { 2,5,8,10 });
	assert(c[0] == 2 && c[1] == 2 && e == c);
	for (auto i : c) {
		std::cout << i << ' ';
	}
	return 0;
}