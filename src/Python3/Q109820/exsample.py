# -*- coding: UTF-8 -*


def application(environ, start_response):
    #start_response('200 OK', [('Content-Type', 'text/html')])
    content = """<!DOCTYPE html><head></head><body>
<h1>お疲れ様です。</h1>
</body></html>"""
    return content.encode('utf-8')


def main():
    print(application(None, None))


if __name__ == "__main__":
    main()
