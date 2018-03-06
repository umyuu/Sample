# -*- coding: utf-8 -*-
import requests
from pprint import PrettyPrinter


def main() -> None:
    URL = 'https://api.openbd.jp/v1/get?isbn=4873112990'
    response = requests.get(URL)
    data = response.json()
    pp = PrettyPrinter()
    pp.pprint(data)


if __name__ == "__main__":
    main()
