# python3

import re
import random


cards = dict()  # Our bank's database for accounts


class Card:

    def __init__(self, card_number: str, secret_pin: str):
        if self.isValidNumber(card_number) and self.isValidPin(secret_pin):
            self._card_number = card_number
            self._balance = 0
            self._secret_pin = secret_pin

    def setPin(self, secret_pin: str):
        if self.isValidPin(secret_pin):
            self._secret_pin = secret_pin

    def checkPin(self, card_pin: str) -> bool:
        # Checks pin matches with the current instances pin
        return self._secret_pin == card_pin

    @staticmethod
    def isValidNumber(number: str) -> bool:
        card_pattern = "40{5}[0-9]{10}"  # current pattern used for card validation
        if len(number) == 16 and isMatch(card_pattern, number):
            if number[-1] == getCheckSum("400000", number[6:15]):
                return True
        return False

    @staticmethod
    def isValidPin(pin: str) -> bool:
        pin_pattern = "[0-9]{4}"  # checks pin is in range 0000 - 9999
        return isMatch(pin_pattern, pin)

    def getBalance(self) -> float:
        return self._balance

    def __str__(self):
        try:
            return f"card number: {self._card_number}\nbalance: {self._balance}"
        except AttributeError:
            return "Card is not initialized properly <Card Number doesn't exists>"


def isMatch(pattern: str, string: str) -> bool:
    # checks if given string matches regex pattern completely
    is_match = re.match(pattern, string)

    if is_match is None: return False  # if not a single character matches the pattern

    chars_matched = is_match.span()[1]
    if chars_matched != len(string): return False  # if all character doesn't match pattern

    return True


def createCard():
    """Creates a card card for user and adds to database"""

    prefix = "400000"
    accountIdentifier = generateSequence(9)

    card_number = "400000" + accountIdentifier
    card_number += getCheckSum(prefix, accountIdentifier)
    while card_number in cards:
        accountIdentifier = generateSequence(9)
        card_number = "400000" + accountIdentifier
        card_number += getCheckSum(prefix, accountIdentifier)

    # Generating PIN for user
    card_pin = generateSequence(4)
    cards[card_number] = Card(card_number, card_pin)

    print("\nYour card has been created")
    print(f"Your card number:\n{card_number}\nYour card PIN:\n{card_pin}")


def getCheckSum(prefix: str, account_identifier: str) -> str:
    card_number = list(map(int, prefix + account_identifier))
    # print(card_number)

    # implementing Luhn Algorithm to check sum
    for i in range(len(card_number)):
        if (i + 1) % 2:
            card_number[i] *= 2
            if card_number[i] > 9:
                card_number[i] -= 9

    # print(card_number)
    sum_of_digits = sum(card_number)
    # print(sum_of_digits)
    check_sum_digit = 10 - sum_of_digits % 10
    if check_sum_digit == 10: check_sum_digit = 0
    return str(check_sum_digit)


def generateSequence(n: int) -> str:
    """
    Geneates sequence of n digits [0 - 9]
    :param n:
    :return: str type of sequence number
    """
    res = ""
    for i in range(n):
        res += str(random.randint(0, 9))
    return res


def loginAccount() -> bool:
    print("\nYour card number:")
    card_number = input()
    print("Your card PIN:")
    card_pin = input()
    choice = None
    if card_number in cards.keys():
        if cards.get(card_number).checkPin(card_pin):
            print("\nYou have successfully logged in!")
            while True:
                print("\n1. Balance\n2. Log out\n0. Exit")
                choice = input()

                if choice == "1":
                    print(f"\nBalance: {cards.get(card_number).getBalance()}")

                elif choice == "2":
                    print("\nYou have successfully logged out!")
                    return False

                elif choice == "0":
                    return True
        else:
            print("\nWrong card number or PIN!")
            return False
    else:
        print("\nWrong card number or PIN!")
        return False


def Main():

    while True:
        print("1. Create an account\n"
              + "2. Log into account\n"
              + "0. Exit")

        choice = input()
        if choice == '1':
            createCard()
            print()

        elif choice == '2':
            if loginAccount(): break
            print()

        elif choice == "0":
            break


if __name__ == '__main__':
    Main()
