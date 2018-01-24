# -*- coding: UTF-8 -*
from janome.tokenizer import Tokenizer


def main():
    ids =['今日の天気は晴れ', '昨日の天気は雨']
    print(type(ids))
    data = []
    t = Tokenizer()  # Tokenizerの初期化は一回だけでOKです。
    for text in ids:
        for token in t.tokenize(text):
            data.append(token.surface)
            print(data)


if __name__ == "__main__":
    main()
