# -*- coding: UTF-8 -*
import random


class HitAndBlow(object):
    def __init__(self, n: int=3):
        assert 10 >= n
        self.N = n
        self.answer = self.generate()

    def generate(self) -> list:
        """
        答えの数字を生成。
        :return:
        """
        digits = list(range(10))
        random.shuffle(digits)
        return digits[:self.N]

    def predict(self, guess: list) -> tuple:
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
        user_input = input(f"予想する{game.N}桁の数字を入力してください:")
        if len(user_input) != game.N:
            continue
        guess = [int(i) for i in user_input]

        #print(game.answer)
        hit, blow = game.predict(guess)
        print(f"Hit:{hit}, Blow:{blow}")
        # ゲームクリア
        if hit == game.N:
            print('正解です！')
            break


if __name__ == '__main__':
    main()
