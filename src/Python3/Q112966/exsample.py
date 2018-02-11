# -*- coding: utf8 -*-
from bs4 import BeautifulSoup


def main() -> None:
    html = """<!DOCTYPE html><head><title></title></head>
        <body>
            <a>15m<sup>2</sup></a>,
            <a>100kg</a>
        </body></html>"""

    soup = BeautifulSoup(html, 'lxml')
    result = soup.find_all("a")
    for el in result:
        print("#" * 20)
        print(el.contents[0].string)
        print(el.text)
        print(el.string)


if __name__ == '__main__':
    main()
