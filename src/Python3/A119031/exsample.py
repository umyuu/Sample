# -*- coding: utf8 -*-
import json
from oauth2client.client import flow_from_clientsecrets
import webbrowser
from oauth2client.file import Storage
import requests


def main() -> None:
    # pip install oauth2client
    # client_secretsはgoogleコンソールより作成
    flow = flow_from_clientsecrets(
        'secret/client_secrets.json',
        scope='https://picasaweb.google.com/data/',
        redirect_uri="urn:ietf:wg:oauth:2.0:oob"
    )

    auth_uri = flow.step1_get_authorize_url()
    webbrowser.open(auth_uri)

    token = input("Input your code > ")

    credentials = flow.step2_exchange(token)

    # file.Storage
    storage = Storage('secret/credentials')
    storage.put(credentials)
    # 1.with文を使用するように変更
    with open("secret/credentials") as json_file:
        load = json.load(json_file)

    access_token = load["access_token"]
    user_id = 'default'
    # 2.エンドポイントを変更
    url = 'https://picasaweb.google.com/data/feed/api/user/{}'.format(user_id)
    # 3.headerを変更
    head = {'Authorization': 'OAuth {}'.format(access_token), 'GData-Version': '3'}
    print(head)
    response = requests.get(url, headers=head)
    print(response)


if __name__ == '__main__':
    main()
