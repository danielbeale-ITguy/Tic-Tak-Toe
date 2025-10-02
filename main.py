import pygame
from variables import *
from grid import grid





def main():

    pygame.init()

    
    
    screen = pygame.display.set_mode((screen_height,screen_width))
    game_grid = grid(screen,screen_half,screen_half,grid_square)

    turn_display = (475,75,150,150)
    turn_display_cross = pygame.image.load('cross.png')
    turn_display_nought = pygame.image.load('nought.png')
    screen.blit(turn_display_cross,turn_display)
    #TEST IMAGE LOADING

    screen.fill(WHITE)

    while True:
        game = True
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()

        
    #       CURRENT GRID GAME LOOP FOR DRAWING SQAURE AND CHECKING
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                game_grid.clicked(mouse_x,mouse_y)
                screen.fill(WHITE)
            elif event.type == pygame.MOUSEBUTTONUP:
                game = game_grid.check_win()
                display = game_grid.turn_display()
                if game == True:
                    main()



                if display == True:
                    screen.blit(turn_display_cross,turn_display)
                    pygame.display.flip()
                else:
                    screen.blit(turn_display_nought,turn_display)
                    pygame.display.update()


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
