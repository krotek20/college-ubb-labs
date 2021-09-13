#pragma once
#include "observer.h"
#include <QWidget>
#include "ui.h"
#include <QLabel>
#include <string>

class UiLabels : public QWidget, public Observable {
private:
	int value = 0;

	QLabel* label = new QLabel;

	UI& ui;

	std::string type;
public:

	UiLabels(UI& ui, int initialValue, std::string type) : ui{ ui }, value{ initialValue }, type{ type } {
		ui.addObservable(this);
		this->setWindowTitle(QString::fromStdString(type));
		this->ui.isOpen[type] = true;

		QVBoxLayout* main = new QVBoxLayout;
		this->setLayout(main);
		main->addWidget(label);
	}

	void signal() override;

	~UiLabels() {
		ui.removeObservable(this);
		this->ui.isOpen[type] = false;
	}
};