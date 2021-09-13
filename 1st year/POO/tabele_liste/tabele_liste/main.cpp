#include "tabele_liste.h"
#include <QtWidgets/QApplication>
#include <vector>
#include "domain.h"
#include "tabel_ui.h"
#include "lista_ui.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    
    std::vector <Student> v = { Student("Stan", "Adi", 2), Student("Vintila", "Radu", 23), Student("Suciu", "Alin", 233) };

    //TabelUi ui(v);
    ListUi ui(v);

    ui.show();

    return a.exec();
}
