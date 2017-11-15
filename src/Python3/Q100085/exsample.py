# -*- coding: utf-8 -*-
import requests
from requests.compat import urljoin
from bs4 import BeautifulSoup

URL = 'http://www.gochiusa.com/ova/'


def download_images(url):
    """
    スクレイピング対象URLから、jpgファイル一覧URLを取得
    :param url: スクレイピング対象URL
    :return: yield
    """
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    for link in soup.find_all("img"):
        src_attr = link.get("src")
        if src_attr.endswith(".jpg"):
            print(src_attr)
            # 相対URLから絶対URLに変換
            yield urljoin(URL, src_attr)


def main():
    for target in download_images(URL):
        resp = requests.get(target)
        with open('img/' + target.split('/')[-1], 'wb') as f:
            f.write(resp.content)


if __name__ == '__main__':
    main()
