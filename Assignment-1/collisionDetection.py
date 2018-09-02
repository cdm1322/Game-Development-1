import pygame, sys, random, os
from pygame.locals import *
# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()
# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),
    0, 32)
pygame.display.set_caption('Collision Detection - PRESS "R" FOR FUN MODE')
# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
# Set up the player and food data structures.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),
         random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
# Set up movement variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 6

#testing
astleyMode = False
astleyMusic = pygame.mixer.music
astleyMusic.load(os.path.abspath("astley.mp3"))
background = pygame.Surface(windowSurface.get_size())
background = background.convert()
background.fill((250, 250, 250))
backgroundRect = pygame.Rect((0,0), (WINDOWWIDTH, WINDOWHEIGHT))
backgroundImage = pygame.image.load(os.path.abspath("rick.jpg"))
backgroundImage = pygame.transform.scale(backgroundImage, backgroundRect.size)
backgroundImage = backgroundImage.convert()

background.blit(backgroundImage, backgroundRect)

# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_t:
                player.top = random.randint(0, WINDOWHEIGHT -
                    player.height)
                player.left = random.randint(0, WINDOWWIDTH -
                    player.width)
            if event.key == K_r:
                if astleyMode:
                    astleyMusic.stop()
                    astleyMode = False
                else:
                    astleyMusic.play(-1, 0)
                    astleyMode = True
        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1],
                 FOODSIZE, FOODSIZE))

        foodCounter += 1
        if foodCounter >= NEWFOOD:
            # Add new food.
            foodCounter = 0
            foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH -
             FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE),
             FOODSIZE, FOODSIZE))

     # Draw the white background onto the surface.
        if astleyMode:
            windowSurface.blit(backgroundImage,(0,0))
        else:
            windowSurface.fill(WHITE)

     # Move the player.
        if moveDown and player.bottom < WINDOWHEIGHT:
            player.top += MOVESPEED
        if moveUp and player.top > 0:
            player.top -= MOVESPEED
        if moveLeft and player.left > 0:
            player.left -= MOVESPEED
        if moveRight and player.right < WINDOWWIDTH:
            player.right += MOVESPEED

     # Draw the player onto the surface.
        pygame.draw.rect(windowSurface, BLACK, player)

     # Check whether the player has intersected with any food squares.
        for food in foods[:]:
            if player.colliderect(food):
                foods.remove(food)

     # Draw the food.
        for i in range(len(foods)):
            pygame.draw.rect(windowSurface, GREEN, foods[i])

     # Draw the window onto the screen.
        pygame.display.update()
        mainClock.tick(40)
