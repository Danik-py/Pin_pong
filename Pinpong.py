from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пинпог')
back = (212, 11, 202)
window.fill(back)
clock = time.Clock()

mixer.init()
mixer.music.load('Shuter/GucciMogucci_-_BAN_Prod_by_Just_Overboard_73000380.mp3')
mixer.music.play()
mixer.music.set_volume(0.1)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed =key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed =key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

raket_1 = Player('Shuter/racket.png', 20, 170, 5, 50, 150)
raket_2 = Player('Shuter/racket.png', 630, 170, 5, 50, 150)
ball = GameSprite('Shuter/tenis_ball.png', 250, 250, 2, 50, 50)
font.init()
font_1 = font.Font(None, 35)
lose_1 = font_1.render('The LOSER', True, (180, 0, 0))
lose_2 = font_1.render('The LOSER', True, (180, 0, 0))
speed_x = 3
speed_y = 3
finish = False
game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        ball.reset()
        raket_1.update_l()
        raket_1.reset()
        raket_2.update_r()
        raket_2.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(raket_1, ball) or sprite.collide_rect(raket_2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose_1, (200, 200))
        window.blit(lose_2, (200, 200))
        
    display.update()
    clock.tick(40)