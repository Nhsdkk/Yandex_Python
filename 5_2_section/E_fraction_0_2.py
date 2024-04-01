from typing import Optional, Self


class Fraction:
    _chislitel, _znamenatel = None, None
    _neg = False

    @staticmethod
    def _gcd(number1: int, number2: int) -> int:
        while number1 != 0 and number2 != 0:
            if number1 > number2:
                number1 %= number2
            else:
                number2 %= number1

        if number1 == 0:
            return number2
        else:
            return number1

    def _reduce(self):
        gcd_value = self._gcd(abs(self._chislitel), abs(self._znamenatel))

        self._chislitel, self._znamenatel = self._chislitel // gcd_value, self._znamenatel // gcd_value

    def numerator(self, number: int = None) -> Optional[int]:
        if number is None:
            return self._chislitel

        self._chislitel = abs(number)
        if number < 0:
            self._neg = not self._neg
        self._reduce()

    def denominator(self, number: int = None) -> Optional[int]:
        if number is None:
            return self._znamenatel

        self._znamenatel = abs(number)
        if number < 0:
            self._neg = not self._neg
        self._reduce()

    def __init__(self, *args):
        if len(args) == 1:
            self._chislitel, self._znamenatel = int(args[0].split("/")[0]), int(args[0].split("/")[1])
        else:
            self._chislitel, self._znamenatel = args[0], args[1]

        self._neg = self._chislitel * self._znamenatel < 0

        self._chislitel, self._znamenatel = abs(self._chislitel), abs(self._znamenatel)

        self._reduce()

    def _to_common(self, other: Self) -> int:
        return self._znamenatel * other.denominator()

    def __str__(self) -> str:
        if self._neg:
            return f"-{abs(self._chislitel)}/{abs(self._znamenatel)}"
        else:
            return f"{abs(self._chislitel)}/{abs(self._znamenatel)}"

    def __repr__(self) -> str:
        if self._neg:
            return f"Fraction('-{abs(self._chislitel)}/{abs(self._znamenatel)}')"
        else:
            return f"Fraction('{abs(self._chislitel)}/{abs(self._znamenatel)}')"

    def __neg__(self) -> Self:
        new_fraction = Fraction(self._chislitel, self._znamenatel)
        new_fraction._neg = not self._neg
        return new_fraction


a = Fraction("-1/-3")
b = Fraction(-2, -6)
# a.numerator(-2)

print(a, b, -a, -b , -(-a), -(-b))