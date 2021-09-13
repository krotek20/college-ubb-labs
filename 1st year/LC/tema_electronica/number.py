# Autor : Vintila Radu - Florian


class Number:
    """
    Clasa abstracta pentru instanta de numar
    """

    def __init__(self, digits, base):
        """
        Constructor Number
        :param digits: list of number's digits (list)
        :param base: number's base (int)
        """
        self.__digits = digits
        self.__base = base

    # setters and getters
    def get_digits(self):
        return self.__digits

    def get_base(self):
        return self.__base

    def set_digits(self, digits):
        self.__digits = digits
