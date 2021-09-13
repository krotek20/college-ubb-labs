#include "tabel_ui.h"
#include <QVBoxLayout>
#include <QLineEdit>

TabelUi::TabelUi(std::vector<Student>& stArr) : stArr{ stArr } {
	QVBoxLayout* mainLayout = new QVBoxLayout;
	this->setLayout(mainLayout);
	/*
	this->table->setColumnCount(3);

	mainLayout->addWidget(this->table);

	
	this->table->clear();
	this->table->setHorizontalHeaderLabels({ "Nume", "Prenume", "Id" });

	this->table->setRowCount(this->stArr.size());
	for (int i = 0; i < this->stArr.size(); i++) {
		this->table->setItem(i, 0, new QTableWidgetItem(this->stArr[i].getNume().c_str()));
		this->table->setItem(i, 1, new QTableWidgetItem(this->stArr[i].getPrenume().c_str()));
		this->table->setItem(i, 2, new QTableWidgetItem(QString::number(this->stArr[i].getId())));
	}

	this->table->setSelectionBehavior(QAbstractItemView::SelectionBehavior::SelectRows);

	QLineEdit* nume = new QLineEdit();
	QLineEdit* prenume = new QLineEdit();
	QLineEdit* id = new QLineEdit();

	mainLayout->addWidget(nume);
	mainLayout->addWidget(prenume);
	mainLayout->addWidget(id);

	QWidget::connect(this->table, &QTableWidget::itemSelectionChanged, [this, nume, prenume, id] {
		auto item = this->table->selectedItems();
		if (item.size() == 0)
			return;
		nume->setText(item[0]->text());
		prenume->setText(item[1]->text());
		id->setText(item[2]->text());
		});
		*/

	this->table->setModel(new TableModel(this->stArr));
	mainLayout->addWidget(this->table);

	this->table->setSelectionBehavior(QAbstractItemView::SelectionBehavior::SelectRows);
	this->table->setSelectionMode(QAbstractItemView::SelectionMode::SingleSelection);

	QLineEdit* nume = new QLineEdit();
	QLineEdit* prenume = new QLineEdit();
	QLineEdit* id = new QLineEdit();

	mainLayout->addWidget(nume);
	mainLayout->addWidget(prenume);
	mainLayout->addWidget(id);

	QObject::connect(this->table->selectionModel(), &QItemSelectionModel::selectionChanged, [this, nume, prenume, id] {
		auto item = this->table->selectionModel()->selectedIndexes();
		if (item.size() == 0)
			return;
		nume->setText(item[0].data().toString());
		prenume->setText(item[1].data().toString());
		id->setText(item[2].data().toString());
		});

}

int TableModel::rowCount(const QModelIndex& parent) const
{
	return arr.size();
}

int TableModel::columnCount(const QModelIndex& parent) const
{
	return 3;
}

QVariant TableModel::data(const QModelIndex& index, int role) const
{
	if (role == Qt::DisplayRole) {
		switch (index.column()){
		case 0:
			return QString::fromStdString(arr[index.row()].getNume());
		case 1:
			return QString::fromStdString(arr[index.row()].getPrenume());
		case 2:
			return QString::number(arr[index.row()].getId());
		}
	}
	return QVariant();
}
