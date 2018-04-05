# -*- coding: utf8 -*-
import datetime as dt
import json
#
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_content(params:dict):
    url = "https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc"
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.text


def main() -> None:
    startDate = "2018-03-23 00:00:00"
    endDate = "2018-03-23 23:00:00"
    start_timestamp = dt.datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S').timestamp()
    end_timestamp = dt.datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S').timestamp()
    query = {"periods": 3600, "after": str(int(start_timestamp)), "before": str(int(end_timestamp))}
    res = json.loads(get_content(query))["result"]["3600"]
    res = np.array(res)

    time_stamp = res[:, 0].reshape(len(res), 1)
    close_price = res[:, 4].reshape(len(res), 1)
    tmp_data = np.hstack((time_stamp, close_price))
    data = pd.DataFrame(tmp_data, columns=['ds', 'y'])

    from pytz import timezone
    #data['ds'] = data['ds'].apply(lambda x: dt.datetime.fromtimestamp(x,tz=timezone('Asia/Tokyo')))
    data['ds'] = data['ds'].apply(lambda x: dt.datetime.fromtimestamp(x))
    file_name = f'bitflyer-{query["after"]}-{query["before"]}.csv'
    data.to_csv(file_name, index=False)
    data = pd.read_csv(file_name)
    data.plot()
    plt.show()


if __name__ == '__main__':
    main()
