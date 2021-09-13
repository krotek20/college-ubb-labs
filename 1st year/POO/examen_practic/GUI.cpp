#include "GUI.h"

GUI::GUI(srv& s) : s{ s } {
	QVBoxLayout* mainLy = new QVBoxLayout;
	this->setLayout(mainLy);

	QHBoxLayout* mLy = new QHBoxLayout;
	mainLy->addLayout(mLy);

	auto tableLy = initTableLayout();
	auto otherLy = initOtherLayout();

	mLy->addLayout(tableLy);
	mLy->addLayout(otherLy);

	QVBoxLayout* paintLy = new QVBoxLayout;
	mainLy->addLayout(paintLy);
	paintLy->setSpacing(10);
}

QVBoxLayout* GUI::initTableLayout() {
	QVBoxLayout* tableLy = new QVBoxLayout;
	tableLy->addWidget(this->items, 0, Qt::AlignTop);
	this->items->setModel(this->model);
	this->items->setSelectionBehavior(QAbstractItemView::SelectionBehavior::SelectRows);
	this->items->setSelectionMode(QAbstractItemView::SelectionMode::SingleSelection);
	return tableLy;
}

QVBoxLayout* GUI::initOtherLayout() {
	QVBoxLayout* otherLy = new QVBoxLayout;

	QFormLayout* formLy = new QFormLayout;
	formLy->addRow("Titlu: ", this->titlu);
	otherLy->addLayout(formLy);

	this->rank->setOrientation(Qt::Orientation::Horizontal);
	this->rank->setRange(0, 9);
	otherLy->addWidget(this->rank, 0 ,Qt::AlignTop);

	QPushButton* updateBtn = new QPushButton{ "&Update" };
	otherLy->addWidget(updateBtn, 0, Qt::AlignTop);

	QObject::connect(this->items->selectionModel(), &QItemSelectionModel::selectionChanged, [this]() {
		auto index = this->items->selectionModel()->selectedIndexes();
		if (index.size() == 0) {
			QMessageBox::warning(this, "Warning!", "Please select a row in table!");
			return;
		}
		this->titlu->setText(index[1].data().toString());
		this->rank->setValue(index[3].data().toInt());
	});

	QObject::connect(updateBtn, &QPushButton::clicked, [&]() {
		auto titluString = this->titlu->text().toStdString();
		auto rankInt = this->rank->value();
		auto index = this->items->selectionModel()->selectedIndexes();
		int id = index[0].data().toInt();

		this->s.updateSong(id, titluString, rankInt);
		this->updateTable(this->s.getAllSorted());
	});

	QPushButton* deleteBtn = new QPushButton{ "&Delete" };
	otherLy->addWidget(deleteBtn, 0, Qt::AlignTop);
	QObject::connect(deleteBtn, &QPushButton::clicked, [&]() {
		auto index = this->items->selectionModel()->selectedIndexes();
		int id = index[0].data().toInt();

		try {
			this->s.stergeSong(id);
		}
		catch (SongException & ex) {
			QMessageBox::warning(this, "Exception!", ex.getMsg().c_str());
			return;
		}
		this->updateTable(this->s.getAllSorted());
	});

	return otherLy;
}

void GUI::paintEvent(QPaintEvent*) {
	QPainter p{ this };
	int ranks[10] = { 0 };
	for (const auto& s : this->s.getAllSorted()) {
		ranks[s.first.getRank()]++;
	}
	for (int i = 0; i < 9; ++i) {
		// merge pus ranks[i] * 10 pentru o mai buna observare a valorilor in cazul in care sunt putine date
		p.drawLine(i * 20 + 10, height(), i * 20 + 10, height() - ranks[i] * 10);
	}
}

void GUI::updateTable(std::vector<std::pair<Song, int>> s) {
	this->model->setSongArr(s);
	this->items->setModel(model);
	repaint();
}

