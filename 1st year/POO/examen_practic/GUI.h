#pragma once
#include <QtWidgets/QWidget>
#include <qpushbutton.h>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QHBoxLayout>
#include <qslider.h>
#include <qlineedit.h>
#include <qformlayout.h>
#include <qtableview.h>
#include <qmessagebox.h>
#include <qpainter.h>
#include <qbrush.h>
#include <vector>
#include <string>
#include "service.h"
#include "domain.h"
#include "TableModel.h"

class GUI : public QWidget {
public:
	GUI(srv& s);
private:
	srv& s;

	QTableView* items = new QTableView;
	TableModel* model = new TableModel(this->s.getAllSorted());
	QLineEdit* titlu = new QLineEdit;
	QSlider* rank = new QSlider;

	QVBoxLayout* initTableLayout();
	QVBoxLayout* initOtherLayout();

	void paintEvent(QPaintEvent* ev) override;

	void updateTable(std::vector<std::pair<Song, int>> s);
};