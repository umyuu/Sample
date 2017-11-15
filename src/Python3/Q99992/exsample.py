# -*- coding: utf-8 -*-
import threading
import time


def log(text):
    print("{0}:{1}".format(text, time.time()))


def hello():
    log("hello")


def main():
    # 5秒後に実行
    t = threading.Timer(5, hello)
    t.start()
    log("main ")
    time.sleep(7)
    log("main ")


if __name__ == '__main__':
    main()