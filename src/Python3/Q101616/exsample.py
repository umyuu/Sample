# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_response(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    return requests.get(url, headers={'User-Agent': user_agent}, timeout=2000)


def main():
    url = 'https://shikiho.jp/tk/stock/info/9983'
    soup = BeautifulSoup(get_response(url).content, 'html.parser')
    for syuyou in soup.find_all(class_='syuyou'):
        for tr_tag in syuyou.find_all('tr'):
            print('=' * 50)
            #他の値を取りたい時はこの部分のコメントを外して試行錯誤してみてくださいな。
            #print(tr_tag)
            print(tr_tag.th.text)
            if tr_tag.td is None:
                continue
            print('#' * 50)
            print(tr_tag.td.text)
            print('#' * 50)


if __name__ == '__main__':
    main()
