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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            game_grid.clicked(mouse_x,mouse_y)
     



    game_grid.draw()

    
    


    pygame.display.update()

pygame.quit()




