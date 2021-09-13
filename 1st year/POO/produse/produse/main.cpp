#include "produse.h"
#include <QtWidgets/QApplication>
#include "tests.h"
#include "ui.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    testAll();
    
    Repository repo("produse.txt");
    Service service(repo);
    UI ui(service);
    ui.show();

    return a.exec();
}
