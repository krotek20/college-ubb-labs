#pragma once
#include <string>
#include <iostream>

class Song {
private:
	int id, rank;
	std::string titlu, artist;
public:
	// constructor
	Song(int id, const std::string& titlu, const std::string& artist, int rank) : id{ id }, titlu{ titlu }, artist{ artist }, rank{ rank } {}
	// constructor de copiere
	Song(const Song& s) : id{ s.id }, titlu{ s.titlu }, artist{ s.artist }, rank{ s.rank } {}

	// getteri
	int getId() const {
		return this->id;
	}
	std::string getTitlu() const {
		return this->titlu;
	}
	std::string getArtist() const {
		return this->artist;
	}
	int getRank() const {
		return this->rank;
	}

	// setteri
	void setTitlu(const std::string& titlu) {
		this->titlu = titlu;
	}
	void setRank(int rank) {
		this->rank = rank;
	}

	// afisare ca string a unei melodii
	std::string toString() const {
		return std::to_string(this->id) + ' ' + this->titlu + ' ' + this->artist + ' ' + std::to_string(this->rank) + '\n';
	}

	bool operator==(const Song& s) const {
		return s.getId() == this->id;
	}
};

// MyException class
class SongException {
private:
	std::string msg;
public:
	SongException(const std::string& msg) : msg{ msg } {}
	std::string getMsg() const {
		return this->msg;
	}
};

// testare functii domain
void testDomain();