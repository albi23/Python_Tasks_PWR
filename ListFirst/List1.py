from __future__ import division

import collections
import math
import operator
import random
import re
from filecmp import cmp
from typing import List, Dict
from typing import TypeVar

import scipy.special
from pyparsing import (Literal, CaselessLiteral, Word, Combine, Group, Optional,
                       ZeroOrMore, Forward, nums, alphas, oneOf)

T = TypeVar('T')


def pascal_triangle(n: int) -> None:
    if n <= 0:
        return

    max_size_of_number: int = len(str((int(scipy.special.binom(n, int(n / 2))))))
    for line in range(1, n + 1):
        x = int(max_size_of_number * ((n / 2) - (line - 1) / 2))
        pattern_of_line: str = '{:^' + str(x) + '}'
        print(pattern_of_line.format(' '), end='')
        c: int = 1
        for j in range(1, line + 1):
            print(c, end=' ')
            c = int(c * (line - j) / j)
        print()
    pass


def primes(n: int) -> List[int]:
    primes_bool_array = [True] * (n + 1)
    primes_bool_array[0] = primes_bool_array[1] = False

    limit: int = int(math.sqrt(n))

    for number in range(0, limit + 1):
        if primes_bool_array[number]:
            i: int = number * number
            while i <= n:
                primes_bool_array[i] = False
                i += number

    primes_array: List[int] = []
    for i in range(0, n + 1):
        if primes_bool_array[i]:
            primes_array.append(i)

    return primes_array


pass

print(primes(100))


def make_without_repeats(generic_list: List[T]) -> List[T]:
    if len(generic_list) == 0:
        return generic_list
    else:
        array_set: List[T] = []
        if isinstance(generic_list[0], list):
            sorted(generic_list, key=lambda l: l[0])

        else:
            generic_list.sort()

        previous: T = None
        for i in range(0, len(generic_list)):
            if generic_list[i] != previous:
                array_set.append(generic_list[i])
            previous = generic_list[i]

    return array_set
    pass


