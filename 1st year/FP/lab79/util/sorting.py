"""
@@@ Vintila Radu @@@
"""


def selection_sort(array, key, cmp):
    """
    Sortarea prin selectie. La fiecare pas se cauta cel mai mic element din lista.
    Daca este diferit de cel de pe pozitia curenta (i) de parcurgere, atunci se face interschimbarea.
    Lista astfel obtinuta este sortata corect pana la pozitia i.
    Se continua procedeul pana cand i = lenght(array)
    :param array: lista de entitati ce se doreste a fi sortata
    :param key: functie lambda; specifica criteriul dupa care se face sortarea
    :param cmp: functie (criteriu de comparare)
    :return: lista sortata v, copie a primei liste
    """
    # facem o copie a listei originale
    v = array[:]
    # parcurgem lista pana la ultima pozitie
    for i in range(len(v)):
        minimum = i
        for j in range(i + 1, len(v)):
            # Preia cea mai mica valoare
            if cmp(key(v[j]), key(v[minimum])) == 1:
                minimum = j
        # daca exista o valoare mai mica dupa cea de pe pozitia i
        # se face interschimbarea
        v[minimum], v[i] = v[i], v[minimum]

    return v


def minIndex(v, key, cmp, i, j):
    if i == j:
        return i
    k = minIndex(v, key, cmp, i + 1, j)
    return i if cmp(key(v[i]), key(v[k])) == 1 else k


def selection_sort_rec(array, key, cmp, index=0):
    """
    Sortarea prin selectie recursiva.
    :param array: lista de entitati
    :param key: functie lambda (criteriul de sortare)
    :param cmp: functie (criteriu de comparare)
    :param index: contorul de parcurgere al sirului
    :return: v - noua lista sortata dupa criteriul dat
    """
    v = array[:]
    # daca am ajuns la finalul sirului, returnam lista sortata
    if index == len(v):
        return v
    # avand deja contorul ca parametru, ne ramane de gasit valoarea minima
    k = minIndex(v, key, cmp, index, len(v) - 1)
    # daca nu sunt identice, se face interschimbare
    if k != index:
        v[k], v[index] = v[index], v[k]
    # se continua cu urmatorul element din sir
    # fiecare pana la pozitia index sunt acum sortate corect
    return selection_sort_rec(v, key, cmp, index + 1)


def shake_sort(array, key, cmp):
    """
    In cazul shake sort-ului vor fi facute doua parcurgeri la fiecare pas
    Prima parcurgere este de la stanga la dreapta. La fel ca si in cazul bubble sort-ului,
    vor fi comparate elementele de pe pozitii consecutive, daca cel din stanga este mai mare,
    se face interschimbarea. In acest mod, elementul cel mai mare din sir ajunge pe ultima pozitie
    A doua parcurgere este imediata si se face de la dreapta la stanga. Dupa finalizarea primei parcurgeri
    se incepe cea de-a doua in sens inserv, astfel incat la final se pune pe prima pozitie cel mai mic element.
    Se continua procedeul pana cand lista este sortata.

    Complexitate - spatiu de memorie:
    complexitate memorie adițională este: Θ(1) (este un algoritm de sortare in-place)

    Complexitate - timp de executie:
    Caz favorabil: Θ(n) - Este parcursa lista o data pentru a se putea observa ca este sortata
    Caz defavorabil si cel mediu: Θ(n*n) - Cu fiecare parcurgere este pus la pozitia corecta de sortare un element.
    Este astfel nevoie de n parcurgeri a listei pentru a pune toate cele n elemente pe poiztiile bune.
    (n-1)+(n-2)+...+3+2+1 = sum (n(n-1)/2) => O(n*n)

    :param array: lista de entitati
    :param key: functie lambda (criteriul de sortare)
    :param cmp: functie (criteriu de comparare)
    :return: noua lista sortata
    """
    # copie a listei originale
    v = array[:]
    # contor de verificare a interschimbarii a doua elemente
    # ceea ce ne arata daca lista este inca sortata sau nu
    swapped = True
    left = 0
    right = len(v) - 1
    while swapped:
        swapped = False
        for i in range(left, right):
            if cmp(key(v[i]), key(v[i + 1])) == -1:
                v[i], v[i + 1] = v[i + 1], v[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        # s-a gasit elementul maxim al acestei parcurgeri si se scade contorul din dreapta cu o pozitie
        right -= 1
        for i in range(right - 1, left - 1, -1):
            if cmp(key(v[i]), key(v[i + 1])) == -1:
                v[i], v[i + 1] = v[i + 1], v[i]
                swapped = True
        # s-a gasit elementul minim al acestei parcurgeri si se creste contorul din stanga cu o pozitie
        left += 1

    return v


def sorted_custom(array, method, *, key=lambda item: item, reverse=False,
                  cmp=lambda x, y: 1 if x < y else 0 if x == y else -1):
    """
    Noua functie generica pentru sortare
    :param array: lista de entitati
    :param method: string (metoda de sortare)
    :param key: functie lambda (criteriul de sortare)
    :param reverse: bool (true - se sorteaza descrescator, false - se sorteaza crescator)
    :param cmp: functie lambda (criteriu de comparare)
    :return: lista sortata
    """
    sort = {
        "selection": selection_sort,
        "selection_rec": selection_sort_rec,
        "shake": shake_sort
    }
    result = sort[method](array, key, cmp)
    if reverse is True:
        result.reverse()
    return result
