# -*- coding: utf8 -*-
import urllib.request
from bs4 import BeautifulSoup


def get_content(url:str):
    """
    @params url スクレイピング対象のURL
    """
    with urllib.request.urlopen(url) as response:
        return BeautifulSoup(response.read(), "html.parser")


def get_data(soup) -> str:
    i = 0
    for parent in soup.find('div', {'class': 'race_otherdata'}):
        data = parent.string.rstrip()
        if len(data) == 0:
            continue
        if i == 2:
            # 本賞金以降はSkip
            continue
        yield data
        i += 1


def main() -> None:
    url = 'http://race.netkeiba.com/?pid=race_old&id=p201805010301'
    soup = get_content(url)
    # python 3なのでcodec.openは不要
    with open('tokyo_race_1.csv', 'w', encoding='utf-8') as f:
        f.write('other_race_name' + u"\n")
        for row in get_data(soup):
            print(row)
            f.write(row + "\n")


if __name__ == '__main__':
    main()
