#include "ui.h"
#include <QFormLayout>
#include <QMessageBox>
#include <QHeaderView>
#include <QAbstractItemModel>
#include "labels.h"

QVBoxLayout* UI::setProductLayout()
{
	QVBoxLayout* layout = new QVBoxLayout;

	QFormLayout* flayout = new QFormLayout;

	flayout->addRow("Id: ", id);
	flayout->addRow("Nume: ", nume);
	flayout->addRow("Tip: ", tip);
	flayout->addRow("Pret: ", pret);

	layout->addLayout(flayout);
	layout->addWidget(this->adauga);

	QPushButton::connect(this->adauga, &QPushButton::clicked, [&] {
		this->adaugaProdus();
		});

	layout->addWidget(this->slider);
	this->slider->setRange(0, 100);

	QObject::connect(this->slider, &QSlider::valueChanged, [&] {
		this->update(this->service.getAll());
		});

	return layout;
}

QVBoxLayout* UI::setTableLayout()
{
	QVBoxLayout* layout = new QVBoxLayout;
	
	layout->addWidget(this->table);

	this->table->setModel(this->tableModel);

	return layout;
}

void UI::adaugaProdus()
{
	int id = this->id->text().toInt();
	std::string nume = this->nume->text().toStdString();
	std::string tip = this->tip->text().toStdString();
	double pret = this->pret->text().toDouble();
	try {
		this->service.adauga(Produs(id, nume, tip, pret));
	}
	catch (const RepoException& ex) {
		QMessageBox::warning(this, "RepoException", ex.getMesaj().c_str());
	}
	catch (const ServiceException& ex) {
		QMessageBox::warning(this, "ServiceException", ex.getMesaj().c_str());
	}

	this->update(this->service.getAll());
}

void UI::update(const std::vector <Produs>& arr)
{
	tableModel->setProductArray(arr, slider->value());
	for (auto it : arr)
		if (!isOpen[it.getTip()]) {
			UiLabels* newLabel = new UiLabels(*this, 0, it.getTip());
			newLabel->show();
		}
	this->signal();
}

UI::UI(Service& s) : service{s}
{
	QHBoxLayout* mainLayout = new QHBoxLayout;
	this->setLayout(mainLayout);

	mainLayout->addLayout(setTableLayout());
	mainLayout->addLayout(this->setProductLayout());

	this->update(this->service.getAll());
}
