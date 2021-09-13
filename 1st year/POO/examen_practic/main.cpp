#include "ExamenPractic.h"
#include <QtWidgets/QApplication>
#include "domain.h"
#include "repository.h"
#include "service.h"
#include "GUI.h"

void testAll() {
    testDomain();
    testRepo();
    testService();
}

int main(int argc, char *argv[])
{
    //teste
    testAll();

    //backend
    Repo r{ "Repo.txt" };
    srv s{ r };

    //frontend
    QApplication a(argc, argv);
    GUI g{ s };
    g.show();
    return a.exec();
}
