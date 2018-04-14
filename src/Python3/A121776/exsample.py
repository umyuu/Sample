# -*- coding: utf8 -*-
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn
import html


class MyHandler(SimpleHTTPRequestHandler):
    def to_content(self) ->str:
        body = f"time:{html.escape(self.date_time_string())}<br>dir:{html.escape(os.getcwd())}"
        content = f"<html><head></head><body>{body}</body></html>"
        return content

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(self.to_content().encode('utf-8'))
        self.wfile.write(b'\n')


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True


def main() ->None:
    PORT = 8000
    print(os.getcwd())
    print(os.path.abspath(__file__))
    with  ThreadingHTTPServer(("", PORT), MyHandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


if __name__ == '__main__':
    main()
