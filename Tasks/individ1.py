#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Pair (пара чисел); определить метод перемножения полей и операцию
сложения пар (a,b) + (c,d) = (a + b, c + d) . Определить производный класс Long с
полями: старшая часть числа и младшая часть числа. Определить методы умножения
и вычитания.
"""


class Pair:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def display(self):
        print(self.first, self.second)

    def multiplication(self, term):
        if isinstance(term, Pair):
            return Pair(self.first * self.second, term.first * term.second)

    def addition(self, term):
        if isinstance(term, Pair):
            return Pair(self.first + self.second, term.first + term.second)


class Long(Pair):

    def multiplication(self, term):
        if isinstance(term, Long):
            return Long(self.first * term.first - self.second * term.second, self.first * term.second + self.second *
                        term.first)

    def subtraction(self, term):
        if isinstance(term, Long):
            return Pair(self.first - self.second, term.first - term.second)


if __name__ == '__main__':
    num1 = Pair(2322014567, 8325124567)
    num2 = Pair(1012443456, 1502545456)
    num1.multiplication(num2).display()
    num1.addition(num2).display()
    long1 = Long(23, 54)
    long2 = Long(10, 78)
    long1.multiplication(long2).display()
    long1.subtraction(long2).display()
