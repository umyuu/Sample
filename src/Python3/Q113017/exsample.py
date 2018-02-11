# -*- coding: utf8 -*-
import linecache


def main() -> None:
    line_no = 1
    file_name = r'sample.txt'
    target_line = linecache.getline(file_name, line_no)
    for c in target_line:
        print(c)


if __name__ == '__main__':
    main()