print(make_without_repeats([1, 2, 4, 4, 4, 6, 8, 4, 2, 55, -1, -1, 6, 8, 0, -1, -2]))
print(make_without_repeats(['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'h', 'h', 'w', 'f']))
print(make_without_repeats(
    [['a', 'b', 'f'], ['a', 'b', 'f'], ['b', 'b', 'b'], ['b', 'b', 'e'], ['a', 'b', 'f'], ['c', 'c', 'f']]))


def prime_factors(n: int) -> Dict[int, int]:
    prime: int = 2
    factors_map = {}
    res = collections.ChainMap(factors_map)
    while n >= prime * prime:
        if n % prime == 0:
            if res.get(prime) is not None:
                factors_map[prime] += 1
            else:
                factors_map[prime] = 1
            n = int(n / prime)
        else:
            prime += 1

    if res.get(n) is not None:
        factors_map[n] += 1
    else:
        factors_map[n] = 1
    return factors_map
    pass


print(prime_factors(10616832000))


def fraczero(n: int) -> int:
    if n >= 0 or n <= 1000:
        result_array: List = re.findall("0+$", str(math.factorial(n)))
        if len(result_array) > 0:
            return len(result_array[0])
    return 0


print(fraczero(10000))


def random_calculation():
    random_arr: List = []
    even: int = 0
    random_sum: int = 0
    first_max: int = 0
    second_max = 0
    first_min: int = 100
    second_min = 100
    for index in range(0, 20):
        next_random: int = random.randrange(1, 100)
        random_sum += next_random

        if next_random > first_max:
            second_max = first_max
            first_max = next_random
        if next_random < first_min:
            second_min = first_min
            first_min = next_random

        if next_random % 2 == 0: even += 1
        random_arr.append(next_random)

    print("List: ", random_arr)
    print("Max : ", first_max, "  second first_max ", second_max)
    print("Min : ", first_min, "  second first_min ", second_min)
    print("Even count : ", even, "  avg of numbers  ", random_sum / len(random_arr))


random_calculation()


def pattern_mather(pattern: str, text_list: List[str]) -> List[str]:
    map_dictionary = {}
    for i in range(0, len(pattern)):
        if pattern[i] is not "*":
            map_dictionary[i] = pattern[0]

    return [string for string in text_list if all(string[i] == c for i, c in map_dictionary.items())]


L = ['aababacaa', 'cabaabcca', 'aaabbcbacb', 'acababbaab']
my_pattern = "a**a******"

print(pattern_mather(my_pattern, L))


def to_arabic(roman: str) -> int:
    arabic: List[int] = [1000, 500, 100, 50, 10, 5, 1]
    roman_arr: List[chr] = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    i: int = 0
    j: int = 0
    result: int = 0
    while j < len(roman) and i < len(arabic):
        if roman[j] == roman_arr[i]:
            result += arabic[i]
            j += 1
        elif ((i % 2 == 0)
              and (i < len(roman_arr) - 2)
              and (j < len(roman) - 1)
              and (roman[j] == roman_arr[i + 2])
              and (roman[j + 1] == roman_arr[i])):
            result += arabic[i] - arabic[i + 2]
            j += 2
            i += 1
        elif ((i % 2 == 1)
              and (i < len(roman_arr) - 1)
              and (j < len(roman) - 1)
              and (roman[j] == roman_arr[i + 1])
              and (roman[j + 1] == roman_arr[i])):
            result += arabic[i] - arabic[i + 1]
            j += 2
            i += 1
        else:
            i += 1

    if i == len(roman_arr):
        return -1
    return result


print(to_arabic('MMMCMXCIX'))


class NumericStringParser(object):
    def pushFirst(self, strg, loc, toks):
        self.exprStack.append(toks[0])

    def pushUMinus(self, strg, loc, toks):
        if toks and toks[0] == '-':
            self.exprStack.append('unary -')

    def __init__(self):
        """
        expop   :: '^'
        multop  :: '*' | '/'
        addop   :: '+' | '-'
        integer :: ['+' | '-'] '0'..'9'+
        atom    :: PI | E | real | fn '(' expr ')' | '(' expr ')'
        factor  :: atom [ expop factor ]*
        term    :: factor [ multop factor ]*
        expr    :: term [ addop term ]*
        """
        point = Literal(".")
        e = CaselessLiteral("E")
        fnumber = Combine(Word("+-" + nums, nums) +
                          Optional(point + Optional(Word(nums))) +
                          Optional(e + Word("+-" + nums, nums)))
        ident = Word(alphas, alphas + nums + "_$")
        plus = Literal("+")
        minus = Literal("-")
        mult = Literal("*")
        div = Literal("/")
        lpar = Literal("(").suppress()
        rpar = Literal(")").suppress()
        addop = plus | minus
        multop = mult | div
        expop = Literal("^")
        pi = CaselessLiteral("PI")
        expr = Forward()
        atom = ((Optional(oneOf("- +")) +
                 (ident + lpar + expr + rpar | pi | e | fnumber).setParseAction(self.pushFirst))
                | Optional(oneOf("- +")) + Group(lpar + expr + rpar)
                ).setParseAction(self.pushUMinus)
        factor = Forward()
        factor << atom + \
        ZeroOrMore((expop + factor).setParseAction(self.pushFirst))
        term = factor + \
               ZeroOrMore((multop + factor).setParseAction(self.pushFirst))
        expr << term + \
        ZeroOrMore((addop + term).setParseAction(self.pushFirst))
        self.bnf = expr
        epsilon = 1e-12
        self.opn = {"+": operator.add,
                    "-": operator.sub,
                    "*": operator.mul,
                    "/": operator.truediv,
                    "^": operator.pow}
        self.fn = {"sin": math.sin,
                   "cos": math.cos,
                   "tan": math.tan,
                   "exp": math.exp,
                   "sqrt": math.sqrt,
                   "log": math.log,
                   "log2": math.log2,
                   "log10": math.log10,
                   "degrees": math.degrees,
                   "factorial": math.factorial,
                   "floor": math.floor,
                   "gcd": math.gcd,
                   "abs": abs,
                   "trunc": lambda a: int(a),
                   "round": round,
                   "sgn": lambda a: abs(a) > epsilon and cmp(a, 0) or 0}

    def evaluateStack(self, s):
        op = s.pop()
        if op == 'unary -':
            return -self.evaluateStack(s)
        if op in "+-*/^":
            op2 = self.evaluateStack(s)
            op1 = self.evaluateStack(s)
            return self.opn[op](op1, op2)
        elif op == "PI":
            return math.pi  # 3.1415926535
        elif op == "E":
            return math.e  # 2.718281828
        elif op in self.fn:
            return self.fn[op](self.evaluateStack(s))
        elif op[0].isalpha():
            return 0
        else:
            return float(op)

    def eval(self, num_string, parseAll=True):
        self.exprStack = []
        results = self.bnf.parseString(num_string, parseAll)
        val = self.evaluateStack(self.exprStack[:])
        return val


def calculator() -> None:
    nsp = NumericStringParser()
    print("Enter \'x\' to exit")
    while True:
        x = input(">> ")
        if x == "x":
            return
        try:
            print(nsp.eval(x))
        except Exception:
            print('Bad formula')


calculator()
