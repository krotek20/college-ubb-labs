#include "OfferManager.h"
#include <assert.h>

OfferManager::~OfferManager() {}

/*
Adauga o noua oferta
arunca exceptie daca: nu se poate salva, nu e valid
*/
void OfferManager::addOffer(const string& name, const string& dest, const string& type, int price) {
    Offer o{ name,dest,type,price };
    val.validate(o);
    rep.store(o);
    undoActions.push_back(make_unique<UndoAdd>(rep, o));
}

/*
Modifica o oferta existenta
arunca exceptie daca: nu exista o oferta cu acelasi nume
*/
void OfferManager::modOffer(const string& name, const string& dest, const string& type, int price) {
    val.validate(Offer{ name, dest, type, price });
    Offer o = rep.getOffer(name);
    rep.modify(Offer{ name,dest,type,price });
    undoActions.push_back(make_unique<UndoModify>(rep, o));
}

/*
Sterge o oferta dupa nume
arunca exceptie daca: nu exista o oferta cu acest nume
*/
void OfferManager::removeOffer(const string& name) {
    Offer o = rep.remove(name);
    undoActions.push_back(make_unique<UndoRemove>(rep, o));
}

vector<Offer> OfferManager::filter(function<bool(const Offer&)> fct) const {
    auto all = rep.getAll();
    vector<Offer> filteredAll;
    copy_if(all.begin(), all.end(), back_inserter(filteredAll), fct);
    return filteredAll;
}

vector<Offer> OfferManager::filterDest(const string& dest) const {
    return filter([dest](const Offer& o) {
        return o.getDest() == dest;
    });
}

vector<Offer> OfferManager::filterPrice(int price) const {
    return filter([price](const Offer& o) noexcept {
        return o.getPrice() >= price;
    });
}


vector<Offer> OfferManager::generalSort(MaiMicF maiMicF) const {
    vector<Offer> v = rep.getAll();
    if (v.size() == 0) {
        throw OfferException("\nLista e goala!");
    }
    sort(v.begin(), v.end(), maiMicF);
    return v;
}

/*
Sorteaza dupa nume
*/
vector<Offer> OfferManager::sortByName() const {
    return generalSort([](const Offer& o1, const Offer& o2) {
        return o1.getName() < o2.getName();
    });
}
/*
Sorteaza dupa destinatie
*/
vector<Offer> OfferManager::sortByDest() const {
    return generalSort([](const Offer& o1, const Offer& o2) {
        return o1.getDest() < o2.getDest();
    });
}
/*
Sorteaza dupa tip + pret
*/
vector<Offer> OfferManager::sortByTypePrice() const {
    return generalSort([](const Offer& o1, const Offer& o2) {
        return o1.getType() == o2.getType() ? o1.getPrice() < o2.getPrice() : o1.getType() < o2.getType();
    });
}

vector<EntityCountDTO> OfferManager::raportByType() const {
    map<string, EntityCountDTO> dto;
    auto all = rep.getAll();
    auto it = all.begin();
    while (it != all.end()) {
        auto type = it->getType();
        dto[type].count++;
        dto[type].type = type;
        ++it;
    }
    vector<EntityCountDTO> list;
    it = all.begin();
    while(it != all.end()) {
        EntityCountDTO ecdto;
        auto type = it->getType();
        ecdto.count = dto.at(type).getCount();
        ecdto.name = it->getName();
        ecdto.type = type;
        list.push_back(ecdto);
        ++it;
    }
    return list;
}

int OfferManager::totalPrice() {
    auto all = rep.getAll();
    return std::accumulate(all.begin(), all.end(), 0, [](int nr, const Offer& o) {
        return nr + o.getPrice();
    });
}

void OfferManager::undo() {
    if (undoActions.empty()) {
        throw OfferException("Nu mai exista operatii!");
    }
    undoActions.back()->doUndo();
    undoActions.pop_back();
}

void OfferManager::addToWL(const string& name) {
    const Offer& o = rep.getOffer(name);
    wl.add(o);
    undoActions.push_back(make_unique<UndoAddToWL>(wl, o));
}

void OfferManager::clearWL() {
    wl.clear();
}

void OfferManager::randomWL(int cate) {
    wl.generate(cate, rep.getAll());
}

const vector<Offer>& OfferManager::getAllWL() {
    return wl.getAllWL();
}

void OfferManager::exportHTML(string fileName) const {
    exportToHTML(fileName, wl.getAllWL());
}

// TESTE MANAGER
void testAddCtr() {
    bool didCatch = false;
    OfferRepo rep;
    OfferValidator val;
    OfferManager ctr{ rep,val };
    ctr.addOffer("a", "b", "c", 6);
    assert(ctr.getAll().size() == 1);

    //adaug ceva invalid
    try {
        didCatch = false;
        ctr.addOffer("", "", "", -1);
    }
    catch (ValidateException&) {
        didCatch = true;
    }
    assert(didCatch);
    //incerc sa adaug ceva ce exista deja
    try {
        didCatch = false;
        ctr.addOffer("a", "c", "b", -1);
    }
    catch (ValidateException&) {
        didCatch = true;
    }
    assert(didCatch);
}

void testModCtr() {
    bool didCatch = false;
    OfferRepo rep;
    OfferValidator val;
    OfferManager ctr{ rep,val };

    ctr.addOffer("a", "b", "c", 6);
    ctr.addOffer("aa", "bb", "cc", 66);
    auto v = ctr.getAll();
    Offer o2{ "a", "b", "c", 6 };
    assert(v[0] == o2);

    ctr.modOffer("aa", "bbb", "ccc", 666);
    v = ctr.getAll();
    o2 = { "aa","bbb","ccc",666 };
    assert(v[1] == o2);

    try {
        didCatch = false;
        ctr.modOffer("a", "svsd", "vdsv", -1);
    }
    catch (ValidateException&) {
        didCatch = true;
    }
    assert(didCatch);

    try {
        didCatch = false;
        ctr.modOffer("aaa", "sds", "sds", 66);
    }
    catch (OfferException&) {
        didCatch = true;
    }
    assert(didCatch);
}

