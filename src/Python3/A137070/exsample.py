# -*- coding: utf-8 -*-
import json
import socket
import threading
import requests


class SocketServer():
    def __init__(self):
        self.host = "127.0.0.1" #socket.gethostname()
        print(self.host)
        self.port = 50006
        self.clients = []

    def socket_server_up(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(10)
        fd, addr = sock.accept()


if __name__ == "__main__":
    print("サーバーを立ち上げます")

ss = SocketServer()
ss.socket_server_up()
