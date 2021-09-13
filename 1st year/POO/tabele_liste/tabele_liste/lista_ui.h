#pragma once
#include "domain.h"
#include <vector>
#include <QWidget>
#include <QListWidget>

class ListUi : public QWidget {
private:
	std::vector <Student>& stArr;
public:
	ListUi(std::vector <Student>& stArr);

	//QListWidget* list = new QListWidget();

	QListView* list = new QListView();
};

class ListModel : public QAbstractTableModel {
private:
	std::vector <Student>& arr;
public:
	ListModel(std::vector <Student>& arr) : arr{ arr } {};

	int rowCount(const QModelIndex& parent = QModelIndex()) const override;

	int columnCount(const QModelIndex& parent = QModelIndex()) const override;

	QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override;
};