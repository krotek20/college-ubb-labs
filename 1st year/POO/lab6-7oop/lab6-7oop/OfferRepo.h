#pragma once
#include "Offer.h"
//#include "List.h"
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <exception>
#include <cstdlib>
#include <time.h>

using namespace std;

class RepoAbstract {
public:
     virtual void store(const Offer& o) = 0;
     virtual bool exist(const string& name) const = 0;
     virtual vector<Offer> getAll() const = 0;
     virtual Offer getOffer(const string& name) const = 0;
     virtual Offer remove(const string& name) = 0;
     virtual void modify(const Offer& newOffer) = 0;
     virtual ~RepoAbstract() = default;
};

class OfferRepo : public RepoAbstract {
    vector <Offer> all;

public:
    OfferRepo() : RepoAbstract() {}
    //nu permitem copierea de obiecte
    OfferRepo(const OfferRepo& ot) = delete;
    /*
    Salvare oferta
    arunca exceptie daca mai exista o oferta cu acelasi nume
    */
    void store(const Offer& o) override;
    /*
    Cauta oferta dupa nume
    returneaza true daca exista si false daca nu exista
    */
    bool exist(const string& name) const override;
    /*
    returneaza toate ofertele salvate
    */
    vector<Offer> getAll() const noexcept override;
    /*
    returneaza o oferta dupa nume
    */
    Offer getOffer(const string& name) const override;
    /*
    Sterge oferta din lista interna
    */
    Offer remove(const string& name) override;
    /*
    Modifica o oferta exista din lista interna
    */
    void modify(const Offer& newOffer) override;
};

class RepoLab : public RepoAbstract {
    vector <Offer> all;
    int prob;

public:
    RepoLab(int p) : RepoAbstract(), prob{ p } {
        srand(unsigned(time(NULL))); 
    }
    //nu permitem copierea de obiecte
    RepoLab(const RepoLab& ot) = delete;
    /*
    Salvare oferta
    arunca exceptie daca mai exista o oferta cu acelasi nume
    */
    void store(const Offer& o) override {
        const int p = rand() % 100;
        if (p > prob) {
            throw OfferException("Crapa");
        }
        else {
            if (exist(o.getName())) {
                throw OfferException("Exista deja o oferta cu numele: " + o.getName());
            }
            else {
                all.push_back(o);
            }
        }
    }
    /*
    Cauta oferta dupa nume
    returneaza true daca exista si false daca nu exista
    */
    bool exist(const string& name) const override {
        const int p = rand() % 100;
        cout << p << ' ' << prob << endl;
        if (p > prob) {
            throw OfferException("Crapa");
        }
        else {
            vector<Offer> v = this->getAll();
            auto it = find_if(v.begin(), v.end(), [&](const Offer& o) {
                return o.getName() == name;
            });
            if (it == v.end()) {
                return false;
            }
            return true;
        }
    }
    /*
    returneaza toate ofertele salvate
    */
    vector<Offer> getAll() const override {
        const int p = rand() % 100;
        if (p > prob) {
            throw OfferException("Crapa");
        }
        else {
            return all;
        }
    }
    /*
    returneaza o oferta dupa nume
    */
    Offer getOffer(const string& name) const override {
        const int p = rand() % 100;
        if (p > prob) {
            throw OfferException("Crapa");
        }
        else {
            for (const auto& o : all) {
                if (o.getName() == name) {
                    return o;
                }
            }
            throw OfferException("Nu exista o oferta cu numele: " + name);
        }
    }
    /*
    Sterge oferta din lista interna
    */
    Offer remove(const string& name) override {
        const int p = rand() % 100;
        if (p > prob) {
            throw OfferException("Crapa");
        }
        else {
            if (!exist(name)) {
                throw OfferException("Nu exista o oferta cu numele: " + name);
            }
            Offer oldOffer;
            all.erase(
                remove_if(all.begin(), all.end(), [&](const Offer& o) {
                if (o.getName() == name)
                    oldOffer = o;
                return o.getName() == name;
            }), all.end()
                );
            return oldOffer;
        }
    }
    /*
    Modifica o oferta exista din lista interna
    */
    void modify(const Offer& newOffer) override {
        const int p = rand() % 100;
        if (p > prob) {
            throw OfferException("Crapa");
        }
        else {
            if (!exist(newOffer.getName())) {
                throw OfferException("Nu exista o oferta cu numele: " + newOffer.getName());
            }
            replace_if(all.begin(), all.end(), [&](const Offer& o) {
                return o.getName() == newOffer.getName();
            }, newOffer);
        }
    }
};

class OfferRepoFile : public RepoAbstract {
private:
    vector <Offer> all;
    string fileName;
    void loadFromFile();
    void writeToFile();

public:
    OfferRepoFile(string fileName) : RepoAbstract(), fileName{ fileName } {
        loadFromFile(); //incarcam datele din fisier
    }
    void store(const Offer& o) override {
        if (exist(o.getName())) {
            throw OfferException("Exista deja o oferta cu numele: " + o.getName());
        }
        else {
            all.push_back(o);
        }
        writeToFile();
    }
    Offer remove(const string& name) override {
        if (!exist(name)) {
            throw OfferException("Nu exista o oferta cu numele: " + name);
        }
        Offer oldOffer;
        all.erase(
            remove_if(all.begin(), all.end(), [&](const Offer& o) {
            if (o.getName() == name)
                oldOffer = o;
            return o.getName() == name;
        }), all.end()
            );
        writeToFile();
        return oldOffer;
    }
    void modify(const Offer& newOffer) override {
        if (!exist(newOffer.getName())) {
            throw OfferException("Nu exista o oferta cu numele: " + newOffer.getName());
        }
        replace_if(all.begin(), all.end(), [&](const Offer& o) {
            return o.getName() == newOffer.getName();
        }, newOffer);
        writeToFile();
    }
    bool exist(const string& name) const override {
        vector<Offer> v = this->getAll();
        auto it = find_if(v.begin(), v.end(), [&](const Offer& o) {
            return o.getName() == name;
        });
        if (it == v.end()) {
            return false;
        }
        return true;
    }
    vector<Offer> getAll() const noexcept override {
        return all;
    }
    Offer getOffer(const string& name) const override {
        for (const auto& o : all) {
            if (o.getName() == name) {
                return o;
            }
        }
        throw OfferException("Nu exista o oferta cu numele: " + name);
    }
};

void testeRepo();