import pygame, sys, random
from button import Button
from objects import Basket, Fruit, Bomb, Health_bar, Explosion, explosion_group
from objects import basket, bomb,fruit , fruit_2,fruit_image , health, new_game
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0, 0, 0)


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

BASKET_WIDTH = 150
BASKET_HEIGHT =100


SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
SCREEN.fill(WHITE)

background = pygame.image.load("images/forest.jpg")
pygame.display.set_caption("Nut hopper")


BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        SCREEN.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if basket.health < 1:
            break
        fruit.hard_mode()
        fruit_2.hard_mode()
        if basket.score > 5:
            bomb.vel = 8
        basket.draw(SCREEN)
        bomb.draw(SCREEN)
        fruit.draw(SCREEN)
        fruit_2.draw(SCREEN) 
        health.draw()
        health.draw_text(SCREEN)
        fruit.draw_text(SCREEN)
        fruit_image.draw_fruit_img()
        fruit.move()
        fruit_2.move()
        bomb.move()
        basket.move(SCREEN_WIDTH)
        explosion_group.draw(SCREEN)
        explosion_group.update()
        fruit.catch_fruit()
        fruit_2.catch_fruit()
        
        bomb.lose_life()
        # print(FramePerSec.get_fps())
        pygame.display.update()
        FramePerSec.tick(FPS)

def lose():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(background, (0,0))

        LOSE_TEXT = get_font(35).render("GAME OVER", True, "Red")
        LOSE_RECT = LOSE_TEXT.get_rect(center=(400//2,100))
        SCREEN.blit(LOSE_TEXT, LOSE_RECT)
        
        SCORE_TEXT = get_font(30).render(f"YOUR SCORE {basket.score}", True, "White")
        SCORE_RECT = LOSE_TEXT.get_rect(center=(400//2,200))
        SCREEN.blit(SCORE_TEXT, SCORE_RECT)
        
        RESTART = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400//2,600-250), 
                            text_input="RESTART", font=get_font(25), base_color="#d7fcd4", hovering_color="White")

        RESTART.changeColor(OPTIONS_MOUSE_POS)
        RESTART.update(SCREEN)
        
        BACK_MENU = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400//2,600-100), 
                            text_input="QUIT", font=get_font(25), base_color="#d7fcd4", hovering_color="White")

        BACK_MENU.changeColor(OPTIONS_MOUSE_POS)
        BACK_MENU.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_MENU.checkForInput(OPTIONS_MOUSE_POS):
                    new_game()
                    main_menu()
                elif RESTART.checkForInput(OPTIONS_MOUSE_POS):
                    new_game()
                    play()
                    
        pygame.display.update()



def main_menu():
    
    while True:
        if basket.health < 4:
            lose()
           
        SCREEN.blit(BG, (0, 0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(40).render("NUT HOPPER", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400//2,100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400//2,600-350), 
                            text_input="PLAY", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400//2,600-200), 
                            text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()