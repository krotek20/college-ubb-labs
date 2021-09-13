# meniu
def meniu_optiuni():
    """
    functie prin care poti alege o optiune dintr-un meniu
    """

    print("1. Citire lista de numere intregi\n"
          "2. Secventa de lungime maxima cu proprietatea 10\n"
          "3. Secventa de lungime maxima cu proprietatea 11\n"
          "4. Secventa de lungime maxima cu proprietatea 7\n"
          "5. Iesire")


# add function
def add_to_list(l, n):
    l.clear()

    print("Cititi cele " + str(n) + " numere!")
    for i in range(n):
        k = input()
        while True:
            try:
                k = int(k)
                l.append(k)
                break
            except ValueError:
                print("Nu puteti introduce alta valoare decat una numerica!")
                k = input()


# citire lista
def ui_add_list(l):
    """
    se introduce numarul dorit de elemente pe care le va avea lista
    daca acesta este valid, se introduc pe rand elementele listei
    """
    n = input("Introduceti numarul de elemente: ")
    while True:
        try:
            n = int(n)
            if n > 0:
                add_to_list(l, n)
                break
            else:
                print("Nu puteti introduce o lista cu mai putin de un element!")
                n = input()
        except ValueError:
            print("Nu puteti introduce alta valoare decat una numerica!")
            n = input()


def verify_prop_10(l, i):
    if (l[i + 1] < l[i] and l[i + 1] <= l[i + 2]) or (l[i + 1] >= l[i] and l[i + 1] > l[i + 2]):
        return True
    return False


# prop 10
def sequence_prop_10(l):
    """
    functia care returneaza secventa de lungime maxima din lista cu proprietatea ca
    diferentele l[i+1]-l[i] si l[i+2]-l[i+1] au semne contrare pentru i = 0...n-2
    unde n este numarul elementelor din lista l
    input: l - lista de elemente
    output: st - valoarea de inceput a secventei, dr - valoarea de sfarsit a secventei
    important: l ramane neschimbata
    ===============================================================================================================
    proprietatea data poate fi reinterpretata ca o problema de gasire a unei secvente de tip fierastrau
    bineinteles, secventa trebuie sa fie de lungime maxima
    ===============================================================================================================
    vom verifica aceasta proprietate la fiecare pas intr-un for a carui index este
    valoarea curenta din stanga subsecventei
    daca, de asemenea, secventa este de lungime maxima, aceasta va fi salvata in variabilele st si dr
    """

    # lista trebuie sa aiba minimum 3 elemente
    if len(l) < 3:
        return "Proprietatea nu se poate valida!"

    st = 0
    dr = 0
    ok = 0
    current_st = 0

    for i in range(len(l) - 2):
        if ok == 0:  # incepe o secventa noua
            current_st = i
            if verify_prop_10(l, i) is True:
                ok = 1  # s-a inceput o secventa
                if (i + 2) - current_st >= dr - st:
                    dr = i + 2
                    st = current_st
        else:  # se continua o secventa inceputa anterior
            if verify_prop_10(l, i) is True:
                if (i + 2) - current_st >= dr - st:
                    dr = i + 2
                    st = current_st
            else:
                ok = 0  # s-a sfarsit o secventa

    # daca au existat o secventa cu aceasta proprietate atunci va fi afisata
    if st != 0 or dr != 0:
        prop_10 = [st, dr]
        return prop_10
    return "Nu exista o secventa cu aceasta proprietate!"


def ui_prop_10(l):
    if len(l) == 0:
        print("Introduceti elemente in lista!")
        return
    seq = sequence_prop_10(l)
    print(seq)


# maximum value in l
def max_element(l):
    max_elem = l[0]
    for i in range(len(l)):
        if l[i] >= max_elem:
            max_elem = i
    return max_elem


# prop 11
def sequence_prop_11(l):
    """
    functia care returneaza secventa de lungime maxima din lista care are suma elementelor maxima
    input: l - lista de elemente
    output: sum - suma elementelor secventei, st - valoarea de inceput a secventei, dr - valoarea de sfarsit a secventei
    important: l ramane neschimbata
    """

    # verific daca nu exista o secventa de un element care sa satisfaca proprietatea
    x = max_element(l)

    prop_11 = []
    st = 0
    dr = 0

    # suma maxima va fi comparata de fiecare data cu suma elementelor din secventa
    # daca aceasta nu se va schimba, atunci primul element din lista va avea suma maxima
    smax = l[0]

    # vom citi lista cu ajutorul a doua for-uri
    # primul va reprezenta valoarea din stanga a secventei cautate, iar cel de-al doilea valoarea din dreapta
    for i in range(len(l) - 1):
        sum_of_elements = l[i]  # se adauga valoarea de inceput in sum
        for j in range(i + 1, len(l)):
            sum_of_elements = sum_of_elements + l[j]
            # verificam daca secventa are suma cea mai mare si este de lungime maxima
            if sum_of_elements >= smax and dr - st <= j - i:
                smax = sum_of_elements
                st = i
                dr = j

    # introducem intr-o lista valorile de la rezultat
    if smax < l[x]:
        prop_11.append(l[x])
        prop_11.append(x)
        prop_11.append(x)
    else:
        prop_11.append(smax)
        prop_11.append(st)
        prop_11.append(dr)
    return prop_11


