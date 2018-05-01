# -*- coding: utf8 -*-
from os import getcwd
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn
from ipaddress import ip_address
from html import escape


class MyHandler(SimpleHTTPRequestHandler):
    def to_content(self) -> str:
        body = f"time:{escape(self.date_time_string())}<br>dir:{escape(getcwd())}"
        content = f"<html><head></head><body>{body}</body></html>"
        return content

    def do_GET(self):
        req_ip = ip_address(self.client_address[0])
        # IPアドレスによる簡易的なアクセス制限
        # ループバック,ローカルアドレス以外はステータスコード:403を返す
        is_accepted = any([req_ip.is_loopback, req_ip.is_private])
        if is_accepted:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(self.to_content().encode('utf-8'))
            self.wfile.write(b'\n')
            return
        else:
            self.send_response(403)
            self.end_headers()
            return


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True


def main() ->None:
    PORT = 8000
    with ThreadingHTTPServer(("", PORT), MyHandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


if __name__ == '__main__':
    main()
