import json
from datetime import datetime
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
    return r.json()['result']['60']


def data_write(obj):
    file_name = f'{datetime.now().strftime("%Y%m%d_%H%M%S_%f")}.json'
    print(f'file write:{file_name}')
    with open(file_name, 'w', encoding='utf-8-sig') as f:
        json.dump(obj, f)


def main() -> None:
    content = get_content()
    print(content)
    # file作成
    data_write(content)


if __name__ == '__main__':
    main()