def ui_prop_11(l):
    if len(l) == 0:
        print("Introduceti elemente in lista!")
        return
    seq = sequence_prop_11(l)
    print(seq)


def is_prime(x):
    # algoritm care returneaza false daca un numar nu este prim si true daca un numar este prim
    if x < 2:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def sequence_prop_7(l):
    """
    functia care returneaza secventa de lungime maxima din lista a carei fiecare doua numere consecutive au
    diferenta un numar prim
    input: l - lista de intregi
    output: st - indexul din stanga al secventei, dr - indexul din dreapta al secventei
    """

    # lista trebuie sa aiba cel putin doua elemente pentru ca proprietatea sa se poata valida
    if len(l) < 2:
        return "Proprietatea nu se poate valida!"

    st = 0
    dr = 0
    ok = 0
    current_st = 0

    for i in range(len(l) - 1):
        # diferenta a doua numere consecutive
        if l[i + 1] > l[i]:
            dif = l[i + 1] - l[i]
        else:
            dif = l[i] - l[i + 1]

        if ok == 0:  # se incepe o noua secventa
            current_st = i
            if is_prime(dif) is True:
                ok = 1  # s-a inceput o secventa
                if (i + 1) - current_st > dr - st:
                    dr = i + 1
                    st = current_st
        else:  # se continua o secventa deja inceputa
            if is_prime(dif) is True:
                if (i + 1) - current_st > dr - st:
                    dr = i + 1
                    st = current_st
            else:
                ok = 0  # s-a sfarsit o secventa

    if st != 0 or dr != 0:
        prop_7 = [st, dr]
        return prop_7
    return "Nu exista o secventa cu aceasta proprietate!"


def ui_prop_7(l):
    if len(l) == 0:
        print("Introduceti elemente in lista!")
        return
    seq = sequence_prop_7(l)
    print(seq)


def test_prop_10():
    assert (sequence_prop_10([10]) == "Proprietatea nu se poate valida!")
    assert (sequence_prop_10([5, 9]) == "Proprietatea nu se poate valida!")
    assert (sequence_prop_10([3, 2, 1, 4, 3, 9]) == [1, 5])
    assert (sequence_prop_10([3, 5, 7]) == "Nu exista o secventa cu aceasta proprietate!")
    assert (sequence_prop_10([5, 8, 8]) == "Nu exista o secventa cu aceasta proprietate!")
    assert (sequence_prop_10([10, 8, 8]) == [0, 2])
    assert (sequence_prop_10([2, 6, -10, 9]) == [0, 3])


def test_prop_11():
    assert (sequence_prop_11([10]) == [10, 0, 0])
    assert (sequence_prop_11([-2, -5, 11, -3, -9]) == [11, 2, 2])
    assert (sequence_prop_11([9, -2, 4, -12, 3, 8]) == [11, 0, 2])


def test_prop_7():
    assert (sequence_prop_7([10]) == "Proprietatea nu se poate valida!")
    assert (sequence_prop_7([1, 2, 3]) == "Nu exista o secventa cu aceasta proprietate!")
    assert (sequence_prop_7([1, 2, 4]) == [1, 2])
    assert (sequence_prop_7([5, 3, 1, 9, 7]) == [0, 2])


def run_all_tests():
    test_prop_10()
    test_prop_11()
    test_prop_7()


# main
def main():
    my_list = []
    switcher = {
        "1": ui_add_list,
        "2": ui_prop_10,
        "3": ui_prop_11,
        "4": ui_prop_7
    }
    while True:
        meniu_optiuni()
        option = input("Alege optiunea: ")
        if option == "5":
            print("=============================================\n"
                  "Good Bye!\n"
                  "=============================================\n")
            return
        if option in switcher:
            switcher[option](my_list)
        else:
            print("Optiune invalida!")


# run the program
run_all_tests()
main()
