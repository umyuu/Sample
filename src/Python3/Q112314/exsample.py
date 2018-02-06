# -*- coding: utf8 -*-


def generate_onomatopee(front: str, back: str='', repeat: int=2) -> str:
    """
    :param front:接頭語
    :param back:接尾語
    :param repeat:繰り返し回数
    :return:オノマトペ
    """
    return (front + back) * repeat


def main() -> None:
    tokens =[
        generate_onomatopee('ごろ', 'ごろ'),
        generate_onomatopee('わく'),
        generate_onomatopee('わん')
    ]
    for i in tokens:
        print(i)


if __name__ == '__main__':
    main()
