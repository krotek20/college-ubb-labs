#include "lista.h"
#include <iostream>

using namespace std;


PNod creare_rec() {
    TElem x;
    cout << "x=";
    cin >> x;
    if (x == 0)
        return NULL;
    else {
        PNod p = new Nod();
        p->e = x;
        p->urm = creare_rec();
        return p;
    }
}

Lista creare() {
    Lista l;
    l._prim = creare_rec();
    return l;
}

// verificare lista vida
bool eListaVida(PNod head) {
    return head == NULL;
}

// substituie_rec(head, i, e, contor):
//          true, contor == i
//          false, altfel
bool substituie_rec(PNod head, int i, TElem e, int contor) {
    if (eListaVida(head)) return false;
    if (contor == i) {
        head->e = e;
        return true;
    }
    substituie_rec(head->urm, i, e, contor + 1);
}

// adaugarea elementului e la inceputul listei l
Lista adaugaInceput(Lista l, TElem e) {
    PNod nod = new Nod();
    nod->e = e;
    nod->urm = l._prim;
    l._prim = nod;
    return l;
}

// sublista_rec(nod) 
//          Lista vida, daca nod == NULL
//          adaugaInceput(sublista_rec(nod->urm), nod->e), altfel
Lista sublista_rec(PNod nod) {
    if (nod == NULL) return Lista();
    return adaugaInceput(sublista_rec(nod->urm), nod->e);
}


Lista sublista(Lista l) {
    return sublista_rec(l._prim->urm);
}

// eInLista(l, e):
//          false, eListaVida(l._prim)
//          true, altfel
bool eInLista(Lista l, TElem e) {
    if (eListaVida(l._prim)) return false;
    if (l._prim->e == e) return true;
    return eInLista(sublista(l), e);
}

void tipar_rec(PNod p) {
    if (p != NULL) {
        cout << p->e << " ";
        tipar_rec(p->urm);
    }
}

void tipar(Lista l) {
    tipar_rec(l._prim);
}

void distruge_rec(PNod p) {
    if (p != NULL) {
        distruge_rec(p->urm);
        delete p;
    }
}

void distruge(Lista l) {
    //se elibereaza memoria alocata nodurilor listei
    distruge_rec(l._prim);
}
