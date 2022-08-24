# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame

FRAME_REFRESH_RATE = 30
WHITE = (0, 0, 255)
BACKGROUD = (255, 255, 255) # White
WIDTH = 10
HEIGHT = 10

def main():

    print("PyGame")
    pygame.init() # PyGame application
    print('Box Game')
    
    #size of the screen.
    screen = pygame.display.set_mode((1355, 1000))
    pygame.display.set_caption('Draw with Boxes')
    print('Update display')
    pygame.display.update()
    print('Setup the Clock')
    clock = pygame.time.Clock()

    print('Game Loop')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Quit Event:', event)
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Mouse Event', event)
                x, y = event.pos
                pygame.draw.rect(screen, WHITE, [x, y,WIDTH, HEIGHT])

        # Update the display
        pygame.display.update()
        
        # Frame 
        clock.tick(FRAME_REFRESH_RATE)
    print('Game Over')
    # Quit pygame
    pygame.quit()


if __name__ == '__main__':
    main()
