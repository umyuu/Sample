# -*- coding: utf-8 -*-
import bs4


def main():
    html = "<!DOCTYPE html><html lang='ja'><head><title></title></head>" \
           "<body>" \
           "<div class='name'>吉田<wbr>太郎</div>" \
           "<div class='name'>田中<wbr>一郎</div>" \
           "</body></html>"
    soup = bs4.BeautifulSoup(html, 'lxml')
    for name_list in soup.find_all(class_='name'):
        print("-" * 40)
        print(name_list)
        print(name_list.text)


if __name__ == '__main__':
    main()
