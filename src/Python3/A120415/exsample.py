# -*- coding: utf8 -*-
from bs4 import BeautifulSoup


def main() -> None:
    xml_str = """
    <div class = "AAA">
    <p class ="BBB">XXX</p>
    <p> YYY </p>
    </div>
    <div class = "AAA">
    <p class = "BBB">ZZZ</p>
    <p>WWW</p>
    </div>
    """
    soup = BeautifulSoup(xml_str, "html.parser")
    elements = soup.select("div.AAA > p:nth-of-type(2)")
    # elements -> [<p> YYY </p>, <p>WWW</p>]
    target = elements.pop()
    print(target.text)
    # index指定
    target = soup.select("div.AAA > p:nth-of-type(2)")[1]
    # target -> <p>WWW</p>
    print(target.text)
if __name__ == '__main__':
    main()
