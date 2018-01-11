# -*- coding: utf-8 -*-
import random


def main():
    item = {'peach': '4', 'melon': '4', 'Cherry': '1', 'orange': '3', 'Grape': '4', 'persimmon': '3', 'strawberry': '3',
            'watermelon': '7', 'pear': '4', 'grapefruit': '3', 'banana': '2', 'Apple': '5', 'pineapple': '6'}
    fruit, val = random.choice(list(item.items()))
    print(fruit, val)


if __name__ == '__main__':
    main()
