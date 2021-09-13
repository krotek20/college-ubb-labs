#include "IteratorColectie.h"
#include "Colectie.h"

/*complexitate favorabil, defavorabil, mediu si total: Teta(numar_elemente_distincte)*/
IteratorColectie::IteratorColectie(const Colectie& c) : col(c) { //parcurgere in inordine
	this->elements = new TElem[this->col.size];
	this->elementFreq = new int[this->col.size];
	this->currentElement = 0;
	this->currentFreq = 0;
	this->size = 0;

	Node** st = new Node*[this->col.size];
	int cont = 0;
	
	Node* p = col.nodes;
	while (cont > 0 || p != nullptr) {
		while (p != nullptr) {
			st[cont++] = p;
			p = p->left;
		}
		p = st[cont - 1];
		cont--;
		this->elements[this->size] = p->data;
		this->elementFreq[this->size++] = p->freq;
		p = p->right;
	}

	delete[] st;
}

/*complexitate favorabil, defavorabil, mediu si total: Teta(1)*/
TElem IteratorColectie::element() const {
	return this->elements[this->currentElement];
}

/*complexitate favorabil, defavorabil, mediu si total: Teta(1)*/
IteratorColectie::~IteratorColectie()
{
	delete[] elements;
	delete[] elementFreq;
}

/*complexitate favorabil, defavorabil, mediu si total: Teta(1)*/
bool IteratorColectie::valid() const {
	return this->currentElement < this->size;
}

/*complexitate favorabil, defavorabil, mediu si total: Teta(1)*/
void IteratorColectie::urmator() {
	this->currentFreq++;
	if (this->currentFreq >= this->elementFreq[this->currentElement]) {
		this->currentFreq = 0;
		this->currentElement++;
	}
}

/*complexitate favorabil, defavorabil, mediu si total: Teta(1)*/
void IteratorColectie::prim() {
	this->currentElement = 0;
}