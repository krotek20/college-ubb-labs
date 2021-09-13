#pragma once
#include "OfferManager.h"
#include "Offer.h"
#include <vector>
//#include "List.h"

using std::vector;

class ConsoleUI {
	OfferManager& ctr;
	/*
	Tipareste lista tuturor ofertelor in consola
	*/
	void tipareste(const vector<Offer>& offers);
	void tipareste_DTO(const vector<EntityCountDTO>& list);
	/*
	Citeste datele de la tastatura si adauga oferta
	arunca exceptie daca: nu se poate salva, nu e valid
	*/
	void addUI();
	/*
	Citeste datele de la tastatura si cauta daca exista un obiect cu acelasi nume
	Daca da, se face modificarea, altfel se arunca exceptie
	*/
	void modifyUI();
	/*
	Citeste un nume de la tastatura
	Daca exista o oferta cu acel nume, se va sterge din lista interna
	*/
	void removeUI();

public:
	ConsoleUI(OfferManager& ctr) noexcept :ctr{ ctr } {}
	//nu permitem copierea obiectelor
	ConsoleUI(const ConsoleUI& ot) = delete;

	void start();
};