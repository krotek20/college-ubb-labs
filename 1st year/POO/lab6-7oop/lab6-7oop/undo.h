#pragma once
#include "Offer.h"
#include "OfferRepo.h"
#include "WishlistManager.h"

class ActionUndo {
public:
	virtual void doUndo() = 0;
	virtual ~ActionUndo() = default;
};

class UndoAdd : public ActionUndo {
	Offer newOffer;
	RepoAbstract& rep;

public:
	UndoAdd(RepoAbstract& rep, const Offer& o) : rep{ rep }, newOffer{ o } {}

	void doUndo() override {
		rep.remove(newOffer.getName());
	}
};

class UndoRemove : public ActionUndo {
	Offer oldOffer;
	RepoAbstract& rep;

public:
	UndoRemove(RepoAbstract& rep, const Offer& o) : rep{ rep }, oldOffer{ o } {}

	void doUndo() override {
		rep.store(oldOffer);
	}
};

class UndoModify : public ActionUndo {
	Offer oldOffer;
	RepoAbstract& rep;

public:
	UndoModify(RepoAbstract& rep, const Offer& o) : rep{ rep }, oldOffer{ o } {}

	void doUndo() override {
		rep.remove(oldOffer.getName());
		rep.store(oldOffer);
	}
};

class UndoAddToWL : public ActionUndo {
	Offer newOffer;
	WishlistOffer& wl;

public:
	UndoAddToWL(WishlistOffer& wl, const Offer& o) : wl{ wl }, newOffer{ o } {}

	void doUndo() override {
		wl.pop();
	}
};