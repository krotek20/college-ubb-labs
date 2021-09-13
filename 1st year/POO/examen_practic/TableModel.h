#pragma once
#include <vector>
#include <string>
#include <QAbstractTableModel>
#include "domain.h"

class TableModel : public QAbstractTableModel {
private:
	std::vector<std::pair<Song,int>> items;
public:
	TableModel(std::vector<std::pair<Song, int>> items) : items{ items } {}
	void setSongArr(std::vector<std::pair<Song, int>> s) {
		this->items = s;
		this->layoutChanged();
	}
	int rowCount(const QModelIndex& parent) const override {
		return this->items.size();
	}
	int columnCount(const QModelIndex& parent) const override {
		return 5;
	}
	QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override {
		if (role == Qt::DisplayRole) {
			if (index.column() == 0) {
				auto id = this->items[index.row()].first.getId();
				return QString::number(id);
			}
			if (index.column() == 1) {
				auto titlu = this->items[index.row()].first.getTitlu();
				return QString::fromStdString(titlu);
			}
			if (index.column() == 2) {
				auto artist = this->items[index.row()].first.getArtist();
				return QString::fromStdString(artist);
			}
			if (index.column() == 3) {
				auto rank = this->items[index.row()].first.getRank();
				return QString::number(rank);
			}
			if (index.column() == 4) {
				auto filteredRanks = this->items[index.row()].second;
				return QString::number(filteredRanks);
			}
		}
		return QVariant();
	}
};