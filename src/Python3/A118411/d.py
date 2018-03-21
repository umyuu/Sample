# -*- coding: utf8 -*-
import sys

# thank_you 関数を作成する
def thank_you() -> None:
    print("""

    ありがとう！(∩´∀｀)∩

    """)

    q = input("どういたしまして！")

    if q:
        sys.exit()


def main() -> None:
    thank_you()


if __name__ == '__main__':
    main()
