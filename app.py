import pygame
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0, 0, 0)


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

PADDLE_WIDTH = 150
PADDLE_HEIGHT =100


WINDOW = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
WINDOW.fill(WHITE)

background = pygame.image.load("images/forest.jpg")
pygame.display.set_caption("Nut hopper")

class Basket():
    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.color = WHITE
        self.image = pygame.image.load("images/basket.png")
        self.health = 5
        self.score = 0
    def move(self,SCREEN_WIDTH):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.x - self.vel <= SCREEN_WIDTH - PADDLE_WIDTH :
            self.x += self.vel
        if keys[pygame.K_LEFT] and self.x - self.vel >= 0:
            self.x -= self.vel
    def draw(self,WINDOW):
         WINDOW.blit(pygame.transform.scale(self.image, (self.width,self.height)), (self.x, self.y))

class Fruit(Basket):
    
    def __init__(self,y,width,height):
        self.x = random.randrange(0,350)
        self.img_cor = 70
        self.y = y
        self.width =width
        self.height =height
        self.color = WHITE
        self.image = pygame.image.load("images/nut.png")
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.vel = 3
        
    def draw(self,WINDOW):
        WINDOW.blit(pygame.transform.scale(self.image, (self.width,self.height)), (self.x, self.y))
        
    def move(self):
        self.y += self.vel
        if self.y > SCREEN_HEIGHT:  
                  
            self.x = random.randrange(0,350)
            self.y = 0
    def draw_fruit_img(self):
        WINDOW.blit(pygame.transform.scale(self.image, (self.width,self.height)), (self.img_cor, self.y))
    def draw_text(self,WINDOW):
        text = self.font.render(f'x{basket.score}', True, (255,255,255))
        textRect = text.get_rect()
        textRect.topleft = (100,0)
        WINDOW.blit(text, textRect)
    # Collision of fruit   
    def catch_fruit(self):    
        if((SCREEN_HEIGHT - PADDLE_HEIGHT - 10) - 30) < self.y < (SCREEN_HEIGHT - PADDLE_HEIGHT - 10) and basket.x < self.x < basket.x + PADDLE_WIDTH - 60:    
            basket.score +=1 
            self.x = random.randrange(0,350)
            self.y = 0
        

class Bomb:
    
    def __init__(self,y,width,height):
        self.x = random.randrange(0,350)
        self.y = y
        self.width =width
        self.height =height
        self.color = WHITE
        self.image = pygame.image.load("images/bomb.png")
        self.vel = 3
    def draw(self,WINDOW):
        WINDOW.blit(pygame.transform.scale(self.image, (self.width,self.height)), (self.x, self.y))
        
    def move(self):
        self.y += self.vel
        if self.y > SCREEN_HEIGHT:         
            self.x = random.randrange(0,350)
            self.y = 0
# Collision of bomb    
    def lose_life(self):    
        if((SCREEN_HEIGHT - PADDLE_HEIGHT - 10) - 30) < bomb.y < (SCREEN_HEIGHT - PADDLE_HEIGHT - 10) and basket.x < self.x < basket.x + PADDLE_WIDTH - 60:    
            basket.health -=1
            self.x = random.randrange(0,350)
            self.y = 0

class Heath_bar(Basket):
    
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load("images/health.png")
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        
    def draw(self):
        WINDOW.blit(pygame.transform.scale(self.image, (self.width,self.height)), (self.x, self.y))
                
    def draw_text(self,WINDOW):
        text = self.font.render(f'x{basket.health}', True, (255,255,255))
        textRect = text.get_rect()
        textRect.topleft = (30,0)
        WINDOW.blit(text, textRect)
        
basket = Basket(SCREEN_WIDTH//2 - PADDLE_WIDTH//2 ,SCREEN_HEIGHT - PADDLE_HEIGHT - 10,PADDLE_WIDTH,PADDLE_HEIGHT)
fruit = Fruit(0,50,50)
fruit_2 = Fruit(0,50,50)
fruit_image = Fruit(0,30,30)
bomb = Bomb(0,50,50)
health = Heath_bar(0,0,30,30)
run = True

while run:
    
    WINDOW.fill(WHITE)
    WINDOW.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        elif basket.health < 1:
            run = False
            break
    basket.draw(WINDOW)
    bomb.draw(WINDOW)
    fruit.draw(WINDOW)
    fruit_2.draw(WINDOW) 
    health.draw()
    health.draw_text(WINDOW)
    fruit.draw_text(WINDOW)
    fruit_image.draw_fruit_img()
    fruit.move()
    fruit_2.move()
    bomb.move()
    basket.move(SCREEN_WIDTH)
    
    fruit.catch_fruit()
    fruit_2.catch_fruit()
    
    bomb.lose_life()
    # print(FramePerSec.get_fps())
    pygame.display.update()
    FramePerSec.tick(FPS)
