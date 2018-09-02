import pygame, sys, random
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption('Hello world!')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

rando1 = random.randint(0, 255)
rando2 = random.randint(0, 255)
rando3 = random.randint(0, 255)
RANDOM_COLOR = (rando1, rando2, rando3)

basicFont = pygame.font.SysFont('Times New Roman', 48, True, True)
basicFont.set_underline(True)

text = basicFont.render('Hello world!', True, WHITE, BLUE)

textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

windowSurface.fill(WHITE)

pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106),
    (236, 277), (56, 277), (0, 106)))

pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

if random.randint(0, 5) > 2:
    pygame.draw.polygon(windowSurface, RANDOM_COLOR, ((250, 400), (500, 200),
        (200, 200), (300, 300), (125, 125), (0, 0) ))
else:
    pygame.draw.polygon(windowSurface, RANDOM_COLOR, ((250, 0), (0, 400),
        (500, 400)))
    pygame.draw.polygon(windowSurface, BLUE, ((250, 400),
        (500, 200), (0, 200)))
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20,
    textRect.width + 40, textRect.height + 40))

pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

windowSurface.blit(text, textRect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