void testRemoveCtr() {
    OfferRepo rep;
    OfferValidator val;
    OfferManager ctr{ rep,val };

    ctr.addOffer("a", "b", "c", 6);
    ctr.addOffer("aa", "bb", "cc", 66);
    assert(ctr.getAll().size() == 2);

    ctr.removeOffer("a");
    assert(ctr.getAll().size() == 1);

    ctr.removeOffer("aa");
    assert(ctr.getAll().size() == 0);
}

void testFilterCtr() {
    OfferRepo rep;
    OfferValidator val;
    OfferManager ctr{ rep,val };
    ctr.addOffer("a", "a", "a", 6);
    ctr.addOffer("b", "a", "a", 30);
    ctr.addOffer("c", "a", "a", 60);
    assert(ctr.filterPrice(61).size() == 0);
    assert(ctr.filterPrice(60).size() == 1);
    assert(ctr.filterDest("a").size() == 3);
    assert(ctr.filterDest("z").size() == 0);
}

void testSortCtr() {
    bool didCatch = false;
    OfferRepo rep;
    OfferValidator val;
    OfferManager ctr{ rep,val };
    try {
        didCatch = false;
        auto v = ctr.sortByDest();
    }
    catch (OfferException&) {
        didCatch = true;
    }
    assert(didCatch);
    ctr.addOffer("y", "y", "z", 6);
    ctr.addOffer("z", "z", "d", 6);
    ctr.addOffer("b", "a", "d", 30);
    ctr.addOffer("c", "a", "e", 60);

    auto firstElem = ctr.sortByName()[0];
    assert(firstElem.getName() == "b");

    firstElem = ctr.sortByDest()[0];
    assert(firstElem.getDest() == "a");

    firstElem = ctr.sortByTypePrice()[0];
    assert(firstElem.getName() == "z");
}

void testRaportCtr() {
    OfferRepo rep;
    OfferValidator val;
    OfferManager ctr{ rep,val };
    ctr.addOffer("y", "y", "z", 6);
    ctr.addOffer("z", "z", "d", 6);
    ctr.addOffer("b", "a", "d", 30);
    ctr.addOffer("c", "a", "e", 60);
    auto list = ctr.raportByType();
    assert(list.size() == 4);
    auto it = list.begin();
    ++it;
    assert(it->getCount() == 2);
    assert(it->getName() == "z");
    assert(it->getType() == "d");
}

void testTotalPriceCtr() {
    OfferRepo rep;
    OfferValidator val;
    OfferManager ctr{ rep,val };
    ctr.addOffer("y", "y", "z", 6);
    ctr.addOffer("z", "z", "d", 6);
    ctr.addOffer("b", "a", "d", 30);
    ctr.addOffer("c", "a", "e", 60);
    const int result = ctr.totalPrice();
    assert(result == 102);
}

void testUndo() {
    bool didCatch = false;
    OfferRepo rep;
    OfferValidator val;
    OfferManager ctr{ rep,val };
    ctr.addOffer("y", "y", "z", 6);
    ctr.modOffer("y", "yy", "zz", 66);
    ctr.removeOffer("y");
    assert(ctr.getAll().size() == 0);
    ctr.undo();
    assert(ctr.getAll().size() == 1);
    assert(ctr.getAll()[0].getDest() == "yy");
    ctr.undo();
    assert(ctr.getAll()[0].getDest() == "y");
    ctr.undo();
    assert(ctr.getAll().size() == 0);
    ctr.addOffer("y", "y", "z", 6);
    ctr.addToWL("y");
    ctr.undo();
    assert(ctr.getAllWL().size() == 0);
    ctr.undo();
    try {
        ctr.undo();
    }
    catch (OfferException&) {
        didCatch = true;
    }
    assert(didCatch);
}

void testWishList() {
    bool didCatch = false;
    OfferRepo rep;
    OfferValidator val;
    OfferManager ctr{ rep,val };
    ctr.addOffer("y", "y", "z", 6);
    ctr.addOffer("z", "z", "d", 6);
    ctr.addOffer("b", "a", "d", 30);
    ctr.addOffer("c", "a", "e", 60);
    
    assert(ctr.getAllWL().size() == 0);
    ctr.addToWL("z");
    ctr.addToWL("b");
    assert(ctr.getAllWL().size() == 2);
    ctr.clearWL();
    assert(ctr.getAllWL().size() == 0);
    ctr.randomWL(3);
    assert(ctr.getAllWL().size() == 3);
    ctr.clearWL();
    ctr.addToWL("z");
    ctr.addToWL("b");

    string fileName = "testExport.html";
    try {
        ctr.exportHTML("");
    }
    catch (OfferException&) {
        didCatch = true;
    }
    assert(didCatch);
    ctr.exportHTML(fileName);

    ifstream in(fileName);
    string o;
    getline(in, o);
    assert(o == "z z d 6 ");
    getline(in, o);
    assert(o == "b a d 30 ");
}

void testCtr() {
    testAddCtr();
    testModCtr();
    testRemoveCtr();
    testFilterCtr();
    testSortCtr();
    testRaportCtr();
    testTotalPriceCtr();
    testUndo();
    testWishList();
    cout << ValidateException{ {"testing exception printer", "for service"} } << "\n";
}