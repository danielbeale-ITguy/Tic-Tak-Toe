import pygame

RED = (255,0,0)

screen_height = 300
screen_width = 300


grid_square = screen_height // 3




RED = (255,0,0)



def grid():
    for column in range(0,screen_width,grid_square):
        for row in range(0,screen_height,grid_square):
            pygame.draw.rect(screen,RED,(column,row,grid_square,grid_square),1)




# game loop
pygame.init()

running = True


screen = pygame.display.set_mode((screen_height,screen_width))















while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    grid()
    pygame.display.update()

pygame.quit()