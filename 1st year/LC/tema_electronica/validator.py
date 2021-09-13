# Autor : Vintila Radu - Florian


class number_exception(Exception):
    pass


class validare:
    # class to validate a number (check its atributes)
    @staticmethod
    def validate(number):
        erori = []
        if not number.get_digits():
            erori.append("Please insert a number!")
        if not number.get_base():
            erori.append("Please insert a base!")
        if number.get_base() < 2 or number.get_base() > 16:
            erori.append("Base needs to be an integer between 2 and 16!")
        for digit in number.get_digits():
            if number.get_base() < digit:
                erori.append("This number can not be written in this base!")
                break

        if len(erori) > 0:
            raise number_exception(erori)
