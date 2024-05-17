# The user types in a number of the month (from 1 to 12).
# Based on the typed in number, the program displays one of the following:
# Winter if the number is 1, 2 or 12 etc.
# If the list is out of range, display an error message

class OutOfBoundsError(Exception):
    def __init__(self, message="Číslo měsíce není v rozsahu 1-12"):
        self.message = message
        super().__init__(self.message)


try:
    month = int(input("Zadejte číslo měsíce"))

    if month not in range(1,13):
        raise OutOfBoundsError

    if month in range(3,6):
        print("Jaro")
    elif month in range(6,9):
        print("léto")
    elif month in range(9,12):
        print("Podzim")
    else:
        print("Zima")

except ValueError:
    print("Zadal jsi špatné číslo, zkuste to znovu.")

except OutOfBoundsError:
    print("Číslo měsíce není v rozsahu 1-12")