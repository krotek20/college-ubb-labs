from domain import *
from copy import deepcopy


def valideaza_date(zi, suma, tip):
    """
    functie care verifica daca datele introduse pentru o tranzactie sunt valide
    :param zi: ziua tranzactiei
    :param suma: suma tranzactiei
    :param tip: tipul tranzactiei
    :return: Daca datele sunt valide se returneaza valoarea True, altfel se returneaza valoarea False
    """

    try:
        zi = int(zi)
        suma = int(suma)
        if zi >= 1 and suma >= 1 and (tip == "in" or tip == "out"):
            return True
    except ValueError:
        print("Introduceti date valide!")
    return False


def adaugare_tranzactie(cont, my_id, zi, suma, tip, undo_list):
    """
    functia de adaugare a unei noi tranzactii in cont
    aceasta va fi adaugata doar daca datele tranzactie vor fi valide
    :param undo_list: lista prin care se tine minte ultima comanda efectuata
    :param cont: instanta de cont bancar
    :param my_id: id-ul tranzactiei
    :param zi: ziua in care se creeaza tranzactia
    :param suma: suma pentru aceasta tranzactie
    :param tip: tipul tranzactiei
    """

    if valideaza_date(zi, suma, tip) is True:
        tranzactie = creeaza_tranzactie(my_id, zi, suma, tip)
        cont.append(tranzactie)
        print("Tranzactie creata cu succes!")

        copied_cont = deepcopy(cont)
        undo_list.append(copied_cont)
    else:
        print("Datele introduse nu sunt valide!")


def modificare_tranzactie(cont, current_id, zi, suma, tip, undo_list):
    """
    functia de modificare a unei tranzactii existenta se poate modifica ziua, suma, cat si tipul tranzactiei
    :param undo_list: lista prin care se tine minte ultima comanda efectuata
    :param cont: instanta de cont bancar
    :param tip: noul tip de tranzactie introdus de la tastatura
    :param suma: noua suma introdusa de la tastatura
    :param zi: noua zi introdusa de la tastatura
    :param current_id: id-ul tranzactiei ce se asteapta a fi schimbata
    """

    if valideaza_date(zi, suma, tip) is True:
        set_zi(cont[current_id - 1], zi)
        set_suma(cont[current_id - 1], suma)
        set_tip(cont[current_id - 1], tip)
        print("Modificare realizata cu succes!")

        copied_cont = deepcopy(cont)
        undo_list.append(copied_cont)
    else:
        print("Datele introduse nu sunt valide!")


def stergere_zi(cont, zi, undo_list):
    """
    functia care sterge tranzactiile din cont efectuate intr-o anumita zi
    :param undo_list: lista prin care se tine minte ultima comanda efectuata
    :param cont: instanta de cont bancar
    :param zi: ziua introdusa de la tastatura
    :return: Daca exista tranzactii efectuate in acea zi vor fi sterse din cont si va fi returnat mesajul:
            "Stergere efectuata cu succes!",
            altfel va fi returnat mesajul: "Nu exista tranzactii efectuate in ziua specificata"
    """

    my_list = []
    ok = False
    for tranzactie in cont:
        if int(get_zi(tranzactie)) == zi:
            ok = True
        else:
            my_list.append(tranzactie)
    cont[:] = my_list
    if ok is True:
        copied_cont = deepcopy(cont)
        undo_list.append(copied_cont)

        return "Stergere efectuata cu succes!"
    else:
        return "Nu exista tranzactii efectuate in ziua specificata"


def stergere_perioada(cont, zi_inceput, zi_sfarsit, undo_list):
    """
    functia care sterge tranzactiile din cont efectuate intr-o anumita perioada
    :param undo_list: lista prin care se tine minte ultima comanda efectuata
    :param cont: instanta de cont bancar
    :param zi_inceput: inceputul perioadei introdus de la tastatura
    :param zi_sfarsit: sfarsitul perioadei introdus de la tastatura
    :return: Daca exista tranzactii efectuate in perioada respectiva vor fi sterse din cont si va fi returnat mesajul:
            "Stergere efectuata cu succes!",
            altfel va fi returnat mesajul: "Nu exista tranzactii efectuate in perioada specificata!"
    """

    my_list = []
    ok = False
    for tranzactie in cont:
        if zi_inceput <= int(get_zi(tranzactie)) <= zi_sfarsit:
            ok = True
        else:
            my_list.append(tranzactie)
    cont[:] = my_list
    if ok is True:
        copied_cont = deepcopy(cont)
        undo_list.append(copied_cont)

        return "Stergere efectuata cu succes!"
    else:
        return "Nu exista tranzactii efectuate in perioada specificata!"


