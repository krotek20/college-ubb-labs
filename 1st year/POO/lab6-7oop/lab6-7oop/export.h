#pragma once
#include <string>
#include <vector>
#include <assert.h>
#include "OfferRepo.h"
/*
Scrie in fisierul fileName lista de oferte in format HTML
arunca OfferRepoException daca nu poate crea fisierul
*/
void exportToHTML(const std::string& fileName, const std::vector<Offer>& offers);