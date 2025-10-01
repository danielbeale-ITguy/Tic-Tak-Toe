import pygame
from variables import RED, BLUE, rect_color




class grid:
    def __init__(self,screen,width,height,grid_square):
        self.width = width
        self.height = height
        self.grid_square = grid_square
        self.screen = screen
        self.grid_list = []
        self.default_color = RED
        self.changed_color = BLUE
        self.split_grid()

      
    def split_grid(self):
            for row in range(0,self.height,self.grid_square):
                for column in range(0,self.width,self.grid_square):
                  rect = pygame.Rect(column,row,self.grid_square,self.grid_square)
                  self.grid_list.append((rect,self.default_color))
            
    
    def draw(self):
        for rect, color in self.grid_list:
            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(self.screen, (100, 100, 100), rect, 1) 

    def clicked(self,mouse_x,mouse_y):
        for cell,(rect,color) in  enumerate(self.grid_list):
            if rect.collidepoint(mouse_x,mouse_y):
                color = BLUE
                self.grid_list[cell] = (rect,color)

    def check_win(self):
        if self.grid_list[0][1] == (0,0,255) and \
        self.grid_list[1][1] == (0,0,255) and \
        self.grid_list[2][1] == (0,0,255):
            print('winner')