def stergere_tip(cont, tip, undo_list):
    """
    functia care sterge tranzactiile de un anumit tip din contul bancar
    :param undo_list: lista prin care se tine minte ultima comanda efectuata
    :param cont: instanta de cont bancar
    :param tip: tipul tranzactiilor introdus de la tastatura
    :return: Daca exista tranzactii de acest tip acestea vor fi sterse din cont si va fi returnat mesajul:
            "Stergere efectuata cu succes!",
            altfel va fi returnat mesajul: "Nu exista tranzactii de acest tip in contul bancar!"
    """

    my_list = []
    ok = False
    for tranzactie in cont:
        if get_tip(tranzactie) == tip:
            ok = True
        else:
            my_list.append(tranzactie)
    cont[:] = my_list
    if ok is True:
        copied_cont = deepcopy(cont)
        undo_list.append(copied_cont)

        return "Stergere efectuata cu succes!"
    else:
        return "Nu exista tranzactii de acest tip in contul bancar!"


def cautare_suma_mare(cont, suma):
    """
    functie care printeaza toate tranzactiile a caror suma este mai mare decat o suma data
    :param cont: instanta de cont bancar
    :param suma: suma introdusa de la tastatura
    :return: Daca exista astfel de tranzactii se va returna lista acestora, altfel se va returna mesajul:
            "Nu s-au gasit tranzactii cu sume mai mari decat suma data in contul bancar!"
    """

    my_list = []
    ok = False
    for tranzactie in cont:
        if int(get_suma(tranzactie)) > suma:
            ok = True
            my_list.append(tranzactie)
    if ok is True:
        return my_list
    else:
        return "Nu s-au gasit tranzactii cu sume mai mari decat suma data in contul bancar!"


def cautare_zi_suma(cont, zi, suma):
    """
    functie care printeaza toate tranzactiile a caror zi este mai mica decat o zi data iar suma lor este mai mare
    decat o suma data
    :param cont: instanta de cont bancar
    :param zi: ziua introdusa de la tastatura
    :param suma: suma introdusa de la tastatura
    :return: Daca exista astfel de tranzactii se va returna lista acestora,
    altfel se va returna mesajul: "Nu s-au gasit tranzactii efectuate inainte de ziua data care sa aiba o suma mai
    mare decat suma data in contul bancar!"
    """

    my_list = []
    ok = False
    for tranzactie in cont:
        if int(get_zi(tranzactie)) < zi and int(get_suma(tranzactie)) > suma:
            ok = True
            my_list.append(tranzactie)
    if ok is True:
        return my_list
    else:
        return "Nu s-au gasit tranzactii efectuate inainte de ziua data care sa aiba o " \
               "suma mai mare decat suma data in contul bancar!"


def cautare_tip(cont, tip):
    """
    functie care printeaza toate tranzactiile de un anumit tip
    :param cont: instanta de cont bancar
    :param tip: tipul tranzactiei introdus de la tastatura
    :return: Daca exista astfel de tranzactii se va returna lista acestora, altfel se va returna mesajul:
            "Nu s-au gasit tranzactii de acest tip in contul bancar!"
    """

    my_list = []
    ok = False
    for tranzactie in cont:
        if get_tip(tranzactie) == tip:
            ok = True
            my_list.append(tranzactie)
    if ok is True:
        return my_list
    else:
        return "Nu s-au gasit tranzactii de acest tip in contul bancar!"


def calculeaza_suma_totala_tip(cont, tip):
    """
    functia care calculeaza suma totala a tranzactiilor de un anumit tip
    :param cont: instanta de cont bancar
    :param tip: tipul tranzactiei introdus de la tastatura
    :return: Daca exista tranzactii de tipul dat, se returneaza suma lor, altfel se returneaza mesajul
            "Nu s-au gasit tranzactii de acest tip in contul bancar!"
    """

    suma = 0
    ok = False
    for tranzactie in cont:
        if get_tip(tranzactie) == tip:
            ok = True
            suma += int(get_suma(tranzactie))
    if ok is True:
        return suma
    else:
        return "Nu s-au gasit tranzactii de acest tip in contul bancar!"


