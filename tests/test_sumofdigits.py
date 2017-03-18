# -*- coding: utf-8 -*-
import pytest
import sys
import os
import math
# pylint: disable=C0103

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
for path in [parent_dir, os.path.join(parent_dir, 'src')]:
    if not (path in sys.path):
        sys.path.insert(0, path)

from sumofdigits import Calc


class TestClass(object):
    def test_sumofdigits(self):
        calc = Calc()
        tests = [[-237, -12], [-10, -1], [-9, -9], [-1, -1],
                 [0, 0], [1, 1], [9, 9], [10, 1], [237, 12], [sys.maxsize + 1, 89],
                 [float("inf"), float("inf")], [float("-inf"), float("-inf")]]
        for item in tests:
            x = item[0]
            y = item[1]
            assert calc.sum_of_digits(x) == y, 'x:{0},y:{1}'.format(x, y)
        # nan test
        assert math.isnan(calc.sum_of_digits(float("nan")))
        
if __name__ == '__main__':
    pytest.main("--capture=sys")
