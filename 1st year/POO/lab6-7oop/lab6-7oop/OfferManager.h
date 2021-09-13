#pragma once
#include "undo.h"
#include "Offer.h"
#include "export.h"
#include "OfferRepo.h"
#include "Validator.h"
#include "WishlistManager.h"
//#include "List.h"
#include <vector>
#include <string>
#include <functional>
#include <algorithm>
#include <map>
#include <numeric>
#include <fstream>

using namespace std;

typedef bool(*MaiMicF)(const Offer&, const Offer&);

class EntityCountDTO {
private:
	string name = "";
	string type = "";
	int count = 0;
	friend class OfferManager;
public:
	string getName() const {
		return name;
	}
	string getType() const {
		return type;
	}
	int getCount() const noexcept {
		return count;
	}
};


class OfferManager {
protected:
	RepoAbstract& rep;
	OfferValidator& val;
	vector<unique_ptr<ActionUndo>> undoActions;
	WishlistOffer wl;
	/*
	Functie de sortare generala
	maiMicF - functie care compara 2 Offer, verifica daca are loc relatia mai mic
			- poate fi orice functe (in afara clasei) care respecta signatura (returneaza bool are 2 parametrii Offer)
			- poate fi functie lambda (care nu capteaza nimic in capture list)
	returneaza o lista sortata dupa criteriu dat ca paramatru
	*/
	vector<Offer> generalSort(MaiMicF maiMicF) const;
	/*
	Functie generala de filtrare
	fct - poate fi o functie
	fct - poate fi lambda, am folosit function<> pentru a permite si functii lambda care au ceva in capture list
	returneaza doar ofertele care trec de filtru (fct(offer)==true)
	*/
	vector<Offer> filter(function<bool(const Offer&)> fct) const;

public:
	OfferManager(RepoAbstract& rep, OfferValidator& val) noexcept :rep{ rep }, val{ val } {}
	// nu permitem copierea de obiecte OfferManager
	OfferManager(const OfferManager& ot) = delete;
	// destructor
	~OfferManager();
	/*
	returneaza toate ofertele in ordinea in care au fost adaugate
	*/
	vector<Offer> getAll() const noexcept {
		return rep.getAll();
	}
	/*
	Adauga o noua oferta
	arunca exceptie daca: nu se poate salva, nu e valid
	*/
	void addOffer(const string& name, const string& dest, const string& type, int price);
	/*
	Modifica o oferta existenta
	arunca exceptie daca: nu exista o oferta cu acelasi nume
	*/
	void modOffer(const string& name, const string& dest, const string& type, int price);
	/*
	Sterge o oferta dupa nume
	arunca exceptie daca: nu exista o oferta cu acest nume
	*/
	void removeOffer(const string& name);
	/*
	returneaza doar ofertele cu aceeasi destinatie ca cea data
	*/
	vector<Offer> filterDest(const string& dest) const;
	/*
	returneaza doar ofertele cu pret mai mare decat cel dat
	*/
	vector<Offer> filterPrice(int price) const;
	/*
	Sorteaza dupa nume
	*/
	vector<Offer> sortByName() const;
	/*
	Sorteaza dupa destinatie
	*/
	vector<Offer> sortByDest() const;
	/*
	Sorteaza dupa tip + pret
	*/
	vector<Offer> sortByTypePrice() const;
	/*
	Un raport dupa tipul fiecarui obiect
	Clasa EntityCountDTO stocheaza numele si tipul fiecarei oferte
	In plus, tine un contor pentru fiecare tip de oferta.
	*/
	vector<EntityCountDTO> raportByType() const;
	/*
	Calculeaza totalul preturilor de la toate ofertele
	*/
	int totalPrice();
	/*
	Functia care apeleaza doUndo polimorfic, in functie de ultima operatie efectuata.
	*/
	void undo();

	void addToWL(const string& name);

	void clearWL();

	void randomWL(int cate);

	const vector<Offer>& getAllWL();

	void exportHTML(string fileName) const;
};

void testCtr();