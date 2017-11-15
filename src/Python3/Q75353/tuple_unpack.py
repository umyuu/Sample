# -*- coding: utf-8 -*-
def main():
    ab = [('a1', 'b1'), ('a2', 'b2'), ('a3', 'b3'), ('an', 'bn')]
    a, b = map(list, zip(*ab))
    print(a)
    print(b)

if __name__ == '__main__':
    main()
