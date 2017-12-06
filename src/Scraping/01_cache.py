# -*- coding: utf-8 -*-
import requests
import hashlib
from pathlib import Path
import time


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
        return h.hexdigest()

    def get(self, url):
        file = self.download_dir.joinpath(Downloader.hash_value(url))
        if file.exists():
            with file.open('rb') as f:
                return f.read()
        # ミリ秒に単位を変換
        time.sleep(10000/1000)
        res = requests.get(url, timeout=self.timeout)
        with file.open('wb') as f:
            f.write(res.content)
        return res.content


def main():
    dl = Downloader()
    content = dl.get('https://github.com/umyuu/Sample/tree/master/src')
    print(content)


if __name__ == '__main__':
    main()
