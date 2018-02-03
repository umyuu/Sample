# -*- coding: utf8 -*-
import csv


def main():
    items = {}
    with open('settings.txt', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=':')
        for row in reader:
            key = row[0]
            val = row[1].lstrip()
            if val.isdigit():
                items[key] = int(val)
            else:
                items[key] = val

    print(items)


if __name__ == '__main__':
    main()
