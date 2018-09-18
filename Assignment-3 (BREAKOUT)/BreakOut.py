"""
 bricka (a breakout clone)
 Developed by Leonel Machava <leonelmachava@gmail.com>

 http://codeNtronix.com

 editted by Cody Martin
"""
import sys
import pygame
from pygame.locals import *
import random

SCREEN_SIZE   = 1280,960

# Object dimensions
BRICK_WIDTH   = 120
BRICK_HEIGHT  = 30
PADDLE_WIDTH  = 120
PADDLE_HEIGHT = 24
BALL_DIAMETER = 32
BALL_RADIUS   = int(int(BALL_DIAMETER) / int(2))

MAX_PADDLE_X = SCREEN_SIZE[0] - PADDLE_WIDTH
MAX_BALL_X   = SCREEN_SIZE[0] - BALL_DIAMETER
MAX_BALL_Y   = SCREEN_SIZE[1] - BALL_DIAMETER

# Paddle Y coordinate
PADDLE_Y = SCREEN_SIZE[1] - PADDLE_HEIGHT - 10

# Color constants
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE  = (0,0,255)
BRICK_COLOR = (200,200,0)

# State constants
STATE_BALL_IN_PADDLE = 0
STATE_PLAYING = 1
STATE_WON = 2
STATE_GAME_OVER = 3

# Graphic Assets
# Unbroken Bricks
TILE1 = pygame.image.load("PNG/tile1-1.png")
TILE2 = pygame.image.load("PNG/tile2-1.png")
TILE3 = pygame.image.load("PNG/tile3-1.png")
TILE4 = pygame.image.load("PNG/tile4-1.png")
TILE5 = pygame.image.load("PNG/tile5-1.png")
TILE6 = pygame.image.load("PNG/tile6-1.png")
TILE7 = pygame.image.load("PNG/tile7-1.png")
TILE8 = pygame.image.load("PNG/tile8-1.png")
TILE9 = pygame.image.load("PNG/tile9-1.png")
TILE10 = pygame.image.load("PNG/tile10-1.png")

# Broken Bricks
BROKEN1 = pygame.image.load("PNG/tile1-2.png")
BROKEN2 = pygame.image.load("PNG/tile2-2.png")
BROKEN3 = pygame.image.load("PNG/tile3-2.png")
BROKEN4 = pygame.image.load("PNG/tile4-2.png")
BROKEN5 = pygame.image.load("PNG/tile5-2.png")
BROKEN6 = pygame.image.load("PNG/tile6-2.png")
BROKEN7 = pygame.image.load("PNG/tile7-2.png")
BROKEN8 = pygame.image.load("PNG/tile8-2.png")
BROKEN9 = pygame.image.load("PNG/tile9-2.png")
BROKEN10 = pygame.image.load("PNG/tile10-2.png")

# Ball and Paddle
BALL_GFX = pygame.image.load("PNG/ball.png")
PADDLE_GFX = pygame.image.load("PNG/paddle_default.png")

