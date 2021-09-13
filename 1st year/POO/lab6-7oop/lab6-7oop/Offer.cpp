#include "Offer.h"
#include <assert.h>
#include <iostream>

void testOffer() {
	Offer o{ "a", "b", "c", 1 };
	assert(o.toString() == "a b c 1\n");
}