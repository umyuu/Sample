# -*- coding: utf8 -*-
import requests


def post_content(json_data: dict):
    # identity.tyo1.conoha.io ←送り先はここでいいのかコントロールパネルで確認してください。
    url = 'https://identity.tyo1.conoha.io/v2.0/tokens'
    url = 'http://localhost:3000/v2.0/tokens'
    return requests.post(url=url, json=json_data)


def main() -> None:
    json_data = {"auth": {
        "passwordCredentials": {
            "username": "aaa",
            "password": "bbb"
        },
        "tenantId": "ccc"
        }}
    res = post_content(json_data)
    res.raise_for_status()
    print(res.json())


if __name__ == '__main__':
    main()
