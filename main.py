import pygame
from variables import *
from grid import grid




def main():

    pygame.init()


    screen = pygame.display.set_mode((screen_height,screen_width))
    game_grid = grid(screen,screen_width,screen_height,grid_square)
    #TEST IMAGE LOADING




    while True:
        game = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        
    #       CURRENT GRID GAME LOOP FOR DRAWING SQAURE AND CHECKING
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                game_grid.clicked(mouse_x,mouse_y)

            elif event.type == pygame.MOUSEBUTTONUP:
                game = game_grid.check_win()
                if game == True:
                    main()

        game_grid.draw()










        
        pygame.display.update()

    pygame.quit()


main()
"""
    rect = cross.get_rect()
    pygame.draw.rect(screen,RED,rect,1)
    

    screen.fill(WHITE)
    screen.blit(cross,rect)
    pygame.draw.rect(screen,RED,rect,1)"""
