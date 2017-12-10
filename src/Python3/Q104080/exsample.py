# -*- coding: utf-8 -*-
from janome.tokenizer import Tokenizer


def main():
    t = Tokenizer()
    for token in t.tokenize(u'すもももももももものうち'):
        print('#' * 60)
        print(token)
        print(token.surface)
        print(token.part_of_speech)


if __name__ == '__main__':
    main()
