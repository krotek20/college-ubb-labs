#include "Colectie.h"
#include "IteratorColectie.h"
#include <iostream>
#define max(a, b) a > b ? a : b
using namespace std;


bool rel(TElem e1, TElem e2) {
	return e1 <= e2;
}

/*complexitate favorabil, defavorabil, mediu si total: Teta(1)*/
Colectie::Colectie() {
	
}

/*complexitate: O(log2(numar_elemente_distincte))
complexitate favorabil: Teta(1), cand elementul este in radacina arborelui
complexitate defavorabil: Teta(this->nodes->height) = Teta(log2(numar_elemente_distincte)), cand elementul nu se afla deja in arbore
complexitate medie: Teta(log2(numar_elemente_distincte))*/
Node* Colectie::adauga_rec(Node* p, TElem e)
{
	if (p == nullptr) {
		p = new Node;
		p->data = e;
		p->freq = 1;
		p->height = 0;
		p->left = p->right = nullptr;
		return p;
	}
	if (e == p->data) {
		p->freq++;
		return p;
	}
	if (!rel(e, p->data)) { //pe dreapta
		p->right = adauga_rec(p->right, e);
		if (getHeight(p->right) - getHeight(p->left) == 2) {
			if (!rel(e, p->right->data))
				p = SRS(p);
			else
				p = DRS(p);
		}
		else
			p->height = max(getHeight(p->left), getHeight(p->right)) + 1;
		return p;
	}
	if (rel(e, p->data)) { //pe stanga
		p->left = adauga_rec(p->left, e);
		if (getHeight(p->left) - getHeight(p->right) == 2) {
			if (rel(e, p->left->data))
				p = SRD(p);
			else
				p = DRD(p);
		}
		else
			p->height = max(getHeight(p->left), getHeight(p->right)) + 1;
		return p;
	}

}

/*complexitate favorabil, defavorabil, mediu si total: Teta(p->height) = Teta(log2(numar_elemente_din_p))*/
Node* Colectie::getMin(Node* p)
{
	if (p == nullptr)
		return nullptr;
	if (p->left == nullptr)
		return p;
	return getMin(p->left);
}

/*complexitate: O(log2(numar_elemente_distincte))
complexitate favorabil: Teta(1), cand elementul este in radacina arborelui si nu are frecventa mai mare decat 1
complexitate defavorabil: Teta(this->nodes->height) = Teta(log2(numar_elemente_distincte)), cand elementul nu se afla deja in arbore
complexitate medie: Teta(log2(numar_elemente_distincte))*/
Node* Colectie::sterge_rec(Node* p, TElem e, bool& deleted, bool deleteAll)
{
	if (p == nullptr)
		return nullptr;
	if (rel(e, p->data) && e != p->data)
		p->left = sterge_rec(p->left, e, deleted, deleteAll);
	else if (!rel(e, p->data))
		p->right = sterge_rec(p->right, e, deleted, deleteAll);
	else if (p->left != nullptr && p->right != nullptr) { //element found
		if (!deleteAll) {
			deleted = true;
			p->freq--;
			if (p->freq > 0)
				return p;
			deleteAll = true;
		}
		if (deleteAll) {
			Node* temp = getMin(p->right);
			p->data = temp->data;
			bool newDeleted = false;
			p->right = sterge_rec(p->right, p->data, newDeleted, true);
		}
	}
	else {
		if (!deleteAll) {
			deleted = true;
			p->freq--;
			if (p->freq > 0)
				return p;
			deleteAll = true;
		}
		if (deleteAll) {
			Node* temp = p;
			if (p->left == nullptr)
				p = p->right;
			else if (p->right == nullptr)
				p = p->left;
			delete temp;
		}
	}

	if (p == nullptr)
		return nullptr;
	p->height = max(getHeight(p->left), getHeight(p->right)) + 1;

	if (getHeight(p->right) - getHeight(p->left) == 2) {
		if (getHeight(p->right->left) - getHeight(p->right->right) == 1)
			p = DRS(p);
		else
			p = SRS(p);
		return p;
	}
	if (getHeight(p->left) - getHeight(p->right) == 2) {
		if (getHeight(p->left->right) - getHeight(p->left->left) == 1)
			p = DRD(p);
		else 
			p = SRD(p);
		return p;
	}
	return p;
}

/*complexitate favorabil, defavorabil, mediu si total: Teta(1)*/
int Colectie::getHeight(Node* p)
{
	return p == nullptr ? -1 : p->height;
}

/*complexitate favorabil, defavorabil, mediu si total: Teta(1)*/
Node* Colectie::SRS(Node* p)
{
	Node* pRight = p->right;
	p->right = pRight->left;
	pRight->left = p;
	p->height = p == nullptr ? -1 : max(getHeight(p->left), getHeight(p->right)) + 1;
	pRight->height = pRight == nullptr ? -1 : max(getHeight(pRight->left), getHeight(pRight->right)) + 1;
	return pRight;
}

