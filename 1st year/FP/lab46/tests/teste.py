from service import *


def test_creare_tranzactie():
    tranzactie = creeaza_tranzactie(1, 17, 200, "in")
    assert get_id(tranzactie) == 1
    assert get_zi(tranzactie) == 17
    assert get_suma(tranzactie) == 200
    assert get_tip(tranzactie) == "in"


def test_adaugare():
    tranzactie1 = creeaza_tranzactie(1, 5, 50, "in")
    tranzactie2 = creeaza_tranzactie(2, 15, 29, "in")
    tranzactie3 = creeaza_tranzactie(3, 10, 25, "out")
    cont = [tranzactie1, tranzactie2, tranzactie3]
    adaugare_tranzactie(cont, 4, 21, 35, "in", [])
    assert cont == [tranzactie1, tranzactie2, tranzactie3, {'id': 4, 'zi': 21, 'suma': 35, 'tip': "in"}]


def test_modificare():
    tranzactie1 = creeaza_tranzactie(1, 5, 50, "in")
    cont = [tranzactie1]
    modificare_tranzactie(cont, 1, 21, 35, "out", [])
    assert cont == [{'id': 1, 'zi': 21, 'suma': 35, 'tip': "out"}]


def test_stergere_zi():
    tranzactie1 = creeaza_tranzactie(1, 12, 450, "in")
    tranzactie2 = creeaza_tranzactie(2, 21, 17, "in")
    tranzactie3 = creeaza_tranzactie(3, 28, 90, "out")
    tranzactie4 = creeaza_tranzactie(4, 28, 120, "out")
    cont = [tranzactie1, tranzactie2, tranzactie3, tranzactie4]
    assert stergere_zi(cont, 21, []) == "Stergere efectuata cu succes!"
    assert stergere_zi(cont, 28, []) == "Stergere efectuata cu succes!"
    assert stergere_zi(cont, 2, []) == "Nu exista tranzactii efectuate in ziua specificata"


def test_stergere_perioada():
    tranzactie1 = creeaza_tranzactie(1, 12, 450, "in")
    tranzactie2 = creeaza_tranzactie(2, 21, 17, "in")
    tranzactie3 = creeaza_tranzactie(3, 28, 90, "out")
    tranzactie4 = creeaza_tranzactie(4, 28, 120, "out")
    cont = [tranzactie1, tranzactie2, tranzactie3, tranzactie4]
    assert stergere_perioada(cont, 10, 27, []) == "Stergere efectuata cu succes!"
    assert stergere_perioada(cont, 28, 28, []) == "Stergere efectuata cu succes!"
    assert stergere_perioada(cont, 1, 10, []) == "Nu exista tranzactii efectuate in perioada specificata!"


def test_stergere_tip():
    tranzactie1 = creeaza_tranzactie(1, 12, 450, "in")
    tranzactie2 = creeaza_tranzactie(2, 21, 17, "in")
    tranzactie3 = creeaza_tranzactie(3, 28, 90, "out")
    tranzactie4 = creeaza_tranzactie(4, 28, 120, "out")
    cont = [tranzactie1, tranzactie2, tranzactie3, tranzactie4]
    assert stergere_tip(cont, "in", []) == "Stergere efectuata cu succes!"
    assert stergere_tip(cont, "out", []) == "Stergere efectuata cu succes!"
    assert stergere_tip(cont, "WOW", []) == "Nu exista tranzactii de acest tip in contul bancar!"


def test_cautare_suma_mare():
    tranzactie1 = creeaza_tranzactie(1, 5, 50, "in")
    tranzactie2 = creeaza_tranzactie(2, 15, 29, "in")
    tranzactie3 = creeaza_tranzactie(3, 10, 25, "out")
    cont = [tranzactie1, tranzactie2, tranzactie3]
    assert cautare_suma_mare(cont, 28) == [
        {'id': 1, 'zi': 5, 'suma': 50, 'tip': "in"},
        {'id': 2, 'zi': 15, 'suma': 29, 'tip': "in"}
    ]
    assert cautare_suma_mare(cont, 51) == "Nu s-au gasit tranzactii cu sume mai mari decat suma data in contul bancar!"


def test_cautare_zi_suma():
    tranzactie1 = creeaza_tranzactie(1, 5, 50, "in")
    tranzactie2 = creeaza_tranzactie(2, 15, 29, "in")
    tranzactie3 = creeaza_tranzactie(3, 10, 25, "out")
    cont = [tranzactie1, tranzactie2, tranzactie3]
    assert cautare_zi_suma(cont, 10, 35) == [{'id': 1, 'zi': 5, 'suma': 50, 'tip': 'in'}]
    assert cautare_zi_suma(cont, 15, 55) == "Nu s-au gasit tranzactii efectuate inainte de ziua data care sa aiba o " \
                                            "suma mai mare decat suma data in contul bancar!"


