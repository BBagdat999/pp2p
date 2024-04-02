#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINSCORE = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


pygame.mixer.Sound('Lab8_Racer_background.wav').play()

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, "Yellow", (20, 20), 20)
        self.rect = self.image.get_rect()
        self.rect.center = check_col(E1)
        

    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.kill()
    
    def reset(self):
        self.rect.top = 0
        self.rect.center = check_col(E1)


    


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
#Use it to check if coin center is in enemy
def check_col(enemy):
    x1, y1 = enemy.rect.topleft
    x2, y2 = enemy.rect.bottomright
    while True:
        x, y = (random.randint(20,SCREEN_WIDTH-20), 0)
        if (x < x1 or x > x2):
            return (x, y)
        
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding new User events
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
SPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN, 5000//SPEED)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SPAWN:
            coin = Coin()
            coins.add(coin)
            coin.reset()
            all_sprites.add(coin)

    #Blit scores
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coinscore = font_small.render(str(COINSCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    x, y = coinscore.get_rect().topright
    DISPLAYSURF.blit(coinscore, (SCREEN_WIDTH - x - 10, y + 10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('`7o8Lab8_Racer_crash.wav').play()
        time.sleep(1)
                
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    #Adding +1 to coins score if player collects a coin
    if pygame.sprite.spritecollideany(P1, coins):
        s = pygame.sprite.spritecollide(P1, coins, False)
        for i in s:
            i.kill()
        COINSCORE += 1
            

        
    pygame.display.update()
    FramePerSec.tick(FPS)
pygame.quit()
quit()