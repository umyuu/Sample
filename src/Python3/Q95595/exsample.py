# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import os
SCR_HEIGHT = 480.0
SCR_WIDTH = 640.0
SCR_RECT = (int(SCR_WIDTH), int(SCR_HEIGHT))

PLAYER_IMG = [[0 for i in range(3)] for j in range(4)]
IMG_NAME = ["player_down", "player_left", "player_right", "player_up"]


class test_play(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCR_RECT)
        pygame.display.set_caption("テスト画面")

        #画像
        for j, name in enumerate(IMG_NAME):
            for i in range(3):
                PLAYER_IMG[j][i] = pygame.image.load("image/" + name + "_"+str(i)+".png").convert_alpha()
                print("image/" + name + "_" + str(i) + ".png==>success")
        #グループ作成
        self.all = pygame.sprite.RenderUpdates()
        Player.containers = self.all
        Player()

    def mainloop(self):
        """
        メインループ
        :return:
        """
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.update()
            self.draw(self.screen)
            pygame.display.update()
            self.key_handl()

    def key_handl(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.on_application_exit(1)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.on_application_exit(1)

    def on_application_exit(self, code):
        """
        アプリケーション終了処理
        :param code: key_handlから呼び出し時:1
        :return:
        """
        pygame.quit()
        sys.exit()

    def update(self):
        self.all.update()

    def draw(self, screen):
        screen.fill((0,0,0))
        self.all.draw(screen)


class Player(pygame.sprite.Sprite):
    MOVE_SPEED = 5.0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = PLAYER_IMG[0][0]
        self.rect = self.image.get_rect()
        #小数点
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.move_x = 0.0
        self.move_y = 0.0
        self.walk = 0

    def update(self):
        key_handl = pygame.key.get_pressed()
        #print(self.rect)
        #アクション
        if key_handl[K_LEFT]:
            self.image = PLAYER_IMG[1][int(self.walk)]
            self.move_x = -self.MOVE_SPEED
        elif key_handl[K_RIGHT]:
            self.image = PLAYER_IMG[2][int(self.walk)]
            self.move_x = self.MOVE_SPEED
        else:
            self.move_x = 0.0
        if key_handl[K_UP]:
            self.image = PLAYER_IMG[3][int(self.walk)]
            self.move_y = -self.MOVE_SPEED
        elif key_handl[K_DOWN]:
            self.image = PLAYER_IMG[0][int(self.walk)]
            self.move_y = self.MOVE_SPEED

        else:
            self.move_y = 0.0

        if self.walk < 2:
            self.walk += 0.2
        else:
            self.walk = 0

        if self.rect.x < 0:
            print("flg")
            self.move_x = self.MOVE_SPEED / 2
        elif self.rect.x > SCR_WIDTH:
            self.rect.x = SCR_WIDTH  # if文と代入文は画像サイズを意識して修正する必要があります。
        if self.rect.y < 0:
            self.move_y = self.MOVE_SPEED / 2
        elif self.rect.y > SCR_HEIGHT:
            self.rect.y = SCR_HEIGHT # この部分も同様です。
        self.x += self.move_x
        self.y += self.move_y
        #intへ整形
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)


def main():
    t = test_play()
    t.mainloop()


if __name__ == "__main__":
    main()
