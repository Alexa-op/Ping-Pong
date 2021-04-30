from pygame import *
from random import randint
from time import time as timer

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
            self.rect.x += self.speed

window = display.set_mode((700, 500))
display.set_caption("Ping-Pong")
bg = transform.scale(image.load("bg.jpeg"),(700, 550))
rk1 = Player("rk1.png", 20, 275, 5, 50, 50)

clock = time.Clock()


game = True
finish = False
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(bg,(0, -10))
        display.update()
        rk1.update_l()

    clock.tick(30)