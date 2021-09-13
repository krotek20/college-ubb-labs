from service import *
import itertools


# meniuri
def tipareste_meniu():
    """
    functia de afisare a meniului principal
    """

    meniu = '''
    Alegeti optiunea dorita:
    1. Submeniu adaugare
    2. Submeniu stergere
    3. Cautare
    4. Rapoarte
    5. Submeniu filtrare
    6. Undo
    0. Iesire aplicatie
    '''
    print(meniu)


def meniu_adaugare(cont, undo_list):
    """
    functia prin care se afiseaza submeniul adaugare
    :param undo_list: lista prin care se tine minte ultima comanda efectuata
    :param cont: instanta de cont bancar
    """

    meniu_adauga = '''
    Alegeti optiunea dorita:
    1. Afisare tranzactii curente
    2. Adaugare tranzactie
    3. Modificare tranzactie
    0. Intoarcere la meniul principal
    '''

    options_adaugare = {
        "1": ui_afisare_tranzactii,
        "2": ui_adaugare_tranzactie,
        "3": ui_modificare_tranzactie
    }

    ok = True
    while ok is True:
        print(meniu_adauga)
        try:
            option = input("Alegeti optiunea: ")
            if option == "0":
                ok = False
            elif option == "1":
                options_adaugare[option](cont)
            elif option in options_adaugare:
                options_adaugare[option](cont, undo_list)
        except ValueError:
            print("Nu ati introdus o optiune valida!")
        except KeyError:
            print("Nu ati introdus o optiune valida!")


def meniu_stergere(cont, undo_list):
    """
    functia prin care se afiseaza submeniul stergere
    :param undo_list: lista prin care se tine minte ultima comanda efectuata
    :param cont: instanta de cont bancar
    """

    meniu_sterge = '''
    Alegeti optiunea dorita:
    1. Sterge toate tranzactiile de la ziua specificata
    2. Sterge tranzactiile dintr-o anumita perioada
    3. Sterge toate tranzactiile de un anumit tip
    0. Intoarcere la meniul principal
    '''

    options_stergere = {
        "1": ui_stergere_zi,
        "2": ui_stergere_perioada,
        "3": ui_stergere_tip
    }

    ok = True
    while ok is True:
        print(meniu_sterge)
        try:
            option = input("Alegeti optiunea: ")
            if option == "0":
                ok = False
            if option in options_stergere:
                options_stergere[option](cont, undo_list)
        except ValueError:
            print("Nu ati introdus o optiune valida!")
        except KeyError:
            print("Nu ati introdus o optiune valida!")


def meniu_cautari(cont, option):
    """
    functia prin care se afiseaza submeniul cautari
    :param cont: instanta de cont bancar
    """

    """meniu_cauta = '''
    Alegeti optiunea dorita:
    1. Cauta tranzactiile cu suma mai mare decat o suma data
    2. Cauta tranzactiile efectuate inainte de o zi si mai mari decat o suma
    3. Cauta tranzactiile de un anumit tip
    0. Intoarcere la meniul principal
    '''"""

    options_cautare = {
        "1": ui_cautare_suma_mare,
        "2": ui_cautare_zi_suma,
        "3": ui_cautare_tip
    }

    ok = True
    while ok is True:
        # print(meniu_cauta)
        try:
            # option = input("Alegeti optiunea: ")
            if option == "0":
                ok = False
            if option in options_cautare:
                options_cautare[option](cont)
                ok = False
        except ValueError:
            print("Nu ati introdus o optiune valida!")
        except KeyError:
            print("Nu ati introdus o optiune valida!")


def meniu_rapoarte(cont, option):
    """
    functia prin care se afiseaza submeniul de rapoarte
    :param cont: instanta de cont bancar
    """

    """meniu_raport = '''
    Alegeti optiunea dorita:
    1. Suma totala a tranzactiilor de un anumit tip
    2. Soldul contului la o data specificata
    3. Tipareste toate tranzactiile de un anumit tip ordonate dupa suma
    0. Intoarcere la meniul principal
    '''"""

    options_rapoarte = {
        "1": ui_suma_totala_tip,
        "2": ui_sold_data,
        "3": ui_sortare_suma_tip
    }

    ok = True
    while ok is True:
        # print(meniu_raport)
        try:
            # option = input("Alegeti optiunea: ")
            if option == "0":
                ok = False
            if option in options_rapoarte:
                options_rapoarte[option](cont)
                ok = False
        except ValueError:
            print("Nu ati introdus o optiune valida!")
        except KeyError:
            print("Nu ati introdus o optiune valida!")


def meniu_filtrare(cont):
    """
    functia prin care se afiseaza submeniul de filtrare
    :param cont: instanta de cont bancar
    """

    meniu_filtru = '''
    Alegeti optiunea dorita:
    1. Elimina toate tranzactiile de un anumit tip
    2. Elimina toate tranzactiile mai mici decat o suma data care au tipul specificat
    0. Intoarcere la meniul principal
    '''

    options_filtrare = {
        "1": ui_elimina_tip,
        "2": ui_elimina_suma_tip
    }

    ok = True
    while ok is True:
        print(meniu_filtru)
        try:
            option = input("Alegeti optiunea: ")
            if option == "0":
                ok = False
            if option in options_filtrare:
                options_filtrare[option](cont)
        except ValueError:
            print("Nu ati introdus o optiune valida!")
        except KeyError:
            print("Nu ati introdus o optiune valida!")


