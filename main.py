import pygame
from variables import *
from grid import grid






pygame.init()




screen = pygame.display.set_mode((screen_height,screen_width))
game_grid = grid(screen,screen_width,screen_height,grid_square)

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    

    
    game_grid.split_grid()


    pygame.display.update()

pygame.quit()





"""def grid():
    for column in range(0,screen_width,grid_square):
        for row in range(0,screen_height,grid_square):
            pygame.draw.rect(screen,RED,(column,row,grid_square,grid_square),1)"""

