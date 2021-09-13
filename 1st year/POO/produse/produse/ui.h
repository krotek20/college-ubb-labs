#pragma once
#include "service.h"
#include <qwidget.h>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QLineEdit>
#include <QPushButton>
#include <QTableView>
#include "table_model.h"
#include <QSlider>
#include "observer.h"
#include <map>

class UI : public QWidget, public Observer {
private:
	Service& service;

	QLineEdit* id = new QLineEdit;
	QLineEdit* nume = new QLineEdit;
	QLineEdit* tip = new QLineEdit;
	QLineEdit* pret = new QLineEdit;

	QTableView* table = new QTableView();
	TableModel* tableModel = new TableModel();

	QVBoxLayout* setProductLayout();

	QVBoxLayout* setTableLayout();

	QPushButton* adauga = new QPushButton("Adauga");

	QSlider* slider = new QSlider();

	std::map<std::string, bool> isOpen;

	void adaugaProdus();

	void update(const std::vector <Produs>& arr);

	friend class UiLabels;

public:
	UI(Service& s);
};