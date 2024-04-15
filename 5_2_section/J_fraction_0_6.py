from typing import Optional, Self


class Fraction:
    _chislitel, _znamenatel = None, None

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

        if self._chislitel < 0 and self._znamenatel < 0:
            self._chislitel, self._znamenatel = -self._chislitel, -self._znamenatel
        elif self._chislitel > 0 and self._znamenatel < 0:
            self._chislitel, self._znamenatel = -self._chislitel, -self._znamenatel

    def numerator(self, number: int = None) -> Optional[int]:
        if number is None:
            return self._chislitel

        self._chislitel = number
        self._reduce()

    def denominator(self, number: int = None) -> Optional[int]:
        if number is None:
            return self._znamenatel

        self._znamenatel = number
        self._reduce()

    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], int):
                self._chislitel, self._znamenatel = args[0], 1
            elif isinstance(args[0], str) and "/" not in args[0]:
                self._chislitel, self._znamenatel = int(args[0]), 1
            else:
                self._chislitel, self._znamenatel = int(args[0].split("/")[0]), int(args[0].split("/")[1])
        else:
            self._chislitel, self._znamenatel = args[0], args[1]

        self._reduce()

    def _to_common(self, other: Self) -> int:
        return self._znamenatel * other.denominator()

    def __sub__(self, other: Self) -> Self:
        if isinstance(other, int):
            other = Fraction(other, 1)
        common = self._to_common(other)

        return Fraction(self._chislitel * other.denominator()
                        - other.numerator() * self._znamenatel,
                        common)

    def __str__(self) -> str:
        return f"{self._chislitel}/{self._znamenatel}"

    def __neg__(self) -> Self:
        return Fraction(-self._chislitel, self._znamenatel)

    def __add__(self, other: Self):
        if isinstance(other, int):
            other = Fraction(other, 1)
        common = self._to_common(other)

        return Fraction(self._chislitel * other.denominator()
                        + other.numerator() * self._znamenatel,
                        common)

    def __iadd__(self, other: Self) -> Self:
        if isinstance(other, int):
            other = Fraction(other, 1)
        common = self._to_common(other)

        self._chislitel = (self._chislitel * other.denominator()
                           + other.numerator() * self._znamenatel)
        self._znamenatel = common

        self._reduce()

        return self

    def __isub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        common = self._to_common(other)

        self._chislitel = (self._chislitel * other.denominator()
                           - other.numerator() * self._znamenatel)
        self._znamenatel = common

        self._reduce()

        return self

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction(self._chislitel * other.numerator(), self._znamenatel * other.denominator())

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction(self._chislitel * other.denominator(), self._znamenatel * other.numerator())

    def __imul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        self._chislitel *= other.numerator()
        self._znamenatel *= other.denominator()
        self._reduce()
        return self

    def __itruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        self._chislitel *= other.denominator()
        self._znamenatel *= other.numerator()
        self._reduce()
        return self

    def __repr__(self) -> str:
        return f"Fraction({self._chislitel}, {self._znamenatel})"

    def reverse(self):
        return Fraction(self._znamenatel, self._chislitel)

    def __le__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self._chislitel * other.denominator() <= other.numerator() * self._znamenatel

    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self._chislitel * other.denominator() < other.numerator() * self._znamenatel

    def __gt__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self._chislitel * other.denominator() > other.numerator() * self._znamenatel

    def __ge__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self._chislitel * other.denominator() >= other.numerator() * self._znamenatel

    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self._chislitel * other.denominator() == other.numerator() * self._znamenatel

    def __ne__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self._chislitel * other.denominator() != other.numerator() * self._znamenatel
