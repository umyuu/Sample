# -*- coding: utf-8 -*-
from datetime import datetime
import requests


def main() -> None:
    url = 'https://www.google.co.jp/'
    querystring = {"Id": "3333", "Id2": "4444", "from": "xxx", "to": "yyy"}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)

    file_name = querystring['Id'] + '_' + querystring['Id2'] + '.json'
    with open(file_name, 'a') as f:  # 追記モードで開く
        f.write('\n' + '#' * 60 + '\n')
        f.write(str(response.status_code) + '\n') # ステータスコードを書き込み
        f.write(datetime.now().strftime('%Y%m%d_%H%M%S_%f') + '\n')
        f.writelines(response.text)  # シーケンスが引数。


if __name__ == "__main__":
    main()

