#pragma once
#include "domain.h"
#include <vector>
#include <QWidget>
#include <QTableWidget>

class TabelUi : public QWidget{
private:
	std::vector <Student>& stArr;
public:
	TabelUi(std::vector <Student>& stArr);

	//QTableWidget* table = new QTableWidget();

	QTableView* table = new QTableView();
};

class TableModel : public QAbstractTableModel {
private:
	std::vector <Student>& arr;
public:
	TableModel(std::vector <Student>& arr) : arr{ arr } {};

	int rowCount(const QModelIndex& parent = QModelIndex()) const override;

	int columnCount(const QModelIndex& parent = QModelIndex()) const override;

	QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override;
};