# functii ui
def ui_afisare_tranzactii(cont):
    if len(cont) == 0:
        print("Nu exista tranzactii in cont!")
    else:
        for tranzactie in cont:
            print(tranzactie)


def ui_adaugare_tranzactie(cont, undo_list):
    counter = itertools.count(len(cont) + 1)

    print("Introduceti ziua, suma si tipul tranzactiei")
    zi = input("zi: ")
    suma = input("suma: ")
    tip = input("tip: ")
    my_id = next(counter)

    adaugare_tranzactie(cont, my_id, zi, suma, tip, undo_list)


def ui_modificare_tranzactie(cont, undo_list):
    current_id = input("Introduceti id-ul tranzactiei pe care doriti sa o modificati: ")
    try:
        current_id = int(current_id)
    except ValueError:
        print("Introduceti o valoare valida!")

    if cauta_tranzactie(cont, current_id) is True:
        print("Introduceti datele noii tranzactii (zi, suma, tip): ")
        zi = int(input("zi: "))
        suma = int(input("suma: "))
        tip = input("tip: ")
        modificare_tranzactie(cont, current_id, zi, suma, tip, undo_list)
    else:
        print("Nu exista o tranzactie cu acest id!")


def ui_stergere_zi(cont, undo_list):
    zi = int(input("Introduceti ziua: "))
    print(stergere_zi(cont, zi, undo_list))


def ui_stergere_perioada(cont, undo_list):
    zi_inceput = int(input("Introduceti ziua de inceput: "))
    while True:
        zi_sfarsit = int(input("Introduceti ziua de sfarsit: "))
        if zi_sfarsit >= zi_inceput:
            break
    print(stergere_perioada(cont, zi_inceput, zi_sfarsit, undo_list))


def ui_stergere_tip(cont, undo_list):
    tip = input("Introduceti tipul: ")
    print(stergere_tip(cont, tip, undo_list))


def ui_cautare_suma_mare(cont):
    suma = input("Introduceti suma: ")
    try:
        suma = int(suma)
        print(cautare_suma_mare(cont, suma))
    except ValueError:
        print("Introduceti o valoare valida!")


def ui_cautare_zi_suma(cont):
    zi = input("Introduceti ziua: ")
    suma = input("Introduceti suma: ")
    try:
        zi = int(zi)
        suma = int(suma)
        print(cautare_zi_suma(cont, zi, suma))
    except ValueError:
        print("Introduceti o valoare valida!")


def ui_cautare_tip(cont):
    tip = input("Introduceti tip: ")
    print(cautare_tip(cont, tip))


def ui_suma_totala_tip(cont):
    tip = input("Introduceti tip: ")
    print(calculeaza_suma_totala_tip(cont, tip))


def ui_sold_data(cont):
    data = int(input("Introduceti data: "))
    print(sold_data(cont, data))


def ui_sortare_suma_tip(cont):
    tip = input("Introduceti tip: ")
    print(sortare_suma_tip(cont, tip))


def ui_elimina_tip(cont):
    tip = input("Introduceti tip: ")
    print(elimina_tip(cont, tip))


def ui_elimina_suma_tip(cont):
    suma = int(input("Introduceti suma: "))
    tip = input("Introduceti tip: ")
    print(elimina_suma_tip(cont, suma, tip))


def ui_undo(cont, undo_list):
    preferinta = input("Sunteti sigur ca doriti sa faceti undo la ultima comanda "
                       "prin care s-a modificat lista? (DA/NU)\n")
    if preferinta.lower() == "da":
        print(undo(cont, undo_list))
    elif preferinta.lower() == "nu":
        pass
    else:
        print("Puteti sa raspundeti doar cu DA sau NU!")


def run_ui():
    """
    Principala functie prin care se va tipari meniul si
    vor fi introduse valori pentru alegerea unei optiuni valide
    Input: un numar de la 0 la 6
    Output: meniul principal
    """

    # DUMMY DATA
    tranzactie1 = creeaza_tranzactie(1, 15, 25, "in")
    tranzactie2 = creeaza_tranzactie(2, 12, 10, "in")
    tranzactie3 = creeaza_tranzactie(3, 28, 90, "out")
    cont = [tranzactie1, tranzactie2, tranzactie3]
    undo_list = []

    options = {
        "1": meniu_adaugare,
        "2": meniu_stergere,
        "3": meniu_cautari,
        "4": meniu_rapoarte,
        "5": meniu_filtrare,
        "6": ui_undo
    }

    while True:
        tipareste_meniu()
        option = input("Alege optiunea: ")
        try:
            if len(option) == 1:
                if option == "0":
                    print("=============================================\n"
                          "Good Bye!\n"
                          "=============================================\n")
                    return
                if option == "1" or option == "2" or option == "6":
                    options[option](cont, undo_list)
                elif option == "5":
                    options[option](cont)
            else:
                tokens = option.split()
                for token in tokens:
                    comanda = token.split("-")
                    if comanda[0].lower() == "cautare" and 1 <= int(comanda[1]) <= 3:
                        meniu_cautari(cont, comanda[1])
                    elif comanda[0].lower() == "rapoarte" and 1 <= int(comanda[1]) <= 3:
                        meniu_rapoarte(cont, comanda[1])
                    else:
                        print("Comanda invalida!")
        except ValueError:
            print("Nu ati introdus o optiune valida!")
        except KeyError:
            print("Nu ati introdus o optiune valida!")
