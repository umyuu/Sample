# -*- coding: utf8 -*-


def main() -> None:
    data = [('Candidate is jerk, alleges rival', 338647), ('Bears love berries, alleges bear', 253801), ('Bad things gone, say good people', 170098)]
    for article, view in data:
        print(f'"{article}" — {view} views')


if __name__ == '__main__':
    main()
