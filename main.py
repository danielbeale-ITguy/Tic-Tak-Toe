import pygame
from variables import *
from grid import grid






pygame.init()


screen = pygame.display.set_mode((screen_height,screen_width))
game_grid = grid(screen,screen_width,screen_height,grid_square)


rect1 = pygame.Rect(0,0,50,50)


while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            print(mouse_x,mouse_y)

    
    game_grid.split_grid()



    pygame.draw.rect(screen,rect_color,(rect1))
    
    


    pygame.display.update()

pygame.quit()




