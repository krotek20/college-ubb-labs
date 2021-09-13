#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_tabele_liste.h"

class tabele_liste : public QMainWindow
{
    Q_OBJECT

public:
    tabele_liste(QWidget *parent = Q_NULLPTR);

private:
    Ui::tabele_listeClass ui;
};
