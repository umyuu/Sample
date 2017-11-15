# -*- coding: utf-8 -*-
def search(key, arr):
    return list(filter(lambda n: n[0] == key, arr))


def main():
    arr = [[100, 2], [300, 3], [500, 4], [800, 5], [200, 6]]
    inp_id = 200
    ret = search(inp_id, arr)
    print(ret)
    if len(ret) > 0:
        print("ok")
    else:
        print("Error")


if __name__ == '__main__':
    main()
