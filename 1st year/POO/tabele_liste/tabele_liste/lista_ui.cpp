#include "lista_ui.h"
#include <QVBoxLayout>
#include <QLineEdit>

ListUi::ListUi(std::vector<Student>& stArr) : stArr{stArr}
{
	QVBoxLayout* mainLayout = new QVBoxLayout();
	this->setLayout(mainLayout);

	mainLayout->addWidget(this->list);

	/*
	this->list->clear();

	for (auto it : stArr) {
		this->list->addItem(new QListWidgetItem(QString::fromStdString(it.toString())));
	}*/

	QLineEdit* nume = new QLineEdit();
	QLineEdit* prenume = new QLineEdit();
	QLineEdit* id = new QLineEdit();

	mainLayout->addWidget(nume);
	mainLayout->addWidget(prenume);
	mainLayout->addWidget(id);
	/*
	QObject::connect(this->list, &QListWidget::itemSelectionChanged, [=] {
		auto list = this->list->selectedItems();
		if (list.size() == 0)
			return;
		QString text = list[0]->text();
		auto splittedText = text.split(" ");
		nume->setText(splittedText[0]);
		prenume->setText(splittedText[1]);
		id->setText(splittedText[2]);
		});*/

	this->list->setModel(new ListModel(this->stArr));

	QObject::connect(this->list->selectionModel(), &QItemSelectionModel::selectionChanged, [=] {
		auto items = this->list->selectionModel()->selectedIndexes();
		if (items.size() == 0)
			return;
		QString text = items[0].data().toString();
		auto splittedText = text.split(" ");
		nume->setText(splittedText[0]);
		prenume->setText(splittedText[1]);
		id->setText(splittedText[2]);
		});
}

int ListModel::rowCount(const QModelIndex& parent) const
{
	return arr.size();
}

int ListModel::columnCount(const QModelIndex& parent) const
{
	return 1;
}

QVariant ListModel::data(const QModelIndex& index, int role) const
{
	if (role == Qt::DisplayRole) {
		return QString::fromStdString(this->arr[index.row()].toString());
	}
	return QVariant();
}
