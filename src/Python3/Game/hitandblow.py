# -*- coding: UTF-8 -*
import random


class HitAndBlow(object):
    def __init__(self, n=3):
        self.N = n
        self.answer = self.generate()

    def generate(self):
        """
        答えの数字を生成。
        :return:
        """
        digits = [i for i in range(10)]
        random.shuffle(digits)
        return digits[:self.N]

    def judge(self, guess):
        """
        Hit&Blowの判定処理
        :param guess: 予測した数字
        :return:
        """
        assert len(guess) == len(self.answer)
        hit = sum(g == a for g, a in zip(guess, self.answer))
        blow = sum(g in self.answer for g in guess) - hit
        return hit, blow


def main():
    game = HitAndBlow()
    while True:
        input_num = input(f"予想する{game.N}桁の数字を入力してください:")
        guess = [int(x) for x in list(input_num)]
        if len(guess) != game.N:
            continue

        #print(game.answer)
        hit, blow = game.judge(guess)
        print(f"Hit:{hit}, Blow:{blow}")
        if hit == game.N:
            print('正解です')
            break


if __name__ == '__main__':
    main()
