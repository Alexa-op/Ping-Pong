from pygame import *
from random import randint
from time import time as timer

h = 600
w = 700
speed_x = 3
speed_y = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.size_x = size_x
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y < 545:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y < 545:
            self.rect.y += self.speed

window = display.set_mode((w, h))
display.set_caption("Ping-Pong")
bg = transform.scale(image.load("bg.jpeg"),(w, h))
rk1 = Player("rk1.png", 20, 275, 7, 100, 100)
rk2 = Player("rk2.png", 600, 275, 7, 100, 100)
ball = Player("ball.png", 350, 275, 3, 50, 50)

clock = time.Clock()


game = True
finish = False
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > h-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(rk1, ball) or sprite.collide_rect(rk2, ball):
            speed_x *= -1


        window.blit(bg,(0, 0))

        ball.reset()
        rk1.reset()
        rk2.reset()

        rk1.update_l()
        rk2.update_r()

        display.update()

    clock.tick(30)
