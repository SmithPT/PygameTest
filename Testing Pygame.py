import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    
    res = [750, 600]
    DISPLAY = pygame.display.set_mode((res[0], res[1]), 0, 12)
    pygame.display.set_caption("Test Starting Velocity")
    clock = pygame.time.Clock()

    WHITE = (255,255,255)
    BLACK = (0,0,0)
    BLUE = (0,0,255)

    font = pygame.font.Font('freesansbold.ttf', 36) # Default font, size 36
    text = font.render('Welcome', True, (WHITE))
    textRect = text.get_rect()
    textRect.center = (res[0] // 2, res[1] // 2)



    DISPLAY.fill(BLACK)

    # Adding shapes to the screen
    #pygame.draw.rect(DISPLAY,BLACK,(200,150,400,100))
    #pygame.draw.rect(DISPLAY,BLACK,(170,100,200,200))
    

    # object properties
    #x, y = 100, 100
    pos = [100,100]
    width, height = 20, 20
    
    # testing starting velocity
    #vel = ([5,0])
    vel = 5

    run = True
    while run:
        #pygame.time.delay(100)

        for event in pygame.event.get():
            #DISPLAY.blit(text, textRect)
            if event.type == pygame.QUIT:
                 run = False

        # Get state of all keyboard buttons
        keys = pygame.key.get_pressed()

        # object position based on key presses
        if keys [ pygame.K_LEFT]: #and pos[0] > 0:
            pos[0] -= vel
            DISPLAY.fill(BLACK)
        if keys [ pygame.K_RIGHT]: #and pos[0] < res[0]:
            pos[0] += vel
            DISPLAY.fill(BLACK)
        if keys [ pygame.K_UP]: #and pos[1] > 0:
            pos[1] -= vel
            DISPLAY.fill(BLACK)
        if keys [ pygame.K_DOWN]: #and pos[1] < res[1]:
            pos[1] += vel
            DISPLAY.fill(BLACK)

        # quit game on key press
        if keys [pygame.K_q]:
            run = False

        # Draw the rectangle
        snake = pygame.draw.rect(DISPLAY, (WHITE), (*pos, width, height))
        if pos[0] > 750 or pos[0] < 0 or pos[1] > 500 or pos[1] < 0:
            run = False
        #pygame.
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

main()