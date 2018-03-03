# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

SCREEN = Rect(0, 0, 700, 500)

pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Shooting")


#自機と敵機
class Flyer(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, vx, vy):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(filename).convert_alpha()
        w = self.image.get_width()
        h = self.image.get_height()
        self.rect = Rect(x, y, w, h)
        self.vx = vx
        self.vy = vy

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Player(Flyer):
    def __init__(self, filename, x, y, vx, vy):
        super().__init__(filename, x, y, vx, vy)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            self.rect.move_ip(-self.vx, 0)
        if pressed_key[K_RIGHT]:
            self.rect.move_ip(self.vx, 0)
        if pressed_key[K_UP]:
            self.rect.move_ip(0, -self.vy)
        if pressed_key[K_DOWN]:
            self.rect.move_ip(0, self.vy)
        if self.y < -30 or self.y > 500 or self.x < -30 or self.x > 700:
            pygame.sprite.Sprite.remove(self)

    def shoot(self, screen): #弾発射
        class Bullet(object):
            def __init__(self, x: int, y: int):
                self.bullet = Rect(x, y, 20, 20)

            def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), self.bullet)

            def move(self, x: int=0, y: int=-5):
                self.bullet.move_ip(x, y)

            @property
            def is_destroy(self) -> bool:
                if self.bullet.x < 0 or self.bullet.y < 0:
                    return True
                return False

        # 自機の位置が移動しても発射位置が追従するようにself.x/self.y ではなく self.rectを使用
        return Bullet(self.rect.x, self.rect.y)


class Enemy(Flyer):
    def __init__(self, filename, x, y, vx, vy):
        super().__init__(filename, x, y, vx, vy)

    def move(self):
        self.rect.move_ip(self.vx, self.vy)
        self.rect = self.rect.clamp(SCREEN)

#メイン
def main():
    player = Player("player.jpg", 350, 400, 5, 5)
    enemy1 = Enemy("enemy.jpg", 100, 100, 5, 0)
    clock = pygame.time.Clock()
    bullet_list = []

    while 1:
        clock.tick(30)
        screen.fill((0, 0, 0))

        player.move()
        enemy1.move()
        player.draw(screen)
        enemy1.draw(screen)
        for bullet in bullet_list:
            bullet.move()
            bullet.draw()
        #リストからスクリーン範囲外のbulletをクリーンアップ
        bullet_list = list(filter(lambda x: not x.is_destroy, bullet_list))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    # 発射時にbullet_listに追加
                    bullet_list.append(player.shoot(screen))
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main()
