#pragma once;
#include "IteratorColectie.h"

#define NULL_TELEM 0
typedef int TElem;

class Node {
	friend class Colectie;
	friend class IteratorColectie;
private:
	TElem data = NULL_TELEM;
	int freq = 0;
	int height = 0;
	Node* left = nullptr;
	Node* right = nullptr;
};

typedef bool(*Relatie)(TElem, TElem);

//in implementarea operatiilor se va folosi functia (relatia) rel (de ex, pentru <=)
// va fi declarata in .h si implementata in .cpp ca functie externa colectiei
bool rel(TElem, TElem);

class IteratorColectie;

class Colectie {

	friend class IteratorColectie;

private:
	/* aici e reprezentarea */

	int size = 0;
	Node* nodes = nullptr;

	//adauga recursiv un element pe arborele determinat de p
	Node* adauga_rec(Node* p, TElem e);

	//gaseste minimul din arborele p
	Node* getMin(Node* p);

	//sterge recursiv un element de pe arborele determinat de p
	Node* sterge_rec(Node* p, TElem e, bool& deleted, bool deleteAll);

	int getHeight(Node* p);

	/*simpla rotatie stanga*/
	Node* SRS(Node* p);

	/*dubla rotatie stanga*/
	Node* DRS(Node* p);

	/*simpla rotatie dreapta*/
	Node* SRD(Node* p);

	/*dubla rotatie dreapta*/
	Node* DRD(Node* p);

	/*dealoca nodurile din arborele p*/
	void destroyNodes(Node* p);

public:
	//constructorul implicit
	Colectie();

	//adauga un element in colectie
	void adauga(TElem e);

	//sterge o aparitie a unui element din colectie
	//returneaza adevarat daca s-a putut sterge
	bool sterge(TElem e);

	//verifica daca un element se afla in colectie
	bool cauta(TElem elem) const;

	//returneaza numar de aparitii ale unui element in colectie
	int nrAparitii(TElem elem) const;


	//intoarce numarul de elemente din colectie;
	int dim() const;

	//verifica daca colectia e vida;
	bool vida() const;

	//returneaza un iterator pe colectie
	IteratorColectie iterator() const;

	// destructorul colectiei
	~Colectie();


};