/*complexitate favorabil, defavorabil, mediu si total: Teta(1)*/
Node* Colectie::DRS(Node* p)
{
	Node* pRight = p->right;
	Node* newP = pRight->left;
	p->right = newP->left;
	pRight->left = newP->right;
	newP->left = p;
	newP->right = pRight;
	p->height = p == nullptr ? -1 : max(getHeight(p->left), getHeight(p->right)) + 1;
	pRight->height = pRight == nullptr ? -1 : max(getHeight(pRight->left), getHeight(pRight->right)) + 1;
	newP->height = newP == nullptr ? -1 : max(getHeight(newP->left), getHeight(newP->right)) + 1;
	return newP;
}

/*complexitate favorabil, defavorabil, mediu si total: Teta(1)*/
Node* Colectie::SRD(Node* p)
{
	Node* pLeft = p->left;
	p->left = pLeft->right;
	pLeft->right = p;
	p->height = p == nullptr ? -1 : max(getHeight(p->left), getHeight(p->right)) + 1;
	pLeft->height = pLeft == nullptr ? -1 : max(getHeight(pLeft->left), getHeight(pLeft->right)) + 1;
	return pLeft;
}

/*complexitate favorabil, defavorabil, mediu si total: Teta(1)*/
Node* Colectie::DRD(Node* p)
{
	Node* pLeft = p->left;
	Node* newP = pLeft->right;
	p->left = newP->right;
	pLeft->right = newP->left;
	newP->right = p;
	newP->left = pLeft;
	p->height = p == nullptr ? -1 : max(getHeight(p->left), getHeight(p->right)) + 1;
	pLeft->height = pLeft == nullptr ? -1 : max(getHeight(pLeft->left), getHeight(pLeft->right)) + 1;
	newP->height = newP == nullptr ? -1 : max(getHeight(newP->left), getHeight(newP->right)) + 1;
	return newP;
}

/*complexitate favorabil, defavorabil, mediu si total: Teta(numar_elemente_distincte)*/
void Colectie::destroyNodes(Node* p)
{
	if (p == nullptr)
		return;
	if (p->left != nullptr)
		destroyNodes(p->left);
	if (p->right != nullptr)
		destroyNodes(p->right);
	delete p;
}

/*complexitate: O(log2(numar_elemente_distincte))
complexitate favorabil: Teta(1), cand elementul este in radacina arborelui
complexitate defavorabil: Teta(this->nodes->height) = Teta(log2(numar_elemente_distincte)), cand elementul nu se afla deja in arbore
complexitate medie: Teta(log2(numar_elemente_distincte))*/
void Colectie::adauga(TElem e) {
	this->size++;
	this->nodes = this->adauga_rec(this->nodes, e);
}

/*complexitate: O(log2(numar_elemente_distincte))
complexitate favorabil: Teta(1), cand elementul este in radacina arborelui si nu are frecventa mai mare decat 1
complexitate defavorabil: Teta(this->nodes->height) = Teta(log2(numar_elemente_distincte)), cand elementul nu se afla in arbore
complexitate medie: Teta(log2(numar_elemente_distincte))*/
bool Colectie::sterge(TElem e) {
	bool deleted = false;
	this->nodes = sterge_rec(this->nodes, e, deleted, false);
	if (deleted)
		this->size--;
	return deleted;
}

/*complexitate: O(log2(numar_elemente_distincte))
complexitate favorabil: Teta(1), cand elementul cautat se afla in radacina arborelui
complexitate defavorabil: Teta(this->nodes->height) = Teta(log2(numar_elemente_distincte)), cand elementul nu se afla in arbore
complexitate medie: Teta(log2(numar_elemente_distincte))*/
bool Colectie::cauta(TElem elem) const {
	Node* node = this->nodes;
	while (node != nullptr) {
		if (node->data == elem)
			if (node->freq > 0)
				return true;
			else 
				return false;
		node = rel(elem, node->data) ? node->left : node->right;
	}
	return false;
}

/*complexitate: O(log2(numar_elemente_distincte))
complexitate favorabil: Teta(1), cand elementul cautat se afla in radacina arborelui
complexitate defavorabil: Teta(this->nodes->height) = Teta(log2(numar_elemente_distincte)), cand elementul nu se afla in arbore
complexitate medie: Teta(log2(numar_elemente_distincte))*/
int Colectie::nrAparitii(TElem elem) const {
	Node* node = this->nodes;
	while (node != nullptr) {
		if (node->data == elem)
			return node->freq;
		node = rel(elem, node->data) ? node->left : node->right;
	}
	return 0;
}


/*complexitate favorabil, defavorabil, mediu si total: Teta(1)*/
int Colectie::dim() const {
	return this->size;
}

/*complexitate favorabil, defavorabil, mediu si total: Teta(1)*/
bool Colectie::vida() const {
	return this->nodes == nullptr;
}


IteratorColectie Colectie::iterator() const {
	return  IteratorColectie(*this);
}

/*complexitate favorabil, defavorabil, mediu si total: Teta(numar_elemente_distincte)*/
Colectie::~Colectie() {
	destroyNodes(this->nodes);
}