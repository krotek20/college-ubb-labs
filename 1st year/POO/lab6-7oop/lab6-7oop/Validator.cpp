#include "validator.h"
#include <assert.h>
#include <sstream>

void OfferValidator::validate(const Offer& o) {
	vector<string> msgs;
	if (o.getPrice() < 0) msgs.push_back("Pret negativ!!!");
	if (o.getName().size() == 0) msgs.push_back("Nume vid!!!");
	if (o.getDest().size() == 0) msgs.push_back("Destinatie vid!!!");
	if (o.getType().size() == 0) msgs.push_back("Tip vid!!!");
	if (msgs.size() > 0) {
		throw ValidateException(msgs);
	}
}

ostream& operator<<(ostream& out, const ValidateException& ex) {
	for (const auto& msg : ex.msgs) {
		out << msg << " ";
	}
	return out;
}

void testValidator() {
	OfferValidator v;
	Offer o{ "","","",-1 };
	try {
		v.validate(o);
	}
	catch (const ValidateException & ex) {
		std::stringstream sout;
		sout << ex;
		const auto mesaj = sout.str();
		assert(mesaj.find("negativ") >= 0);
		assert(mesaj.find("vid") >= 0);
	}
}