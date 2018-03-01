# -*- coding: utf8 -*-
import sys
import os
import io


def main() -> None:
    # encodingをprint
    print("PYTHONIOENCODING:{0}".format(os.environ.get('PYTHONIOENCODING', '')))
    print("std in:{0}".format(sys.stdin.encoding))
    print("std out:{0}".format(sys.stdout.encoding))
    # shift-jisに
    encoding = 'utf-8'
    encoding = 'shift-jis'
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding=encoding)
    year = int(input("西暦何年?"))
    print("std in:{0}".format(sys.stdin.encoding))
    print(year)


if __name__ == '__main__':
    main()
