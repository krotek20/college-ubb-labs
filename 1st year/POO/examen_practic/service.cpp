#include "service.h"
#include <assert.h>

std::vector<std::pair<Song, int>> srv::getAllSorted() {
	auto v{ r.getAll() };
	std::vector<std::pair<Song, int>> ans;
	int rank[10] = { 0 };
	std::sort(v.begin(), v.end(), [&](const Song& s1, const Song& s2) {
		return s1.getRank() < s2.getRank();
	});
	for (const auto& s : v) {
		rank[s.getRank()]++;
	}
	for (const auto& s : v) {
		ans.push_back({ s,rank[s.getRank()] });
	}
	return ans;
}

void srv::updateSong(int id, std::string titlu, int rank) {
	this->r.update(id, titlu, rank);
}

void srv::stergeSong(int id) {
	this->r.remove(id);
}


void testService() {
	Repo r{ "RepoTest.txt" };
	srv s{ r };
	auto v{ s.getAllSorted() };
	assert(v[0].first.getId() == 1);
	assert(v[0].second == 1);
	assert(v[1].first.getId() == 3);
	assert(v[1].first.getRank() == 2);
	assert(v[1].second == 2);

	// updateSong test
	s.updateSong(4, "titlu10", 8);
	assert(s.getAllSorted()[6].first.getTitlu() == "titlu10");
	assert(s.getAllSorted()[6].first.getRank() == 8);
	s.updateSong(4, "titlu4", 2);

	// stergeSong test
	auto song{ s.getAllSorted()[6] };
	Song so = song.first;
	s.stergeSong(7);
	assert(s.getAllSorted().size() == 6);
	std::ofstream ofs("RepoTest.txt", std::ios_base::app);
	ofs << so.toString();
}