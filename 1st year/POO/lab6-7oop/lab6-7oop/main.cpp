#include <crtdbg.h>
#include "OfferManager.h"
#include "WishlistManager.h"
#include "OfferRepo.h"
#include "Validator.h"
#include "Console.h"
#include "Offer.h"

#define _CRTDBG_MAP_ALLOC

void DummyData(OfferManager& ctr) {
    ctr.addOffer("a", "zz", "yy", 10);
    ctr.addOffer("b", "aa", "dd", 40);
    ctr.addOffer("z", "cc", "ll", 25);
    ctr.addOffer("c", "bb", "ll", 30);
}

void testAll() {
    testValidator();
    testOffer();
    testeRepo();
    testCtr();
}

int main() {
    testAll();

    //OfferRepoFile rep{ "offers.txt" };
    OfferRepo rep;
    OfferValidator val;
    OfferManager ctr{ rep,val };

    //adaug cateva oferte
    //DummyData(ctr);
    ConsoleUI ui{ ctr };
    ui.start();
    _CrtDumpMemoryLeaks();
}