# -*- coding: UTF-8 -*
import os


def find_text_file(file_path, keyword):
    lines = []
    with open(file_path, encoding='utf-8') as f:
        for no, line in enumerate(f):
            if line.find(keyword) >= 0:
                line = line.strip()
                s = "| {0:4}: {1}".format(no + 1, line)
                lines.append(s)
    return lines


def get_input():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword')
    return parser.parse_args()


def find_files(top='.'):
    for root, dirs, files in os.walk(top):
        for f in files:
            yield os.path.join(root, f), f


def main():
    args = get_input()
    keyword = args.keyword
    for full_path, f in find_files():
        try:
            result = find_text_file(full_path, keyword)
            # resultに結果があれば表示する
            if len(result) > 0:
                print("+ file:" + f)
                for li in result:
                    print(li)
        except Exception as ex:
            print(ex)
            continue


if __name__ == "__main__":
    main()
