#include "lista.h"
#include <iostream>

using namespace std;

bool substitutie(Lista l, int i, TElem e) {
	return substituie_rec(l._prim, i, e, 1);
}

void make_substitution(Lista l) {
	int i, e;
	cout << "\na. Substitutie\n";
	cout << "i = "; cin >> i;
	cout << "e (elementul pentru substitutie) = "; cin >> e;
	if (substitutie(l, i, e)) {
		tipar(l);
	}
	else {
		// throw exception("Elementul nu a fost gasit in lista");
		cout << "Elementul nu a fost gasit in lista!\n";
	}
}

// diferenta_elem(l2, e):
//			true, eInLista(l2, e)
//			false, altfel
bool diferenta_elem(Lista l2, TElem e) {
	if (eInLista(l2, e)) return true;
	return false;
}

// diferenta(head_l1, l2, rez):
//			rez, head_l1 == NULL
//			diferenta(head_l1->urm, l2, rez), altfel
Lista diferenta(PNod head_l1, Lista l2, Lista rez) {
	if (head_l1 == NULL) return rez;
	if (!diferenta_elem(l2, head_l1->e)) {
		rez = adaugaInceput(rez, head_l1->e);
	}
	diferenta(head_l1->urm, l2, rez);
}

void make_diferenta() {
	cout << "\nb. Diferenta a doua multimi\n";
	cout << "\nPrima lista:\n";
	Lista l1;
	l1 = creare();
	tipar(l1);

	cout << "\nA doua lista:\n";
	Lista l2;
	l2 = creare();
	tipar(l2);

	cout << "\nLista rezultat:\n";
	Lista rez;
	PNod nod = new Nod();
	nod = NULL;
	rez._prim = nod;
	rez = diferenta(l1._prim, l2, rez);
	tipar(rez);

	distruge(l1);
	distruge(l2);
	distruge(rez);
}

int main()
{
	Lista l;
	l = creare();
	tipar(l);

	// Substitutie
	make_substitution(l);

	// Diferenta multimi
	make_diferenta();

	distruge(l);
}