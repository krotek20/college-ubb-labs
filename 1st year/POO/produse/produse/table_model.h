#pragma once
#include <QAbstractTableModel>
#include <vector>
#include "domain.h"

class TableModel : public QAbstractTableModel {
private:

	std::vector <Produs> productArray;

	int filter = 0;

public:
	void setProductArray(const std::vector <Produs>& productArray, int filter);

	int columnCount(const QModelIndex& parent = QModelIndex()) const;

	int rowCount(const QModelIndex& parent = QModelIndex()) const;

	QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const;

	QVariant headerData(int section, Qt::Orientation orientation, int role) const;
};