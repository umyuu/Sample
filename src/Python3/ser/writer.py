# -*- coding: utf8 -*-
import random
import argparse
from io import StringIO
import time
import serial


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', default='COM3')
    parser.add_argument('--baud_rate', '-rate', default=115200, type=int)
    args = parser.parse_args()

    with serial.Serial(args.port, args.baud_rate, timeout=300) as con1:
        while True:
            io_buffer = StringIO()
            io_buffer.write("Hello\r\n")
            io_buffer.write("World\r\n")
            io_buffer.write(f"{random.randint(0,500)}\r\n")
            con1.write(io_buffer.getvalue().encode())
            time.sleep(1)


if __name__ == '__main__':
    main()
