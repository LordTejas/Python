# python3

import re


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
        return isMatch(card_pattern, number)

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


if __name__ == '__main__':
    pass
