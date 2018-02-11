# -*- coding: utf8 -*-
import time
from io import BytesIO
from contextlib import closing
import argparse
import serial
import tornado.ioloop


class MySerial(object):
    def __init__(self, port: str, baud_rate: int, lineterminator: str):
        self._serial_port = serial.Serial(port, baud_rate)
        self._line_terminator = lineterminator
        self.io_loop = tornado.ioloop.IOLoop.current()
        self._read_buffer = b''
        self.is_start = False

    def start(self):
        self._read()
        self.io_loop.call_later(1, self.start)

    def _read(self) -> None:
        self._read_buffer += self._serial_port.read(self._serial_port.in_waiting)
        data = self._read_buffer.split(self._line_terminator)
        # next_token
        self._read_buffer = data.pop()
        self.on_fire_callback(data)

    def on_fire_callback(self, data: list) -> None:
        for msg in data:
            print(f"msg:{msg}")

    def close(self) -> None:
        if self._serial_port is not None:
            self._serial_port.close()
            self._serial_port = None

def get_input() -> any:
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', default='COM4')
    parser.add_argument('--baud_rate', '-rate', default=115200, type=int)
    parser.add_argument('--lineterminator', '-lt', default=b'\r\n')
    return parser.parse_args()


def main() -> None:
    args = get_input()
    with closing(MySerial(args.port, args.baud_rate, args.lineterminator)) as con1:
        print(f"serving at:{args.port},{args.baud_rate}")
        con1.start()
        con1.io_loop.start()
        #tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
