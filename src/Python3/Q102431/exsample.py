# -*- coding: utf-8 -*-
from lxml import etree
from lxml import html
import requests

#doesn't work

def main():
    url = 'http://lispon.moe/cdn/activity/act161108/index.html?aUserId=1494366573'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    print(page.content)
    xpath_selector = "//a/@href"
    #xpath_selector = "//p[contains(@class,'followed')]"
    prices = tree.xpath(xpath_selector)
    print(prices)


if __name__ == '__main__':
    main()
