#pragma once
#include "domain.h"
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

class Repo {
private:
	std::vector<Song> items;
	std::string fileName;

	// aduce din fisier informatii in lista interna de Song
	void loadFromFile();

	// Adauga informatii in fisier din lista de Song interna
	void writeToFile();

public:
	// constructor clasa Repo
	// se apeleaza automat la creare loadFromFile()
	Repo(std::string fileName) : fileName{ fileName } {
		loadFromFile();
	}

	// functie care returneaza o copie a listei interne
	std::vector<Song> getAll() const {
		return this->items;
	}

	// modifica o melodie dupa ID (UNIC)
	// in: id (Int), titlu (std::string), rank(Int)
	// out: -
	// noexcept
	void update(int id, std::string titlu, int rank);

	// functie care sterge o melodie din lista interna dupa ID (UNIC)
	// in: id (Int)
	// out: -
	// noexcept
	void remove(int id);
};

void testRepo();