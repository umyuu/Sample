# -*- coding: utf-8 -*-
from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer


class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass


def get_input():
    import argparse
    parser = argparse.ArgumentParser(description='test http server')
    parser.add_argument('--host', '-ho', default='localhost',
                        help='using host')
    parser.add_argument('--port', '-p', type=int, default=8000,
                        help='using port')
    return parser.parse_args()


def main():
    args = get_input()
    server = ThreadingSimpleServer((args.host, args.port), SimpleHTTPRequestHandler)
    try:
        print('serving at', args.host, ':', args.port,)
        while True:
            server.handle_request()
    except KeyboardInterrupt:
        print("Finished")


if __name__ == '__main__':
    main()