def test_cautare_tip():
    tranzactie1 = creeaza_tranzactie(1, 5, 50, "in")
    tranzactie2 = creeaza_tranzactie(2, 15, 29, "in")
    cont = [tranzactie1, tranzactie2]
    assert cautare_tip(cont, "in") == [
        {'id': 1, 'zi': 5, 'suma': 50, 'tip': "in"},
        {'id': 2, 'zi': 15, 'suma': 29, 'tip': "in"}
    ]
    assert cautare_tip(cont, "out") == "Nu s-au gasit tranzactii de acest tip in contul bancar!"
    assert cautare_tip(cont, "WOW") == "Nu s-au gasit tranzactii de acest tip in contul bancar!"


def test_calculeaza_suma_totala_tip():
    tranzactie1 = creeaza_tranzactie(1, 5, 50, "in")
    tranzactie2 = creeaza_tranzactie(2, 15, 29, "in")
    tranzactie3 = creeaza_tranzactie(3, 10, 25, "out")
    cont = [tranzactie1, tranzactie2, tranzactie3]
    assert calculeaza_suma_totala_tip(cont, "in") == 79
    assert calculeaza_suma_totala_tip(cont, "out") == 25
    assert calculeaza_suma_totala_tip(cont, "WOW") == "Nu s-au gasit tranzactii de acest tip in contul bancar!"


def test_sold_data():
    tranzactie1 = creeaza_tranzactie(1, 5, 50, "in")
    tranzactie2 = creeaza_tranzactie(2, 15, 29, "in")
    tranzactie3 = creeaza_tranzactie(3, 10, 25, "out")
    cont = [tranzactie1, tranzactie2, tranzactie3]
    assert sold_data(cont, 16) == 54  # 50 - 25 + 29
    assert sold_data(cont, 5) == 50
    assert sold_data(cont, 3) == 0


def test_sortare_suma_tip():
    tranzactie1 = creeaza_tranzactie(1, 15, 25, "in")
    tranzactie2 = creeaza_tranzactie(2, 12, 10, "in")
    tranzactie3 = creeaza_tranzactie(3, 21, 17, "in")
    tranzactie4 = creeaza_tranzactie(4, 28, 90, "out")
    cont = [tranzactie1, tranzactie2, tranzactie3, tranzactie4]
    assert sortare_suma_tip(cont, "in") == [
        {'id': 2, 'zi': 12, 'suma': 10, 'tip': "in"},
        {'id': 3, 'zi': 21, 'suma': 17, 'tip': "in"},
        {'id': 1, 'zi': 15, 'suma': 25, 'tip': "in"}
    ]
    assert sortare_suma_tip(cont, "out") == [
        {'id': 4, 'zi': 28, 'suma': 90, 'tip': "out"}
    ]
    assert sortare_suma_tip(cont, "WOW") == "Nu exista tranzactii de acest tip!"


def test_elimina_tip():
    tranzactie1 = creeaza_tranzactie(1, 15, 25, "in")
    tranzactie2 = creeaza_tranzactie(2, 12, 10, "in")
    tranzactie3 = creeaza_tranzactie(3, 28, 90, "out")
    cont = [tranzactie1, tranzactie2, tranzactie3]
    assert elimina_tip(cont, "in") == [
        {'id': 3, 'zi': 28, 'suma': 90, 'tip': "out"}
    ]
    assert elimina_tip(cont, "out") == [
        {'id': 1, 'zi': 15, 'suma': 25, 'tip': "in"},
        {'id': 2, 'zi': 12, 'suma': 10, 'tip': "in"}
    ]
    assert elimina_tip(cont, "WOW") == "Tipul specificat nu este valid!"


def test_elimina_suma_tip():
    tranzactie1 = creeaza_tranzactie(1, 15, 25, "in")
    tranzactie2 = creeaza_tranzactie(2, 12, 10, "in")
    tranzactie3 = creeaza_tranzactie(3, 28, 90, "out")
    cont = [tranzactie1, tranzactie2, tranzactie3]
    assert elimina_suma_tip(cont, 24, "in") == [
        {'id': 1, 'zi': 15, 'suma': 25, 'tip': "in"},
        {'id': 3, 'zi': 28, 'suma': 90, 'tip': "out"}
    ]
    assert elimina_suma_tip(cont, 50, "in") == [
        {'id': 3, 'zi': 28, 'suma': 90, 'tip': "out"}
    ]
    assert elimina_suma_tip(cont, 10000, "WOW") == "Tipul specificat nu este valid!"


def run_all_tests():
    test_creare_tranzactie()
    test_adaugare()
    test_modificare()
    test_stergere_zi()
    test_stergere_perioada()
    test_stergere_tip()
    test_cautare_suma_mare()
    test_cautare_zi_suma()
    test_cautare_tip()
    test_calculeaza_suma_totala_tip()
    test_sold_data()
    test_sortare_suma_tip()
    test_elimina_tip()
    test_elimina_suma_tip()
