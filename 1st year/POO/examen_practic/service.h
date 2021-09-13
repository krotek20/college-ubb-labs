#pragma once
#include <vector>
#include <string>
#include "domain.h"
#include "repository.h"
#include <algorithm>

class srv {
private:
	Repo& r;
public:
	srv(Repo& r) : r{ r } {}

	// functie care returneaza un vector de pair
	// acesta contine lista Song-urilor din fisier, sortata dupa rank
	// si un Intreg pentru numarul melodiilor de acelasi rank cu cea curenta
	std::vector<std::pair<Song, int>> getAllSorted();

	// functie care modifica titlul si rank-ul unei melodii dupa ID
	// in: id (Int), titlu (std::string), rank(Int)
	// out: -
	// noexcept
	void updateSong(int id, std::string titlu, int rank);

	// functie care sterge o melodie din lista interna dupa ID
	// in: id (Int)
	// out: -
	// noexcept (In principiu ar trebui exception handling daca nu as putea seta valori concrete din GUI
	//			astfel incat sa nu prind exceptii)
	void stergeSong(int id);

};

void testService();