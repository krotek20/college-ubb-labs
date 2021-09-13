# Autor : Vintila Radu - Florian

from validator import number_exception
from service import service_exception


class Meniu:
    def __init__(self, srv):
        """
        Meniu constructor
        :param srv: service instance
        """
        self.__srv = srv
        # list of commands
        self.cmds = {
            "convert": self.__convert,
            "add": self.__add,
            "diff": self.__difference,
            "mult": self.__multiply,
            "div": self.__divide
        }

    @staticmethod
    def print_meniu():
        print("""
convert - Convert a number in a different base
add - Add two numbers
diff - Difference between two numbers
mult - Multiply two numbers
div - Divide two numbers
exit - Exit the application
        """)

    @staticmethod
    def read_params():
        first_number = int(input("Insert first number: "))
        base_first = int(input("Insert first number's base (from 2 to 16): "))
        second_number = int(input("Insert second number: "))
        base_second = int(input("Insert second number's base (from 2 to 16): "))
        base_final = int(input("Insert desire result base (from 2 to 16): "))
        return first_number, base_first, second_number, base_second, base_final

    @staticmethod
    def print_number(number):
        """
        Print a number in its base
        (A, B, C, D, E, F) = (10, 11, 12, 13, 14, 15)
        :param number: Number object (Number)
        """
        print("Rezultat: ", end='')
        for i in range(len(number.get_digits())):
            if number.get_digits()[i] is not None:
                if number.get_digits()[i] < 10:
                    print(str(number.get_digits()[i]), end='')
                else:
                    print(chr(ord('A')+number.get_digits()[i]-10), end='')

    @staticmethod
    def print_base(base):
        # print a number's base
        print("\nBaza numarului: " + str(base))

    def __convert(self):
        number = int(input("Insert number: "))
        base = int(input("Insert base (from 2 to 16): "))
        base_final = int(input("Convert into (base): "))
        number, msg = self.__srv.convert(number, base, base_final)
        print(msg)
        self.print_number(number)
        self.print_base(number.get_base())

    def __add(self):
        n1, b1, n2, b2, bf = self.read_params()
        number = self.__srv.add(n1, b1, n2, b2, bf)
        self.print_number(number)
        self.print_base(number.get_base())

    def __difference(self):
        n1, b1, n2, b2, bf = self.read_params()
        number = self.__srv.difference(n1, b1, n2, b2, bf)
        self.print_number(number)
        self.print_base(number.get_base())

    def __multiply(self):
        n1, b1, n2, b2, bf = self.read_params()
        number = self.__srv.multiply(n1, b1, n2, b2, bf)
        self.print_number(number)
        self.print_base(number.get_base())

    def __divide(self):
        n1, b1, n2, b2, bf = self.read_params()
        number, rest = self.__srv.divide(n1, b1, n2, b2, bf)
        self.print_number(number)
        print(" rest " + str(rest))
        self.print_base(number.get_base())

    def afisare(self):
        print("--- M e n i u ---")
        print("\nCommand  |  Description", end='')
        while True:
            self.print_meniu()

            cmd = input("Type command: ")

            try:
                if cmd == "exit":
                    break
                elif cmd in self.cmds:
                    self.cmds[cmd]()
                else:
                    print("Invalid command!")
            # catch UI, service and validator exceptions
            except ValueError as ve:
                print("UI error\n" + str(ve))
            except number_exception as ne:
                print(str(ne))
            except service_exception as se:
                print(str(se))
