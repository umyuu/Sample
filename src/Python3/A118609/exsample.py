import time
from datetime import datetime
import json
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


def get_content(url: str='https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc'):
    s = requests.Session()
    retries = Retry(total=5,
                    backoff_factor=0.1,
                    status_forcelist=[500, 502, 503, 504])
    s.mount('https://', HTTPAdapter(max_retries=retries))
    payload = {'periods': '60'}
    r = s.get(url, params=payload)
    # ↓テスト用コード
    # r.status_code = 429
    if r.status_code == 429:
        # APIのドキュメントにはr.json()できるかどうかの保証の記述はなかったので注意です。
        # r.json()出来ない場合は値:Noneを返してくださいな。
        return r.json(), r.status_code
    return r.json(), r.status_code


def data_write(obj):
    file_name = f'{datetime.now().strftime("%Y%m%d_%H%M%S_%f")}.json'
    #print(f'file write:{file_name}')
    with open(file_name, 'w', encoding='utf-8-sig') as f:
        json.dump(obj, f)


def main() -> None:
    CLOSE = 4
    while True:
        content, status_code = get_content()
        # rate_limitなら
        if status_code == 429:
            # sleepタイムを55秒に
            time.sleep(55)
            continue

        json = content['result']['60']
        close = json[-1][CLOSE]
        print(str(datetime.fromtimestamp(round(time.time()) + 60 * 60 * 9)) + ' CLOSE: ' + str(close))  # 直近の終値の表示
        # ファイルに保存したい時。
        #data_write(json)

        time.sleep(5)


if __name__ == '__main__':
    main()
