# -*- coding: UTF-8 -*
from bs4 import BeautifulSoup as bs
import requests as req


def main():
    url = 'http://日本語.jp/'
    res = req.get(url, timeout=2000)
    print(res.encoding)
    # res.contentまたは res.text
    soup = bs(res.content, 'html.parser')
    print(soup)


if __name__ == "__main__":
    main()
