#include "table_model.h"
#include <QBrush>

void TableModel::setProductArray(const std::vector<Produs>& productArray, int filter)
{
	this->productArray = productArray;
	this->filter = filter;
	//emit dataChanged(createIndex(0, 0), createIndex(this->rowCount(), this->columnCount()));
	emit layoutChanged();
}

int TableModel::columnCount(const QModelIndex& parent) const
{
	return 5;
}

int TableModel::rowCount(const QModelIndex& parent) const
{
	return productArray.size();
}

QVariant TableModel::data(const QModelIndex& index, int role) const
{
	if (role == Qt::DisplayRole) {
		switch (index.column()) {
		case 0:
			return QString::number(productArray[index.row()].getId());
		case 1:
			return QString::fromStdString(productArray[index.row()].getNume());
		case 2:
			return QString::fromStdString(productArray[index.row()].getTip());
		case 3:
			return QString::number(productArray[index.row()].getPret());
		case 4:
			return QString::number(productArray[index.row()].getNrVocale());
		}
	}
	if (role == Qt::BackgroundRole) {
		if (productArray[index.row()].getPret() <= this->filter)
			return QBrush(Qt::red);
	}
	return QVariant();
}

QVariant TableModel::headerData(int section, Qt::Orientation orientation, int role) const
{
	if (role == Qt::DisplayRole) {
		if (orientation == Qt::Horizontal)
			switch(section){
			case 0:
				return "ID";
			case 1:
				return "Nume";
			case 2:
				return "Tip";
			case 3:
				return "Pret";
			case 4:
				return "Numar vocale";
			}
	}
	return QVariant();
}
