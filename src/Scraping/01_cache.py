# -*- coding: utf-8 -*-
import time
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests


class Downloader(object):
    def __init__(self):
        self.download_dir = Path(r'./download')
        if not self.download_dir.exists():
            self.download_dir.mkdir()
        self.timeout = 2000

    @staticmethod
    def hash_value(url):
        h = hashlib.sha512()
        h.update(url.encode('utf-8'))
        return '$6$$' + h.hexdigest()

    def get_content(self, url):
        file = self.download_dir.joinpath(Downloader.hash_value(url))
        if file.exists():
            with file.open('rb') as f:
                return f.read()
        # sleep
        time.sleep(5)
        res = requests.get(url, timeout=self.timeout)
        with file.open('wb') as f:
            f.write(res.content)
        return res.content


def main():
    dl = Downloader()
    urls = ['http://www.example.com/',
            'https://teratail.com/',
            'https://teratail.com/questions/109282',
            'https://www.google.co.jp/']

    with ThreadPoolExecutor(max_workers=2) as executor:
        future_to_url = {executor.submit(dl.get_content, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                print(data)
            except Exception as ex:
                print('url:{0} exception:{1}'.format(url, ex))


if __name__ == '__main__':
    main()
