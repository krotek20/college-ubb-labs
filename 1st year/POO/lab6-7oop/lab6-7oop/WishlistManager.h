#pragma once
#include "Offer.h"
#include "OfferManager.h"
#include "OfferRepo.h"
#include <string>
#include <random>
#include <chrono>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <fstream>

using std::vector;
using std::string;
using std::find_if;
using std::size_t;
using std::ofstream;

class WishlistOffer {
	vector<Offer> inCos;
public:
	WishlistOffer() = default;

	void add(const Offer& o) {
		inCos.push_back(o);
	}
	void clear() {
		inCos.clear();
	}
	void pop() {
		inCos.pop_back();
	}
	/*
	Umple cosul aleator
	*/
	void generate(size_t cate, vector<Offer> all) {
		std::shuffle(all.begin(), all.end(), std::default_random_engine(std::random_device{}())); //amesteca vectorul v
		while (inCos.size() < cate && all.size() > 0) {
			inCos.push_back(all.back());
			all.pop_back();
		}
	}

	const vector<Offer>& getAllWL() const {
		return inCos;
	}
};