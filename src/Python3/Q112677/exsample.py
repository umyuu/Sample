# -*- coding: utf8 -*-
import functools


@functools.lru_cache(maxsize=None)
def get_stopwords() -> tuple: # 上記のc2に該当
  '''
  ストップワードリストを返す
  '''

  from time import sleep
  # キャッシュ確認用のデバックスリープ！
  sleep(3)

  import urllib.request
  url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
  with urllib.request.urlopen(url) as response:
      stop_words = [w for w in response.read().decode().split('\r\n') if w != '']
  stop_words.extend(['れる', 'られる', 'する', 'いる', 'なる', 'ある', 'できる', 'おる'])
  return tuple(stop_words)


def main() -> None:
    for i in range(10):
        print(get_stopwords())


if __name__ == '__main__':
    main()
