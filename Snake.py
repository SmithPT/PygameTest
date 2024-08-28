import pygame, sys
from pygame.locals import *

pygame.init()

res_x = 800
res_y = 800
DISPLAY = pygame.display.set_mode((res_x, res_y), 0,12)
pygame.display.set_caption("Scuffed ass snake")
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)

# Snake image
ssize_x = 80
ssize_y = 80
snakepic = pygame.image.load(r"C:\Users\princ\OneDrive\Desktop\Studio stuff\Pygame Test\OIP (2).jpg")
snakepic2 = pygame.transform.scale(snakepic,(ssize_x,ssize_y))
snake = snakepic2.get_rect(center=(res_x / 2, res_y / 2))

snake_rotateD1 = pygame.transform.rotate(snakepic, 270)
snakeSD1 = pygame.transform.scale(snake_rotateD1,(ssize_x,ssize_y))
snakeSRD1 = snakeSD1.get_rect(center=(res_x / 2, res_y / 2))

snake_rotateL1 = pygame.transform.rotate(snakepic, 180)
snakeSL1 = pygame.transform.scale(snake_rotateL1,(ssize_x,ssize_y))
snakeSRL1 = snakeSL1.get_rect(center=(res_x / 2, res_y / 2))

snake_rotateU1 = pygame.transform.rotate(snakepic, 90)
snakeSU1 = pygame.transform.scale(snake_rotateU1,(ssize_x,ssize_y))
snakeSRU1 = snakeSU1.get_rect(center=(res_x / 2, res_y / 2))

vel = 6
class Players:
    vel = 6

    def moveRight(self):
        snake.x += vel
        snakeSRL1.x += vel
        snakeSRU1.x += vel
        snakeSRD1.x += vel
        DISPLAY.fill(WHITE)
        DISPLAY.blit(snakepic2, snake)
        pygame.display.update()

    def moveLeft(self):
        snake.x -= vel
        snakeSRL1.x -= vel
        snakeSRU1.x -= vel
        snakeSRD1.x -= vel
        DISPLAY.fill(WHITE)
        DISPLAY.blit(snakeSL1, snakeSRL1)
        pygame.display.update()

    def moveUp(self):
        snake.y -= vel
        snakeSRL1.y -= vel
        snakeSRU1.y -= vel
        snakeSRD1.y -= vel
        DISPLAY.fill(WHITE)
        DISPLAY.blit(snakeSU1, snakeSRU1)
        pygame.display.update()

    def moveDown(self):
        snake.y += vel
        snakeSRL1.y += vel
        snakeSRU1.y += vel
        snakeSRD1.y += vel
        DISPLAY.fill(WHITE)
        DISPLAY.blit(snakeSD1, snakeSRD1)
        pygame.display.update()

# Obstacle
# Obx = 80
# Oby = 80
# Ob_wid = 80
# Ob_Hei = 80

def start_screen():
    DISPLAY.fill(WHITE)
    SBfont = pygame.font.SysFont('verdana', 40) # Default font, size 36
    start_button = SBfont.render("Press Spacebar to Start", True, (BLACK))
    DISPLAY.blit(start_button, (res_x/2 - start_button.get_width()/2, res_y / 2 + start_button.get_height()/2))
    pygame.display.update()

def game_over_screen():
    DISPLAY.fill(BLACK)
    GOfont = pygame.font.SysFont('verdana', 40)
    GO_button = GOfont.render("You're dead G", True, (WHITE))
    DISPLAY.blit(GO_button, (res_x/2 - GO_button.get_width()/2, res_y / 2 + GO_button.get_height()/2))
    pygame.display.update()

def main():
    run = True
    state = "Menu"
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 run = False

        if state == "Menu":
            start_screen()
            keys = pygame.key.get_pressed() 
            if keys[pygame.K_SPACE]:
                DISPLAY.blit(snakepic2, snake)
                state = "Playing"
                game_over = False

        elif state == "game_over":
            game_over_screen()
            keys = pygame.key.get_pressed() 
            if keys[pygame.K_r]:
                state = "Menu"
            if keys[pygame.K_q]:
                pygame.quit()
                quit()

        elif state == "Playing":
            pygame.display.update()
            keys = pygame.key.get_pressed()

            if keys [ pygame.K_LEFT]: 
                Players.moveLeft(Players)

            if keys [ pygame.K_RIGHT]: 
                Players.moveRight(Players)

            if keys [ pygame.K_UP]: 
                Players.moveUp(Players)

            if keys [ pygame.K_DOWN]:
                Players.moveDown(Players)

            if keys [pygame.K_q]:
                run = False
            if snake.x > res_x or snake.x < 0 or snake.y > res_y or snake.y < 0:
                game_over = True
                state = "game_over"
        
            clock.tick(60)

        elif game_over:
            state = "game_over"
            game_over = "False"

    pygame.quit()
    sys.exit()

main()