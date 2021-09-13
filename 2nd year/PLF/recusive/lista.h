#ifndef LISTA_H
#define LISTA_H


//tip de data generic (pentru moment este intreg)
typedef int TElem;

//referire a structurii Nod;
struct Nod;

//se defineste tipul PNod ca fiind adresa unui Nod
typedef Nod* PNod;

typedef struct Nod {
	TElem e;
	PNod urm;
};

typedef struct {
	//prim este adresa primului Nod din lista
	PNod _prim;
} Lista;

//operatii pe lista - INTERFATA
// verificare lista vida
bool eListaVida(Lista l);

// substitutie recursiva
bool substituie_rec(PNod head, int i, TElem e, int contor);

// adaugare la inceput
Lista adaugaInceput(Lista l, TElem e);

Lista sublista_rec(PNod nod);

// verific daca e este in lista l
bool eInLista(Lista l, TElem e);

// clonare lista fara primul element
Lista sublista(Lista l);

//crearea unei liste din valori citite pana la 0
Lista creare();
//tiparirea elementelor unei liste
void tipar(Lista l);
// destructorul listei
void distruge(Lista l);

#endif