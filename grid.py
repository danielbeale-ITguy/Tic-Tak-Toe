import pygame
from variables import RED





class grid:
    def __init__(self,screen,width,height,grid_square):
        self.width = width
        self.height = height
        self.grid_square = grid_square
        self.screen = screen
      
    def split_grid(self):
            for column in range(0,self.width,self.grid_square):
                for row in range(0,self.height,self.grid_square):
                    pygame.draw.rect(self.screen,RED,(column,row,self.grid_square,self.grid_square),1)
            


