"""
Docstring
"""

import sys
import random
import pygame


pygame.init()

size = width, height = 800, 800
screen = pygame.display.set_mode(size)
speed = [0, 0]

background = pygame.image.load("./space_background.png")
background = pygame.transform.scale(background, (800, 800))
bg_y_pos = 0
bg_2_y_pos = background.get_height()

ticks_since_last_enemy = 0
time_to_next_enemy = 1000
main_clock = pygame.time.Clock()
score = 0
is_game_running = True

class MainCharacter(pygame.sprite.Sprite):
    """
    Holds data for the player character of the game
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # image
        # rect
        self.image = pygame.image.load("./spaceship.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.center = (250, 250)
        self.totalLives = 5
        self.lastHit = 0
    def update(self):
        """
        Updates object following a collision
        """
        self.lastHit = pygame.time.get_ticks()
        self.totalLives -= 1

        if (self.totalLives <= 0):
            is_game_running = False

class BadGuy(pygame.sprite.Sprite):
    """
    Holds data for the enemy non-player-characters of the game
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./ufo.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        enemy_type = random.randint(1, 5)
        self.badSpeed = [0, 0]
        self.rect.center = (0, 0)
        # Randomly generate enemy from a few pattern types
        if enemy_type == 1:
            self.badSpeed = [0, 4]
            self.rect.center = (random.randint(0, width), 0)
        elif enemy_type == 2:
            self.badSpeed = [3, 3]
            self.rect.center = (0, random.randint(0, height/2))
        elif enemy_type == 3:
            self.badSpeed = [-3, 3]
            self.rect.center = (width, random.randint(0, height/2))
        elif enemy_type == 4:
            self.badSpeed = [4, 0]
            self.rect.center = (0, random.randint(height / 4, 3 * height / 4))
        elif enemy_type == 5:
            self.badSpeed = [-4, 0]
            self.rect.center = (width, random.randint(height / 4, 3 * height / 4))
    def update(self):
        """
        Updates object every tick
        """
        self.rect = self.rect.move(self.badSpeed)

        # If they get below the bototm of the screen, despawn
        if self.rect.top > height:
            self.remove(badSprites)

        # Slow down BadGuy if their speed is too high
        if self.badSpeed[0] > 6:
            self.badSpeed[0] -= 0.5
        if self.badSpeed[0] < -6:
            self.badSpeed[0] += 0.5

        if self.badSpeed[1] > 6:
            self.badSpeed[1] -= 0.5
        if self.badSpeed[1] < -6:
            self.badSpeed[1] += 0.5

main = MainCharacter()

main_sprite = pygame.sprite.Group()
main_sprite.add(main)

badSprites = pygame.sprite.Group()

clock = pygame.time.Clock()
# The game loop
while is_game_running:
    # tick rate is 60 fps
    clock.tick(60)
    
    ticks_since_last_enemy += main_clock.tick()
    
    if ticks_since_last_enemy >= time_to_next_enemy:
        score += ticks_since_last_enemy
        ticks_since_last_enemy = 0
        badSprites.add(BadGuy())
        time_to_next_enemy = max(time_to_next_enemy - 10, 100)

    bg_y_pos -= 5
    bg_2_y_pos -= 5

    if bg_y_pos < -1 * background.get_height():
        bg_y_pos = background.get_height()
    if bg_2_y_pos < -1 * background.get_height():
        bg_2_y_pos = background.get_height()

    key = pygame.key.get_pressed()

    # Speed up in direction of key press
    if (key[pygame.K_a]):
        if (speed[0] > -20):
            speed[0] -= 1.5
    if (key[pygame.K_d]):
        if (speed[0] < 20):
            speed[0] += 1.5
    if (key[pygame.K_w]):
        if (speed[1] > -20):
            speed[1] -= 1.5
    if (key[pygame.K_s]):
         if (speed[1] < 20):
            speed[1] += 1.5

    # Slow down when key is not pressed
    if (speed[0] > 0):
        speed[0] -= 0.5
    elif (speed[0] < 0):
        speed[0] += 0.5

    if (speed[1] > 0):
        speed[1] -= 0.5
    elif (speed[1] < 0):
        speed[1] += 0.5

    # Stop when colliding with boundaries
    if main.rect.left < 0 or main.rect.right > width:
        speed[0] = -speed[0] * 1.5
    if main.rect.top < 0 or main.rect.bottom > height:
        speed[1] = -speed[1] * 1.5

    # update positions of MainCharacter and BadGuy objects
    main.rect = main.rect.move(speed)
    badSprites.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    collisions = pygame.sprite.spritecollideany(main, badSprites)
    if (collisions is not None):
        if (pygame.time.get_ticks() - main.lastHit > 1000):
            main_sprite.update()


    # Draw background
    screen.blit(background, (0, bg_y_pos))
    screen.blit(background, (0, bg_2_y_pos))
    # Draw sprites
    main_sprite.draw(screen)
    badSprites.draw(screen)

    # Write UI text for life count
    myFont = pygame.font.SysFont("Times New Roman", 18)
    numLivesDraw = myFont.render("Lives: " + str(main.totalLives), 1, (250, 250, 250))
    scoreText = myFont.render("Score: " + str(score), 1, (250, 250, 250))
    screen.blit(numLivesDraw, (30, 30))
    screen.blit(scoreText, (100, 30))

    pygame.display.flip()

# Display score after game loop ends
screen.