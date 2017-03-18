# -*- coding: utf-8 -*-
import sys
import math


class Calc(object):
    def sum_of_digits(self, n):
        """
        :param n:{int}
        :return:
        for example)
            input   -> output
            -237    -> -12
             237    -> 12
        """
        if math.isnan(n) or math.isinf(n):
            return n
        compare = 0
        if n > 0:
            compare = 1
        elif n < 0:
            compare = -1
        # note:他のプログラミング言語
        #      abs(number.min_value) -> number.min_value
        n = abs(n)
        sum = 0
        while n > 0:
            n, remainder = divmod(n, 10)
            sum += remainder
        return sum * compare


def main():
    numbers = [-237, -10, -9, -1,
               0, 1, 9, 10, 237,
               sys.maxsize + 1, float("inf"), float("-inf"),  float("nan")]
    calc = Calc()
    for i, n in enumerate(numbers):
        print('in:{0} -> out:{1}'.format(n, calc.sum_of_digits(n)))


if __name__ == '__main__':
    main()
