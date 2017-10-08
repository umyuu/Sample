# -*- coding: utf-8 -*-
import requests
import bs4


def main():
    search_payload = {'tbm': 'isch', 'q': 'ユニティちゃん'}
    res = requests.get("https://www.google.co.jp/search", params=search_payload)
    soup = bs4.BeautifulSoup(res.text)
    for tag in soup.find_all('img'):
        print(tag.get("src"))


if __name__ == '__main__':
    main()
