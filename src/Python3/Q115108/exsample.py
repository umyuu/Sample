# -*- coding: utf8 -*-
from bs4 import BeautifulSoup, NavigableString


def get_content():
    body = """
    <li class="text-en text-c">
    A 
    <a href="/word/en/change/#ej-14756">
    <span class="a_line">
    <span class="a_moji" title="changeの意味">change</span>
    </span>
    </a> 
    <a href="/word/en/of/#ej-58587">
    <span class="a_line">
    <span class="a_moji" title="ofの意味">
    of
    </span>
    </span>
    </a> 
    <a href="/word/en/air/#ej-1635">
    <span class="a_line">
    <span class="a_moji" title="airの意味">
    air
    </span>
    </span>
    </a> 
    <a href="/word/en/always/#ej-2421">
    <span class="a_line">
    <span class="a_moji" title="alwaysの意味">
    always
    </span>
    </span>
    </a> 
    <i><i>profit</i>s</i> 
    <a href="/word/en/in/#ej-43166">
    <span class="a_line">
    <span class="a_moji" title="inの意味">
    in
    </span>
    </span>
    </a> 
    <a href="/word/en/your/#ej-96280">
    <span class="a_line">
    <span class="a_moji" title="yourの意味">
    your
    </span>
    </span>
    </a> 
    <a href="/word/en/case/#ej-13775">
    <span class="a_line">
    <span class="a_moji" title="caseの意味">
    case
    </span>
    </span>
    </a>
    .
    </li>

    """
    return BeautifulSoup(body, "html.parser")


def main() -> None:
    soup = get_content()

    tag = soup.find("li", class_="text-en text-c")
    print(tag.i.text.strip())
    contentsList = soup.find("li", class_="text-en text-c").contents

    for _, data in enumerate(contentsList):
        if len(data) == 0:
            continue
        if isinstance(data, NavigableString):
            continue
        #print("#" * 40)

        #print(data.text.strip())


if __name__ == '__main__':
    main()
