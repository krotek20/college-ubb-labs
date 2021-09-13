#include "labels.h"

void UiLabels::signal()
{
	int cont = 0;
	auto v = this->ui.service.getAll();
	for (auto it : v)
		if (it.getTip() == type)
			cont++;
	this->label->setText(QString::number(cont));
}
