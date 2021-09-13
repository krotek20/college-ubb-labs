#include "OfferRepo.h"
#include "Validator.h"
#include <assert.h>

void OfferRepoFile::loadFromFile() {
    ifstream in(fileName);
    if (!in.is_open()) {
        throw OfferException("Eroare la deschiderea fisierului " + fileName);
    }
    while (!in.eof()) {
        string name, dest, type;
        int price;
        in >> name >> dest >> type >> price;
        if (in.eof()) {
            break;
        }
        store(Offer{ name, dest, type, price });
    }
    in.close();
}

void OfferRepoFile::writeToFile() {
    ofstream out(fileName);
    for (auto& o : getAll()) {
        out << o.getName() << ' ' << o.getDest() << ' ' << o.getType() << ' ' << o.getPrice() << '\n';
    }
    out.close();
}

void OfferRepo::store(const Offer& o) {
    if (exist(o.getName())) {
        throw OfferException("Exista deja o oferta cu numele: " + o.getName());
    }
    else {
        all.push_back(o);
    }
}

/*
Cauta oferta dupa nume
returneaza true daca exista si false daca nu exista
*/
bool OfferRepo::exist(const string& name) const {
    vector<Offer> v = this->getAll();
    auto it = find_if(v.begin(), v.end(), [&](const Offer& o) {
        return o.getName() == name;
    });
    if (it == v.end()) {
        return false;
    }
    return true;
}

vector<Offer> OfferRepo::getAll() const noexcept {
	return all;
}

Offer OfferRepo::getOffer(const string& name) const {
    for (const auto& o : all) {
        if (o.getName() == name) {
            return o;
        }
    }
    throw OfferException("Nu exista o oferta cu numele: " + name);
}

/*
Sterge oferta din lista interna
*/
Offer OfferRepo::remove(const string& name) {
    if (!exist(name)) {
        throw OfferException("Nu exista o oferta cu numele: " + name);
    }
    Offer oldOffer;
    all.erase(
        remove_if(all.begin(), all.end(), [&](const Offer& o) {
            if(o.getName() == name)
                oldOffer = o;
            return o.getName() == name;
        }), all.end()
    );
    return oldOffer;
}

/*
Modifica o oferta exista din lista interna
*/
void OfferRepo::modify(const Offer& newOffer) {
    if (!exist(newOffer.getName())) {
        throw OfferException("Nu exista o oferta cu numele: " + newOffer.getName());
    }
    replace_if(all.begin(), all.end(), [&](const Offer& o) {
        return o.getName() == newOffer.getName();
    }, newOffer);
}

// TESTE REPO
void testStore() {
    bool didCatch = false;
    OfferRepo rep;
    rep.store(Offer{ "a","b","c",4 });
    assert(rep.getAll().size() == 1);
    assert(rep.getAll()[0].getName() == "a");

    rep.store(Offer{ "aa","bb","cc",4 });
    assert(rep.getAll().size() == 2);

    //nu pot adauga 2 cu acelasi nume
    try {
        didCatch = false;
        rep.store(Offer{ "a","a","a",4 });
    }
    catch (OfferException&) {
        didCatch = true;
    }
    assert(didCatch);
}

void testExist() {
    OfferRepo rep;
    rep.store(Offer{ "a","b","c",4 });
    rep.store(Offer{ "aa","bb","cc",4 });

    assert(rep.exist("a") == true);
    assert(rep.exist("aaa") == false);
}

void testModify() {
    bool didCatch = false;
    OfferRepo rep;
    rep.store(Offer{ "a","b","c",4 });
    rep.modify(Offer{ "a","bb","cc",4 });
    assert(rep.getOffer("a").getDest() == "bb");
    try {
        rep.modify(Offer{ "b","c","d",1 });
    }
    catch (OfferException& ex) {
        assert(ex.getMsg() == "Nu exista o oferta cu numele: b");
        didCatch = true;
    }
    assert(didCatch);
}

void testRemove() {
    bool didCatch = false;
    OfferRepo rep;
    rep.store(Offer{ "a","b","c",4 });
    rep.store(Offer{ "aa","bb","cc",4 });
    assert(rep.getAll().size() == 2);

    rep.remove("aa");
    assert(rep.getAll().size() == 1);
    try {
        didCatch = false;
        rep.remove("b");
    }
    catch (OfferException&) {
        didCatch = true;
    }
    assert(didCatch);
    assert(rep.getAll().size() == 1);
}

void testFileRepo() {
    bool didCatch = false;
    ofstream out("testOffers.txt", ios::trunc);
    out.close(); //creez un fisier gol
    OfferRepoFile repF{ "testOffers.txt" };
    repF.store(Offer{ "aaa","bbb","ccc",12 });
    try {
        repF.store(Offer{ "aaa","bbb","ccc",12 });
    }
    catch (OfferException&) {
        didCatch = true;
    }
    assert(didCatch);

    OfferRepoFile repF2{ "testOffers.txt" };
    auto p = repF2.exist("aaa");
    assert(p == true);
    auto p2 = repF2.exist("aaa2");
    assert(p2 == false);

    Offer o{ "aaa", "bb", "cc", 1 };
    repF2.modify(o);
    assert(repF2.getOffer("aaa").getDest() == "bb");
    didCatch = false;
    try {
        repF2.modify(Offer{ "a","b","c",2 });
    }
    catch (OfferException&) {
        didCatch = true;
    }
    assert(didCatch);

    repF2.remove("aaa");
    assert(repF2.getAll().size() == 0);
    didCatch = false;
    try {
        repF2.remove("aaa2");
    }
    catch (OfferException&) {
        didCatch = true;
    }
    assert(didCatch);

    OfferRepoFile repF3{ "testOffers.txt" };
    assert(repF3.getAll().size() == 0);

    didCatch = false;
    try {
        repF3.getOffer("a");
    }
    catch (OfferException&) {
        didCatch = true;
    }
    assert(didCatch);

    //fisierul nu exista si nu se poate crea (nu se creaza si directoare)
    //ar trebui sa arunce exceptie
    didCatch = false;
    try {
        OfferRepoFile repF4{ "te/stPets.txt" };
    }
    catch (OfferException&) {
        didCatch = true;
    }
    assert(didCatch);
}

void testeRepo() {
    testStore();
    testExist();
    testModify();
    testRemove();
    testFileRepo();
    cout << ValidateException{ {"testing exception printer", "for repository"} } << "\n";
}