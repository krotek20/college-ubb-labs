#include "repository.h"
#include <assert.h>

void Repo::loadFromFile() {
	std::ifstream fin(this->fileName);
	if (!fin.is_open()) {
		throw SongException("File failed to open!");
	}
	while (!fin.eof()) {
		int id, rank;
		std::string titlu, artist;
		fin >> id >> titlu >> artist >> rank;
		if (fin.eof()) {
			break;
		}
		this->items.push_back(Song{ id, titlu, artist, rank });
	}
	fin.close();
}

void Repo::writeToFile() {
	std::ofstream fout(this->fileName);
	for (const auto& s : this->items) {
		fout << s.getId() << ' ' << s.getTitlu() << ' ' << s.getArtist() << ' ' << s.getRank() << '\n';
	}
	fout.close();
}

void Repo::update(int id, std::string titlu, int rank) {
	for (auto& s : this->items) {
		if (s.getId() == id) {
			s.setTitlu(titlu);
			s.setRank(rank);
		}
	}
	this->writeToFile();
}

void Repo::remove(int id) {
	int contor = 0;
	std::string artist;
	for (const auto& s : this->items) {
		if (s.getId() == id) {
			artist = s.getArtist();
			break;
		}
	}
	for (const auto& s : this->items) {
		if (artist == s.getArtist()) {
			++contor;
		}
	}
	if (contor == 1) {
		throw SongException("Acesta este ultima melodie a acestui artist!");
	}
	for (auto it = this->items.begin(); it != this->items.end(); ++it) {
		if (it->getId() == id) {
			this->items.erase(it);
			break;
		}
	}
	this->writeToFile();
}

void testRepo() {
	bool didCatch = false;
	try {
		Repo r{ "ceva.txt" };
	}
	catch (SongException&) {
		didCatch = true;
	}
	assert(didCatch == true);

	Repo r{ "RepoTest.txt" };

	assert(r.getAll().size() == 7);

	// test update
	// 4 titlu4 artist3 2
	r.update(4, "titlu10", 8);
	assert(r.getAll()[3].getTitlu() == "titlu10");
	assert(r.getAll()[3].getRank() == 8);
	r.update(4, "titlu4", 2);

	// test remove
	Song s{ r.getAll()[6] };
	r.remove(7);
	assert(r.getAll().size() == 6);
	std::ofstream ofs("RepoTest.txt", std::ios_base::app);
	ofs << s.toString();
}