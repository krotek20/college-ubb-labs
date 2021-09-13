#include "export.h"
#include "Offer.h"
#include "OfferRepo.h"
#include <fstream>
#include <string>
#include <vector>
#include <assert.h>

/*
Scrie in fisierul fileName lista de oferte in format HTML
arunca OfferRepoException daca nu poate crea fisierul
*/
void exportToHTML(const std::string& fileName, const std::vector<Offer>& offers) {
	std::ofstream out(fileName, std::ios::trunc);
	if (!out.is_open()) {
		throw OfferException("Unable to open file:" + fileName);
	}
	for (const auto& o : offers) {
		out << o.getName() << ' ' << o.getDest() << ' ' << o.getType() << ' ' << o.getPrice() << ' ' << std::endl;
	}
	out.close();
}