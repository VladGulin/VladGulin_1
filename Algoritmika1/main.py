from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < height - 80:
            self.rect.y += self.speed

    def update_left(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 80:
            self.rect.y += self.speed


wight = 500
height = 500

window = display.set_mode((wight, height))
window.fill((225, 225, 100))

clock = time.Clock()
FPS = 60

start = True
while start == True:
    for e in event.get():
        if e.type == QUIT:
            start = False
    display.update
    clock.tick(FPS)