def sold_data(cont, data):
    """
    functia care returneaza soldul curent al contului la o anumita data
    :param cont: instanta de cont bancar
    :param data: data la care se va calcula soldul
    :return: Daca exista tranzactii pana la acea data se returneaza soldul contului, altfel se returneaza valoarea 0
    """

    sold = 0
    for tranzactie in cont:
        if int(get_zi(tranzactie)) <= data:
            if get_tip(tranzactie) == "in":
                sold += int(get_suma(tranzactie))
            else:
                sold -= int(get_suma(tranzactie))
    return sold


def sorteaza_dupa_suma(list_to_be_sorted):
    """
    functia care sorteaza o lista de tranzactii dupa sumele acestora
    :param list_to_be_sorted: lista de tranzactii
    :return: my_list - lista de tranzactii
    """
    my_list = sorted(list_to_be_sorted, key=lambda k: k["suma"])
    return my_list


def sortare_suma_tip(cont, tip):
    """
    functia care returneaza o lista cu tranzactiile de un anumit tip, ordonante dupa suma
    :param cont: instanta de cont bancar
    :param tip: tipul tranzactiei
    :return: Daca exista tranzactii de tipul specificat se returneaza lista de tranzactii ordonate dupa suma,
            altfel se returneaza mesajul "Nu exista tranzactii de acest tip!"
    """

    my_list_not_sorted = []
    ok = False
    for tranzactie in cont:
        if get_tip(tranzactie) == tip:
            ok = True
            my_list_not_sorted.append(tranzactie)
    if ok is True:
        my_list = sorteaza_dupa_suma(my_list_not_sorted)
        return my_list
    else:
        return "Nu exista tranzactii de acest tip!"


def cauta_tranzactie(cont, tid):
    """
    functia care cauta o tranzactie in cont dupa un id specificat
    :param cont: instanta de cont bancar
    :param tid: id-ul tranzactiei
    :return: Daca exista o astfel de tranzactie se returneaza valoarea True, in caz contrar False
    """

    for tranzactie in cont:
        if tranzactie["id"] == tid:
            return True
    return False


def elimina_tip(cont, tip):
    """
    functia care afiseaza tranzactiile din contul bancar de un anumit tip
    :param cont: instanta de cont bancar
    :param tip: tipul tranzactiei
    :return: Lista tranzactiilor de tipul opus
            Daca tipul specificat nu este valid se va afisa mesajul: "Tipul specificat nu este valid!"
            Daca dupa eliminare nu mai exista tranzactii in contul bancar se va afisa mesajul:
            "Nu exista tranzactii in contul bancar!"
    """

    if tip != "in" and tip != "out":
        return "Tipul specificat nu este valid!"

    my_list = []
    if tip == "in":
        my_list = cautare_tip(cont, "out")
    elif tip == "out":
        my_list = cautare_tip(cont, "in")

    if isinstance(my_list, str):
        return "Nu exista tranzactii in contul bancar!"
    else:
        return my_list


def elimina_suma_tip(cont, suma, tip):
    """
    functia care elimina toate tranzactiile cu suma mai mica de o suma data care au tipul specificat
    :param cont: instanta de cont bancar
    :param suma: suma citita de la tastatura
    :param tip: tipul tranzactiei
    :return: lista tranzactiilor care nu vor fi eliminate
            Daca dupa eliminare nu mai exista tranzactii in contul bancar se va afisa mesajul:
            "Nu exista tranzactii in contul bancar!"
            Daca tipul specificat nu este valid se va afisa mesajul: "Tipul specificat nu este valid!"
    """

    if tip != "in" and tip != "out":
        return "Tipul specificat nu este valid!"

    my_list = []
    for tranzactie in cont:
        if int(get_suma(tranzactie)) >= suma or get_tip(tranzactie) != tip:
            my_list.append(tranzactie)
    if len(my_list) == 0:
        return "Nu exista tranzactii in contul bancar!"
    else:
        return my_list


def undo(cont, undo_list):
    """
    functia care face undo la ultima comanda executata in urma careia contul bancar a fost modificat
    :param undo_list: lista prin care se tine minte ultima comanda efectuata
    :param cont: instanta de cont bancar
    :return: Daca lista de undo e goala atunci va fi afisat mesajul: "Momentan nu s-a efectuat niciun fel de comanda!"
            Daca lista de undo are elemente se va copia in contul bancar ultimul element introdus
    """

    if len(undo_list) == 0:
        return "Momentan nu s-a efectuat niciun fel de comanda!"
    else:
        try:
            undo_list.pop()
            cont[:] = undo_list[-1]
            return "Ultima comanda refacuta cu succes!"
        except IndexError:
            cont[:] = []
