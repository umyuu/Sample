# -*- coding: utf-8 -*-
import requests
import bs4
import pandas as pd # pandas


def main():
    html ="""
    <ul id="front">
        <li class="icon-01">乗用車</li>
        <li class="icon-02">トラック</li>
        <li class="icon-11">軽自動車</li>
        </ul>
    """
    soup = bs4.BeautifulSoup(html, "lxml")
    icon_part = soup.find_all("ul", id="front")
    car_model = []
    for ul_tag in icon_part:
        for li in ul_tag.find_all('li'):
            car_model.append(li.text)
    print(car_model)


if __name__ == '__main__':
    main()
