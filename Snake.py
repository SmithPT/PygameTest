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

vel = 6

# Snake image
ssize_x = 80
ssize_y = 80
snakepic = pygame.image.load(r"C:\Users\princ\OneDrive\Desktop\Studio stuff\Pygame Test\OIP (2).jpg")
snakepic2 = pygame.transform.scale(snakepic,(ssize_x,ssize_y))
snake = snakepic2.get_rect(center=(res_x / 2, res_y / 2))

def start_screen():
    DISPLAY.fill(WHITE)
    font = pygame.font.SysFont('verdana', 40) # Default font, size 36
    start_button = font.render("Press Spacebar to Start", True, (BLACK))
    #startRect = start_button.get_rect(center = (res_x / 2, res_y / 2))
    DISPLAY.blit(start_button, (res_x/2 - start_button.get_width()/2, res_y / 2 + start_button.get_height()/2))
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
                state = "Playing"

        if state == "Playing":
            DISPLAY.fill(WHITE)
            DISPLAY.blit(snakepic2, snake)
            pygame.display.update()
            # Get state of all keyboard buttons
            keys = pygame.key.get_pressed() 
            
            if keys [ pygame.K_LEFT]: #and pos[0] > 0:
                snake.x -= vel
            
            if keys [ pygame.K_RIGHT]: #and pos[0] < res[0]:
                snake.x += vel
        
            if keys [ pygame.K_UP]: #and pos[1] > 0:
                snake.y -= vel
        
            if keys [ pygame.K_DOWN]: #and pos[1] < res[1]:
                snake.y += vel

            # quit game on key press
            if keys [pygame.K_q]:
                run = False

            # Exit Snake when collides
            if snake.x > 750 or snake.x < 0 or snake.y > 500 or snake.y < 0:
                run = False

            clock.tick(60)

    pygame.quit()
    sys.exit()

main()