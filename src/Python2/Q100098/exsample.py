# -*- coding: utf-8 -*-
# python 2.7
from __future__ import unicode_literals
import codecs


def main():
    with codecs.open('test.txt', 'r', encoding='utf-8-sig') as f:
        for text in f.readlines():
            text = text.rstrip('\r\n')
            print text, len(text)


if __name__ == '__main__':
    main()
