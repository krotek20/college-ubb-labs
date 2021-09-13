#include "domain.h"
#include <assert.h>

void testDomain() {
	Song s{ 1, "titlu", "artist", 2 };
	assert(s.getId() == 1);
	assert(s.getTitlu() == "titlu");
	assert(s.getArtist() == "artist");
	assert(s.getRank() == 2);
	s.setTitlu("titlu2");
	assert(s.getTitlu() == "titlu2");
	s.setRank(3);
	assert(s.getRank() == 3);
}