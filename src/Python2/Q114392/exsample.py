# -*- coding: utf8 -*-
import urllib2
import codecs
import time
from bs4 import BeautifulSoup


def get_content(url):
    from contextlib import closing
    with closing(urllib2.urlopen(url)) as response:
        return BeautifulSoup(response.read())


def get_data(soup):
    i = 0
    for parent in soup.find('div', {'class': 'race_otherdata'}):
        unicode_strings = unicode(parent.string).rstrip()
        if len(unicode_strings) == 0:
            continue
        if i == 2:
            # 本賞金以降はSkip
            continue
        yield unicode_strings
        i += 1


def main():
    with codecs.open('tokyo_race_1.csv', 'w', 'utf-8') as f1:
        f1.write('other_race_name' + u"\n")
        url = 'http://race.netkeiba.com/?pid=race_old&id=p201805010301'
        soup = get_content(url)
        for row in get_data(soup):
            print(row)
            f1.write(row + "\n")


if __name__ == '__main__':
    main()
