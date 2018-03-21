# -*- coding: utf8 -*-
import os
# d.pyをimportする。
import d


def main() -> None:
    print("""

    意見をください

    """)
    with open('box.txt', 'w', encoding='utf-8') as f:
        while True:
            q = input('>>> ')
            if q == 'send':
                break
            f.write(q + '\n')
        f.write('-' * 50 + '\n')
    # d.pyの関数を呼び出す。
    d.thank_you()


if __name__ == '__main__':
    main()
