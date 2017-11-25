# -*- coding: utf-8 -*-
import timeit


def double(x):
    y = 2 * x
    return y


def func_repeat(I):
    x = 1
    for i in range(0, I):
        x = double(x)
    return x


def func_answer(I):
    return 2 ** I


def question():
    return [func_repeat(j) for j in range(0, 11)]


def answer():
    return [func_answer(j) for j in range(0, 11)]


def main():
    iteration = 100000
    print(timeit.timeit(question, number=iteration))
    print(question())
    print(timeit.timeit(answer, number=iteration))
    print(answer())


if __name__ == '__main__':
    main()
