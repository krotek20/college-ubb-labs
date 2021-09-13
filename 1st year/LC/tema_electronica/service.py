# Autor : Vintila Radu - Florian

from random import randint
from number import Number
import math


class service_exception(Exception):
    pass


class Service:
    def __init__(self, validator):
        """
        Constructor clasa service
        :param validator: validator (validare)
        """
        # instanta de validator
        self.__validator = validator
        # matrice de conversie rapida
        self.__quick_vals = [[0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111],
                             [0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
        # lista de rezultat (lista cifrelor numarului rezultat)
        self.rez = [None] * 51

    def verify_numbers(self, n1, b1, n2, b2):
        """
        Function which verifies inserted numbers and transform them into a Number object
        :param n1: first number (int)
        :param b1: first number's base (int)
        :param n2: second number (int)
        :param b2: second number's base (int)
        :return: a Number compose of:
                - list of digits
                - base
                (type Number)
        """
        if type(n1) is int:
            # lista cifrelor unui numar
            digits1 = [int(x) for x in str(n1)]
            digits2 = [int(x) for x in str(n2)]
        else:
            # lista cifrelor unui numar fara valori de None
            digits1 = [int(x) for x in n1 if x is not None]
            digits2 = [int(x) for x in n2 if x is not None]
        first_number = Number(digits1, b1)  # se creeaza primul obiect
        self.__validator.validate(first_number)  # se verifica corectitudinea primului obiect
        second_number = Number(digits2, b2)
        self.__validator.validate(second_number)
        return first_number, second_number

    def verify_base(self, number, base):
        """
        Function which verifies the base of a number
        This function is made to convert a number from its base to base for an algebric operation
        :param number: instance of a number (Number)
        :param base: final base (int)
        :return: a new Number if number's base isn't the same as final base
                    the new Number is the conversion of number in final base;
                 the old number (Number)
        """
        if number.get_base() != base:  # daca bazele lor sunt diferite se face conversia
            # se formeaza numarul nr cu cifrele din number
            digits = [str(x) for x in number.get_digits()]
            nr = int("".join(digits))

            new_num, msg = self.convert(nr, number.get_base(), base)  # se face conversia la baza base
            new_num.set_digits([i for i in new_num.get_digits() if i is not None])
            return new_num  # se returneaza noul numar creat
        return number  # daca bazele sunt egale, se returneaza acelasi numar introdus initial

    def convert(self, n, b, bf):
        """
        Conversion function. It chooses the right conversion methode to be used.
        :param n: number (int)
        :param b: base (int)
        :param bf: final desire base (int)
        :return: a Number object (list of digits + base) and a message of the conversion methode used.
        """
        digits = [int(x) for x in str(n)]  # lista de cifre a numarului n
        number = Number(digits, b)  # obiectul Number cu lista de cifre si baza
        self.__validator.validate(number)  # se verifica daca e corect format
        quick_conv = [2, 4, 8, 16]
        if number.get_base() in quick_conv and bf in quick_conv:  # aplicare conversie rapida
            if number.get_base() == 2:
                # din baza 2 in bazele 4, 8 si 16
                return self.quick_convert_from_2(number, bf, quick_conv)
            elif bf == 2:
                # din bazele 4, 8, 16 in baza 2
                return self.quick_convert_to_2(number, number.get_base(), quick_conv)
            else:
                # alta conversie intre bazele 2, 4, 8, 16 (exemplu: din 4 la 16)
                base2number, msg = self.quick_convert_to_2(number, number.get_base(), quick_conv)
                base2number.set_digits([i for i in base2number.get_digits() if i is not None])
                return self.quick_convert_from_2(base2number, bf, quick_conv)
        else:
            random = randint(1, 2)
            # se alege aleatoriu conversia urmatoare
            # 1 - conversie prin substitutie sau prin impartiri repetate
            # 2 - conversie printr-o baza intermediara (baza 10)
            if random == 1:
                if number.get_base() < bf:  # conversie prin substitutie
                    return self.convert_lower_to_higher(number, bf)
                else:  # conversie prin impartiri repetate
                    return self.convert_higher_to_lower(number, bf)
            else:  # conversie printr-o baza intermediara (baza 10)
                base10number = self.convert_to_10(number, number.get_base())
                return self.convert_from_10(base10number, bf)

    def quick_convert_from_2(self, number, bf, quick_conv):
        """
        Function to quickly convert a number from base 2 to base 4, 8 or 16
        :param number: number to be converted (Number)
        :param bf: final base (int)
        :param quick_conv: list of values [2, 4, 8, 16]
        :return: a Number with the result list of digits and the final base
        """
        self.rez = [None] * 51
        poz = quick_conv.index(bf) + 1  # poz = log_2(bf)
        size_rez = len(number.get_digits()) // poz + (len(number.get_digits()) % poz != 0)
        start = size_rez - 1
        for i in range(len(number.get_digits()) - 1, -1, -poz):  # se parcurge invers din poz in poz
            power = pas = 1
            nr = 0
            while i - pas + 1 >= 0 and pas <= poz:  # se formeaza numarul in baza 2
                nr += power * number.get_digits()[i - pas + 1]
                power *= 10
                pas += 1
            for j in range(15):
                # se cauta numarul nr in matricea conversiei rapide si se scrie numarul corespunzator in baza bf
                if nr == self.__quick_vals[0][j]:
                    self.rez[start] = self.__quick_vals[poz - 1][j]
                    start -= 1
                    break
        return Number(self.rez, bf), "---Conversie rapida---"

    def quick_convert_to_2(self, number, b, quick_conv):
        """
        Function to quickly convert a number from base 4, 8 or 16 to base 2
        :param number: number to be converted (Number)
        :param b: final base (int)
        :param quick_conv: list of values [2, 4, 8, 16]
        :return: a Number with the result list of digits and the final base
        """
        self.rez = [None] * 51
        poz = quick_conv.index(b) + 1
        size_rez = len(number.get_digits()) * poz
        start = size_rez - 1
        for i in range(len(number.get_digits()) - 1, -1, -1):
            # se iau invers cifrele din numar si se cauta corespondentul lor in baza 2
            nr = self.__quick_vals[0][number.get_digits()[i]]
            for j in range(poz):
                # se completeaza lista de cifre cu fiecare cifra din numarul in baza 2
                self.rez[start] = nr % 10
                start -= 1
                nr //= 10
        return Number(self.rez, 2), "---Conversie rapida---"

    def convert_to_10(self, number, b):
        """
        Function to convert a number from base b to base 10
        :param number: Number object (Number)
        :param b: base (int)
        :return: nr (int) - the result in base 10
        """
        self.rez = [None] * 51
        nr = number.get_digits()[0]
        for i in range(1, len(number.get_digits())):
            nr = nr * b + number.get_digits()[i]
        return nr

    def convert_from_10(self, number, bf):
        """
        Function to convert a number from base 10 to base bf
        :param number: number in base 10 (int)
        :param bf: base (int)
        :return: Number object and the message of the used conversion methode
        """
        self.rez = [None] * 51
        while number != 0:
            # se formeaza o lista noua formata din cea veche si restul impartirii numarului la baza
            # acest rest este introdus pe prima pozitie in lista (practic este o stiva)
            self.rez = [number % bf] + self.rez[0:]
            number //= bf
        return Number(self.rez, bf), "---Conversie cu baza intermediara (baza 10)---"

    def convert_lower_to_higher(self, number, bf):
        """
        Function to convert a number from a lower base to a higher base
        This is substitution methode of conversion
        :param number: Number object (Number)
        :param bf: final base (int)
        :return: Number object (Number) - the instance of the new number in base bf
        """
        # a_(n)a_(n-1)...a_0 = a_(n)*p^(n)+a_(n-1)*p^(n-1)+...+a_(1)*p
        #    in base p                 in base bf
        # p is the base of number (number.get_base())
        self.rez = [None] * 51
        self.rez[0] = number.get_digits()[0]
        for i in range(1, len(number.get_digits())):
            # nr - lista de o cifra ca memoreaza baza curenta pentru inmultire si cifra de pe pozitia i pentru adunare
            nr = [None] * 2
            nr[0] = number.get_base()
            aux = self.rez
            new_num = self.multiply(aux, bf, nr, bf, bf)
            self.rez = new_num.get_digits()
            nr[0] = number.get_digits()[i]
            aux = self.rez
            self.add(aux, bf, nr, bf, bf)
        return Number(self.rez, bf), "---Conversie prin substitutie---"

    def convert_higher_to_lower(self, number, bf):
        """
        Function to convert a number from a higher base to a lower base
        This is conversion with repeated division
        :param number: Number object (Number)
        :param bf: final base (int)
        :return: Number object (Number) - the instance of the new number in base bf
        """
        # nr / bf = c0 rest r0
        # c0 / bf = c1 rest r1
        # ... ... ... ... ...
        # cn / bf = 0 rest rn
        # Numarul rezultat este format din contactenarea resturilor in ordine inversa (r_(n)r_(n-1)...r_(1)r_(0))
        # any division is made in base p - the base of the initial number (number.get_base())
        self.rez = [None] * 51
        local_rez = [None] * 51
        start = int(math.log(number.get_base(), bf)) * len(number.get_digits())
        base = number.get_base()
        while True:
            nr = [None] * 2
            nr[0] = bf
            new_num, rest = self.divide(number.get_digits(), base, nr, base, base)
            self.rez = new_num.get_digits()
            local_rez[start] = rest
            start -= 1
            number.set_digits(self.rez)
            if len(set(self.rez)) <= 1:
                break
        return Number(local_rez, bf), "---Conversie prin impartiri repetate---"

    def add(self, n1, b1, n2, b2, bf):
        """
        Add two numbers with different bases in a final base
        :param n1: first number (int)
        :param b1: first number's base (int)
        :param n2: second number (int)
        :param b2: second number's base (int)
        :param bf: final base (int)
        :return: result (Number)
        Este folosit principiul de calcul prezentat in Cursul 1
        """
        first_number, second_number = self.verify_numbers(n1, b1, n2, b2)
        first_number = self.verify_base(first_number, bf)  # converteste primul numarul in baza bf
        second_number = self.verify_base(second_number, bf)  # converteste al doilea numar in baza bf
        self.rez = [None] * 51
        transport = 0
        lenght_first = len(first_number.get_digits())
        lenght_second = len(second_number.get_digits())
        start = max(lenght_first, lenght_second)
        lenght_first -= 1
        lenght_second -= 1
        while start >= 0:
            self.rez[start] = transport
            if lenght_first >= 0:
                self.rez[start] += first_number.get_digits()[lenght_first]
                lenght_first -= 1
            if lenght_second >= 0:
                self.rez[start] += second_number.get_digits()[lenght_second]
                lenght_second -= 1
            transport = self.rez[start] // bf
            self.rez[start] = self.rez[start] % bf
            start -= 1
        contor = 0
        while self.rez[contor] == 0:
            self.rez[contor] = None
            contor += 1
        return Number(self.rez, bf)

    def difference(self, n1, b1, n2, b2, bf):
        """
        Difference of two numbers with different bases in a final base
        :param n1: first number (int)
        :param b1: first number's base (int)
        :param n2: second number (int)
        :param b2: second number's base (int)
        :param bf: final base (int)
        :return: result (Number)
        Este folosit principiul de calcul prezentat in Cursul 1
        """
        if n1 < n2:  # in cazul rezultatelor negative (scaderea unui numar mai mare dintr-un numar mai mic)
            n1, n2 = n2, n1
            b1, b2 = b2, b1
            print("-", end='')
        first_number, second_number = self.verify_numbers(n1, b1, n2, b2)
        first_number = self.verify_base(first_number, bf)  # converteste primul numarul in baza bf
        second_number = self.verify_base(second_number, bf)  # converteste al doilea numar in baza bf
        self.rez = [None] * 51
        transport = 0
        start = len(first_number.get_digits()) - 1
        lenght_first = len(first_number.get_digits())
        lenght_second = len(second_number.get_digits())
        lenght_first -= 1
        lenght_second -= 1
        while start >= 0:
            self.rez[start] = first_number.get_digits()[lenght_first] - transport
            lenght_first -= 1
            if lenght_second >= 0:
                self.rez[start] -= second_number.get_digits()[lenght_second]
                lenght_second -= 1
            if self.rez[start] < 0:
                self.rez[start] += bf
                transport = 1
            else:
                transport = 0
            start -= 1
        contor = 0
        while self.rez[contor] == 0:
            self.rez[contor] = None
            contor += 1
        return Number(self.rez, bf)

    def multiply(self, n1, b1, n2, b2, bf):
        """
        Multiply two numbers with different bases in a final base
        :param n1: first number (int)
        :param b1: first number's base (int)
        :param n2: second number (int) - a single digit
        :param b2: second number's base (int)
        :param bf: final base (int)
        :return: result (Number)
        :raise: if the second number is > 10 raise error "A number can be multiplied with only one digit!"
        Este folosit principiul de calcul prezentat in Cursul 1
        """
        first_number, second_number = self.verify_numbers(n1, b1, n2, b2)
        first_number = self.verify_base(first_number, bf)  # converteste primul numarul in baza bf
        second_number = self.verify_base(second_number, bf)  # converteste al doilea numar in baza bf
        if len(second_number.get_digits()) > 1:
            raise service_exception("A number can be multiplied with only one digit!")
        self.rez = [None] * 51
        lenght = len(first_number.get_digits())
        start = lenght + 1
        transport = 0
        start -= 1
        lenght -= 1
        while start >= 0:
            self.rez[start] = transport
            if lenght >= 0:
                self.rez[start] += first_number.get_digits()[lenght] * second_number.get_digits()[0]
                lenght -= 1
            transport = self.rez[start] // bf
            self.rez[start] = self.rez[start] % bf
            start -= 1
        contor = 0
        while self.rez[contor] == 0:
            self.rez[contor] = None
            contor += 1
        return Number(self.rez, bf)

    def divide(self, n1, b1, n2, b2, bf):
        """
        Divide two numbers with different bases in a final base
        :param n1: first number (int)
        :param b1: first number's base (int)
        :param n2: second number (int) - a single digit
        :param b2: second number's base (int)
        :param bf: final base (int)
        :return: result (Number)
        :raises: if the second number is > 10 raise error "A number can be divided with only one digit!"
                 if the second number is 0 raise error "Divided by zero!"
        Este folosit principiul de calcul prezentat in Cursul 1
        """
        first_number, second_number = self.verify_numbers(n1, b1, n2, b2)
        first_number = self.verify_base(first_number, bf)  # converteste primul numarul in baza bf
        second_number = self.verify_base(second_number, bf)  # converteste al doilea numar in baza bf
        if len(second_number.get_digits()) > 1:
            raise service_exception("A number can be divided with only one digit!")
        if second_number.get_digits()[0] == 0:
            raise service_exception("Divided by zero!")
        self.rez = [None] * 51
        transport = 0
        for i in range(len(first_number.get_digits())):
            self.rez[i] = (transport * bf + first_number.get_digits()[i]) // second_number.get_digits()[0]
            transport = (transport * bf + first_number.get_digits()[i]) % second_number.get_digits()[0]
        contor = 0
        while self.rez[contor] == 0:
            self.rez[contor] = None
            contor += 1
        return Number(self.rez, bf), transport