class Bricka:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)


        pygame.display.set_caption("bricka (a breakout clone by codeNtronix.com)")

        self.clock = pygame.time.Clock()

        if pygame.font:
            self.font = pygame.font.Font(None,30)
        else:
            self.font = None

        self.init_game()

    def init_game(self):
        self.lives = 3
        self.score = 0
        self.state = STATE_BALL_IN_PADDLE

        self.paddle = {
            'rect' : pygame.Rect(300,PADDLE_Y,PADDLE_WIDTH,PADDLE_HEIGHT),
            'surface' : pygame.transform.scale(PADDLE_GFX, (PADDLE_WIDTH, PADDLE_HEIGHT))
        }

        self.ball = {
            'rect' : pygame.Rect(300,PADDLE_Y - BALL_DIAMETER,BALL_DIAMETER,BALL_DIAMETER),
            'surface' : pygame.transform.scale(BALL_GFX, (BALL_DIAMETER, BALL_DIAMETER))
        }


        self.ball_vel = [10,-10]

        self.create_bricks()


    def create_bricks(self):
        y_ofs = 35
        self.bricks = []
        for i in range(7):
            x_ofs = 35
            for j in range(9):
                brick_number = random.randint(1,10)
                brick = {
                    'number' : brick_number,
                    'rect' : pygame.Rect(x_ofs,y_ofs,BRICK_WIDTH,BRICK_HEIGHT),
                    'surface' : self.get_brick_surface(brick_number),
                    'broken' : False
                }
                self.bricks.append(brick)
                x_ofs += BRICK_WIDTH + 10
            y_ofs += BRICK_HEIGHT + 5

    def get_brick_surface(self, number):
        if number == 1:
            return pygame.transform.scale(TILE1, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 2:
            return pygame.transform.scale(TILE2, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 3:
            return pygame.transform.scale(TILE3, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 4:
            return pygame.transform.scale(TILE4, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 5:
            return pygame.transform.scale(TILE5, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 6:
            return pygame.transform.scale(TILE6, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 7:
            return pygame.transform.scale(TILE7, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 8:
            return pygame.transform.scale(TILE8, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 9:
            return pygame.transform.scale(TILE9, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 10:
            return pygame.transform.scale(TILE10, (BRICK_WIDTH, BRICK_HEIGHT))

    def break_brick_surface(self, number):
        if number == 1:
            return pygame.transform.scale(BROKEN1, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 2:
            return pygame.transform.scale(BROKEN2, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 3:
            return pygame.transform.scale(BROKEN3, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 4:
            return pygame.transform.scale(BROKEN4, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 5:
            return pygame.transform.scale(BROKEN5, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 6:
            return pygame.transform.scale(BROKEN6, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 7:
            return pygame.transform.scale(BROKEN7, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 8:
            return pygame.transform.scale(BROKEN8, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 9:
            return pygame.transform.scale(BROKEN9, (BRICK_WIDTH, BRICK_HEIGHT))
        if number == 10:
            return pygame.transform.scale(BROKEN10, (BRICK_WIDTH, BRICK_HEIGHT))

    def draw_bricks(self):
        for brick in self.bricks:
            self.screen.blit(brick['surface'], brick['rect'])

    def check_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.paddle['rect'].left -= 5
            if self.paddle['rect'].left < 0:
                self.paddle['rect'].left = 0

        if keys[pygame.K_RIGHT]:
            self.paddle['rect'].left += 5
            if self.paddle['rect'].left > MAX_PADDLE_X:
                self.paddle['rect'].left = MAX_PADDLE_X

        if keys[pygame.K_SPACE] and self.state == STATE_BALL_IN_PADDLE:
            self.ball_vel = [5,-5]
            self.state = STATE_PLAYING

        elif keys[pygame.K_RETURN] and (self.state == STATE_GAME_OVER or self.state == STATE_WON):
            self.init_game()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP and self.state == STATE_BALL_IN_PADDLE:
                self.ball_vel = [5, -5]
                self.state = STATE_PLAYING
            elif event.type == MOUSEBUTTONUP and (self.state == STATE_GAME_OVER or self.state == STATE_WON):
                self.init_game()
            elif event.type == MOUSEMOTION:
                self.paddle['rect'].centerx = event.pos[0]
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()



    def move_ball(self):
        self.ball['rect'].left += self.ball_vel[0]
        self.ball['rect'].top  += self.ball_vel[1]

        if self.ball['rect'].left <= 0:
            self.ball['rect'].left = 0
            self.ball_vel[0] = -self.ball_vel[0]
        elif self.ball['rect'].left >= MAX_BALL_X:
            self.ball['rect'].left = MAX_BALL_X
            self.ball_vel[0] = -self.ball_vel[0]

        if self.ball['rect'].top < 0:
            self.ball['rect'].top = 0
            self.ball_vel[1] = -self.ball_vel[1]
        elif self.ball['rect'].top >= MAX_BALL_Y:
            self.ball['rect'].top = MAX_BALL_Y
            self.ball_vel[1] = -self.ball_vel[1]

    def handle_collisions(self):
        for brick in self.bricks:
            if self.ball['rect'].colliderect(brick['rect']) and brick['broken'] is True:
                self.score += 3
                self.ball_vel[1] = -self.ball_vel[1]
                self.bricks.remove(brick)
                break
            elif self.ball['rect'].colliderect(brick['rect']) and brick['broken'] is False:
                brick['surface'] = self.break_brick_surface(brick['number'])
                brick['broken'] = True
                self.ball_vel[1] = -self.ball_vel[1]
                break

        if len(self.bricks) == 0:
            self.state = STATE_WON

        if self.ball['rect'].colliderect(self.paddle['rect']):
            self.ball['rect'].top = PADDLE_Y - BALL_DIAMETER
            self.ball_vel[1] = -self.ball_vel[1]
        elif self.ball['rect'].top > self.paddle['rect'].top:
            self.lives -= 1
            if self.lives > 0:
                self.state = STATE_BALL_IN_PADDLE
            else:
                self.state = STATE_GAME_OVER

    def show_stats(self):
        if self.font:
            font_surface = self.font.render("SCORE: " + str(self.score) + " LIVES: " + str(self.lives), False, WHITE)
            self.screen.blit(font_surface, (205,5))

    def show_message(self,message):
        if self.font:
            size = self.font.size(message)
            font_surface = self.font.render(message,False, WHITE)
            x = (SCREEN_SIZE[0] - size[0]) / 2
            y = (SCREEN_SIZE[1] - size[1]) / 2
            self.screen.blit(font_surface, (x,y))

    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit

            self.clock.tick(50)
            self.screen.fill(BLACK)
            self.check_input()

            if self.state == STATE_PLAYING:
                self.move_ball()
                self.handle_collisions()
            elif self.state == STATE_BALL_IN_PADDLE:
                self.ball['rect'].left = self.paddle['rect'].left + self.paddle['rect'].width / 2
                self.ball['rect'].top  = self.paddle['rect'].top - self.ball['rect'].height
                self.show_message("PRESS SPACE TO LAUNCH THE BALL")
            elif self.state == STATE_GAME_OVER:
                self.show_message("GAME OVER. PRESS ENTER TO PLAY AGAIN")
            elif self.state == STATE_WON:
                self.show_message("YOU WON! PRESS ENTER TO PLAY AGAIN")

            self.draw_bricks()

            # Draw paddle
            self.screen.blit(self.paddle['surface'], self.paddle['rect'])

            # Draw ball
            self.screen.blit(self.ball['surface'], self.ball['rect'])

            self.show_stats()

            pygame.display.flip()

if __name__ == "__main__":
    Bricka().run()
