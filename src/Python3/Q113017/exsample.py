# -*- coding: utf8 -*-
import linecache


def split_word_list(line: str) -> list:
    word_list = []
    word = []
    for c in line:
        if c == ' ':
            print(word)
            word_list.append(word)
            word = []
            continue
        word.append(c)
    else:
        print(word)
        word_list.append(word)
    return word_list


def main() -> None:
    line_no = 1
    file_name = r'sample.txt'
    target_line = linecache.getline(file_name, line_no)
    target_line = 'This is an apple'
    word_list = split_word_list(target_line)
    print(word_list)


if __name__ == '__main__':
    main()


