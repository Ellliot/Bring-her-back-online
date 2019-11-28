'''
Created on 2019年2月24日

@author: Fred
'''

import random
import arcade
import os
from supercollider import Server, Synth

SPRITE_SCALING_PLAYER = 0.07
SPRITE_SCALING_COIN = 0.3
COIN_COUNT = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "pinball"

MOVEMENT_SPEED = 5
BallVel= 1
x = 0

def Ask():
    i = input("Choose among the genres below:\n 1:Nature\n 2:Weird Gibberish\n 3:Voices\n 4:World Music\n 5:Chef's Special\n")
    f ="sound"
    if i == "1":
        f = "nature"
    elif i == "2":
        f = "weird"
    elif i == "3":
        f = "voices"
    elif i == "4" :
        f = "world"
    elif i == "5" :
        f ="special"
    return f
    
       
class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1



class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0
        self.vel = BallVel
        self.sound=arcade.load_sound(f + "/" +s[x])

    def changeSound(self):
        x = random.randrange(0,len(s)-1)
        self.sound = arcade.load_sound(f+ "/" +s[x])

        
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0:
            self.change_x *= -self.vel

        if self.right > SCREEN_WIDTH:
            self.change_x *= -self.vel

        if self.bottom < 0:
            self.change_y *= -self.vel

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -self.vel


class MyGame(arcade.Window):


    def __init__(self):
        """ Initializer """

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.all_sprites_list = None
        self.coin_list = None
        self.player_sprite = None
        self.score = 0
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.all_sprites_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = arcade.Sprite("platform.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 300
        self.all_sprites_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            coin = Coin("ball.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)
            self.all_sprites_list.append(coin)
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()


    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        self.all_sprites_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list)

        for coin in hit_list:
            if coin.change_y > 0:
                coin.top = self.player_sprite.bottom
            elif coin.change_y < 0:
                coin.bottom = self.player_sprite.top
        if len(hit_list) > 0:
                coin.change_x *= -coin.vel
                coin.change_y *= -coin.vel
                synth = Synth(server, "sine", { "freq" : rand(440,800) , "gain" : -18.0 })


                            

def main():
    print(s)
    window = MyGame()
    window.setup()
    arcade.run()
    server = Server()


if __name__ == "__main__":
    f = Ask()
    s = os.listdir(f)
    main()
