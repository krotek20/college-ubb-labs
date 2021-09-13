#include "Console.h"
#include <iostream>
#include <string>

using std::string;
using std::cout;
using std::cin;

void ConsoleUI::tipareste(const vector<Offer>& offers) {
    cout << "\nOffers:\n";
    bool ok = false;
    for (const Offer& o : offers) {
        cout << o.toString();
        ok = true;
    }
    if (!ok) {
        cout << "The list is empty!\n";
    }
    cout << "End of list!\n";
}

void ConsoleUI::tipareste_DTO(const vector<EntityCountDTO>& list) {
    for (auto ecdto : list) {
        cout << "Name: " << ecdto.getName() << "---Type: " << ecdto.getType() << "---Type Count: " << ecdto.getCount() << '\n';
    }
}

void ConsoleUI::addUI() {
    string name, dest, type;
    int price;
    cout << "Insert name: "; cin >> name;
    cout << "Insert destination: "; cin >> dest;
    cout << "Insert type: "; cin >> type;
    cout << "Insert price: "; cin >> price;
    ctr.addOffer(name, dest, type, price);
    cout << "SUCCES!\n";
}

void ConsoleUI::modifyUI() {
    string name, dest, type;
    int price;
    cout << "Insert name: "; cin >> name;
    cout << "Insert destination: "; cin >> dest;
    cout << "Insert type: "; cin >> type;
    cout << "Insert price: "; cin >> price;
    ctr.modOffer(name, dest, type, price);
    cout << "SUCCES!\n";
}

void ConsoleUI::removeUI() {
    string name;
    cout << "Insert name: "; cin >> name;
    ctr.removeOffer(name);
    cout << "SUCCES!\n";
}

void ConsoleUI::start() {
    while (true) {
        cout << "\nMain menu:\n";
        cout << "1 View Offers\n2 Add\n3 Modify\n4 Remove\n5 Filter offers by destination\n6 Filter offers by price\n";
        cout << "7 Sort by name\n8 Sort by destination\n9 Sort by type+price\n10 Raport type\n11 Wishlist\n";
        cout << "12 Pret total\n13 Undo\n0 Exit\nInsert command: ";
        int cmd;
        string dest, name, fileName;
        cin >> cmd;
        try {
            switch (cmd) {
            case 1:
                tipareste(ctr.getAll());
                break;
            case 2:
                addUI();
                break;
            case 3:
                modifyUI();
                break;
            case 4:
                removeUI();
                break;
            case 5:
                cout << "Insert destination: "; cin >> dest;
                tipareste(ctr.filterDest(dest));
                break;
            case 6:
                int price;
                cout << "Insert price: "; cin >> price;
                tipareste(ctr.filterPrice(price));
                break;
            case 7:
                tipareste(ctr.sortByName());
                break;
            case 8:
                tipareste(ctr.sortByDest());
                break;
            case 9:
                tipareste(ctr.sortByTypePrice());
                break;
            case 10:
                tipareste_DTO(ctr.raportByType());
                break;
            case 11:
                int cmdWL;
                do {
                    cout << "\nWishlist Menu:\n";
                    cout << "1 View list\n2 Add to list\n3 Delete list\n4 Generate random\n5 Export\n0 Back\nInsert command: ";
                    cin >> cmdWL;
                    switch (cmdWL) {
                    case 1:
                        tipareste(ctr.getAllWL());
                        cout << "Elements in cart: " << ctr.getAllWL().size() << '\n';
                        break;
                    case 2:
                        cout << "Insert name: "; cin >> name;
                        ctr.addToWL(name);
                        cout << "SUCCES!\nElements in cart: " << ctr.getAllWL().size() << '\n';
                        break;
                    case 3:
                        ctr.clearWL();
                        cout << "Elements in cart: " << ctr.getAllWL().size() << '\n';
                        break;
                    case 4:
                        size_t offerCount;
                        cout << "Insert number: "; cin >> offerCount;
                        ctr.randomWL(offerCount);
                        cout << "SUCCES!\nElements in cart: " << ctr.getAllWL().size() << '\n';
                        break;
                    case 5:
                        cout << "Insert file name: "; cin >> fileName;
                        ctr.exportHTML(fileName);
                        cout << "SUCCES!\nElements in cart: " << ctr.getAllWL().size() << '\n';
                        break;
                    case 0:
                        break;
                    default:
                        cout << "Invalid command!\n";
                    }
                } while (cmdWL != 0);
                break;
            case 12:
                cout << "Total price: " << ctr.totalPrice() << '\n';
                break;
            case 13:
                ctr.undo();
                tipareste(ctr.getAll());
                break;
            case 0:
                return;
            default:
                cout << "Invalid command!\n";
            }
        }
        catch (const OfferException ex) {
            cout << ex.getMsg() << '\n';
        }
        catch (const ValidateException ex) {
            cout << ex << '\n';
        }
    }
}