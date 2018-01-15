# -*- coding: utf-8 -*-
import requests


def main():
    url = "https://www.suruga-ya.jp/product/detail/WO10669"
    res = requests.get(url)
    print(res.text)
    print(res.encoding)
    with open("text.htm", "w", encoding=res.encoding) as f:
        f.write(res.text)
        f.close()


if __name__ == '__main__':
    main()
