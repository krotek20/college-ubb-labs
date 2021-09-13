#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_produse.h"

class produse : public QMainWindow
{
    Q_OBJECT

public:
    produse(QWidget *parent = Q_NULLPTR);

private:
    Ui::produseClass ui;
};
