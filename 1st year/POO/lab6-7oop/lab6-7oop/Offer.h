#pragma once
#include <string>
#include <iostream>

using std::string;
using std::cout;
using std::to_string;

class Offer {
	string name;
	string dest;
	string type;
	int price;

public:
	Offer(const string n, const string d, const string t, const int p):name{ n }, dest{ d }, type{ t }, price{ p }{}

    Offer(const Offer& o) :name{ o.name }, dest{ o.dest }, type{ o.type }, price{ o.price } {
        //cout << "Copy constructor used.\n";
    }

    Offer() = default;

    // getters
    string getName() const {
        return name;
    }
    string getDest() const {
        return dest;
    }
    string getType() const {
        return type;
    }
    int getPrice() const noexcept {
        return price;
    }

    // setters
    void setDest(const string d) {
        this->dest = d;
    }
    void setType(const string t) {
        this->type = t;
    }
    void setPrice(const int p) noexcept {
        this->price = p;
    }

    
    bool operator==(const Offer& ot) const noexcept {
        return this->name == ot.name && this->dest == ot.dest && this->type == ot.type && this->price == ot.price;
    }

    string toString() const {
        return this->name + ' ' + this->dest + ' ' + this->type + ' ' + to_string(this->price) + '\n';
    }
};

class OfferException {
    string msg;
public:
    OfferException(const string& m) :msg{ m } {};
    string getMsg()const { return msg; }
};

void testOffer();