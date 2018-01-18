# -*- coding: UTF-8 -*
import sys
import time
import math
from enum import Enum, unique
import pygame
from pygame.locals import *


@unique
class GameState(Enum):
    START = 1
    COUNT_UP = 2
    RESULT = 3


def initialize():
    (w,h) = (400,400)   # 画面サイズ
    (x,y) = (w/2, h/2)
    pygame.init()       # pygame初期化
    pygame.display.set_mode((w, h), 0, 32)  # 画面設定
    screen = pygame.display.get_surface()
    pygame.display.set_caption("5byoudetomete")
    return screen


def on_application_exit():
    pygame.quit()
    sys.exit()


def display_high_score(screen, sysfont, high_scores, score=None):
    # ヘッダー行
    text = sysfont.render("###    High Score    ####", False, (0, 0, 0))
    screen.blit(text, (20, 0))
    # 各scoreの表示
    for i, scores in enumerate(high_scores):
        index = i + 1
        marker = ' ' * 3
        if scores == score:
            marker = '->'
        text = "{0}{1}:{2}".format(marker, index, scores)
        text_render = sysfont.render(text, False, (0, 0, 0))
        screen.blit(text_render, (20, 30 * index))


def main():
    BACKGROUND_COLOR = (255, 255, 255,)# 画面の背景色
    STATUS_BAR = (20, 350)
    screen = initialize()
    # 画面設定　文字
    sysfont = pygame.font.SysFont(None, 40)
    # テキストを描画したSurface作成、画像の作成
    click_start = sysfont.render("click to start", False, (0,0,0))
    count_during = sysfont.render("in measurement", False, (0,0,0))
    tokei = pygame.image.load("tokei.png").convert_alpha()
    rect_tokei = tokei.get_rect()
    rect_tokei.center = (200, 180)
    screen.fill(BACKGROUND_COLOR)
    screen.blit(click_start, STATUS_BAR)
    pygame.display.update()             # 画面更新
    game_state = GameState.START
    high_scores = []
    while True:
        for event in pygame.event.get():
            # 終了用のイベント処理
            if event.type == QUIT:          # 閉じるボタンが押されたとき
                on_application_exit()
                continue
 # マウスクリック1回目の処理(カウント中)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                screen.fill(BACKGROUND_COLOR)  # 画面の背景色
                if game_state == GameState.START:
                    t1 = time.perf_counter()
                    screen.blit(count_during, STATUS_BAR)
                    screen.blit(tokei, rect_tokei)    # 画像の描画
                    game_state = GameState.COUNT_UP #ゲームの状態を「カウントアップ」に変更
 #マウスクリック2回目の処理(結果の出力)
                elif game_state == GameState.COUNT_UP:
                    # 5sec
                    t2 = time.perf_counter()-t1-5
                    score = round(t2, 4)
                    dif = sysfont.render("difference:{0}".format(score), False, (0,0,0))
                    screen.blit(dif, STATUS_BAR)
                    high_scores.append(score)
                    # math.fabsを使って0からの相対的なソートを行う
                    high_scores.sort(key=math.fabs)
                    if len(high_scores) > 5:
                        high_scores.pop() #最大5件に。
                    #ハイスコアの表示
                    display_high_score(screen, sysfont, high_scores, score)

                    game_state = GameState.RESULT #ゲームの状態を「リザルト」に変更
                elif game_state == GameState.RESULT:
                    screen.blit(click_start, STATUS_BAR)
                    game_state = GameState.START #ゲームの状態を「スタート」に変更
                else:
                    assert False, game_state
                pygame.display.update()  # 画面更新
                continue


if __name__ == "__main__":
    main()
