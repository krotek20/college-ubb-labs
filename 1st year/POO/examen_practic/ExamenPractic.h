#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_ExamenPractic.h"

class ExamenPractic : public QMainWindow
{
    Q_OBJECT

public:
    ExamenPractic(QWidget *parent = Q_NULLPTR);

private:
    Ui::ExamenPracticClass ui;
};
