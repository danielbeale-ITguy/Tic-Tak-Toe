import pygame
from variables import LAVENDER






class grid:
    def __init__(self,screen,width,height,grid_square):
        self.width = width
        self.height = height
        self.grid_square = grid_square
        self.screen = screen
        self.grid_list = []
        self.default_color = LAVENDER
        self.cross_color = LAVENDER
        self.naught_color = LAVENDER
        self.turn_num = 0
        self.split_grid()

        self.nought = pygame.image.load('nought.png')
        self.nought.convert()
        self.nought = pygame.transform.scale(self.nought, (grid_square, grid_square))
        
        self.cross = pygame.image.load('cross.png')
        self.cross.convert()
        self.cross = pygame.transform.scale(self.cross, (grid_square, grid_square))

      
    def split_grid(self):
            for row in range(0,self.height,self.grid_square):
                for column in range(0,self.width,self.grid_square):
                  rect = pygame.Rect(column,row,self.grid_square,self.grid_square)
                  self.grid_list.append((rect,self.default_color,None))
            
    
    def draw(self):
        for rect, color, image in self.grid_list:
            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(self.screen, (100, 100, 100), rect, 1)

            if image:
                self.screen.blit(image,rect)

    def clicked(self,mouse_x,mouse_y):
        if self.turn_num % 2 == 0:
            for cell,(rect,color,image) in  enumerate(self.grid_list):
                if rect.collidepoint(mouse_x,mouse_y):
                    color = LAVENDER
                    self.turn_num += 1
                    image = self.cross
                    self.grid_list[cell] = (rect,color,image)




                    print(self.turn_num)
        else:
            for cell,(rect,color,image) in  enumerate(self.grid_list):
                if rect.collidepoint(mouse_x,mouse_y):
                    color = LAVENDER
                    self.turn_num += 1
                    image = self.nought
                    self.grid_list[cell] = (rect,color,image)


                    print(self.turn_num)







    def check_win(self):
        # Check nought wins
        if self.grid_list[0][2] == self.nought and \
        self.grid_list[1][2] == self.nought and \
        self.grid_list[2][2] == self.nought:
            return True
        elif self.grid_list[3][2] == self.nought and \
        self.grid_list[4][2] == self.nought and \
        self.grid_list[5][2] == self.nought:
            return True
        elif self.grid_list[6][2] == self.nought and \
        self.grid_list[7][2] == self.nought and \
        self.grid_list[8][2] == self.nought:
            return True
        elif self.grid_list[0][2] == self.nought and \
        self.grid_list[3][2] == self.nought and \
        self.grid_list[6][2] == self.nought:
            return True
        elif self.grid_list[1][2] == self.nought and \
        self.grid_list[4][2] == self.nought and \
        self.grid_list[7][2] == self.nought:
            return True
        elif self.grid_list[2][2] == self.nought and \
        self.grid_list[5][2] == self.nought and \
        self.grid_list[8][2] == self.nought:
            return True
        elif self.grid_list[0][2] == self.nought and \
        self.grid_list[4][2] == self.nought and \
        self.grid_list[8][2] == self.nought:
            return True
        elif self.grid_list[2][2] == self.nought and \
        self.grid_list[4][2] == self.nought and \
        self.grid_list[6][2] == self.nought:
            return True
        
        # Check cross wins
        elif self.grid_list[0][2] == self.cross and \
        self.grid_list[1][2] == self.cross and \
        self.grid_list[2][2] == self.cross:
            return True
        elif self.grid_list[3][2] == self.cross and \
        self.grid_list[4][2] == self.cross and \
        self.grid_list[5][2] == self.cross:
            return True
        elif self.grid_list[6][2] == self.cross and \
        self.grid_list[7][2] == self.cross and \
        self.grid_list[8][2] == self.cross:
            return True
        elif self.grid_list[0][2] == self.cross and \
        self.grid_list[3][2] == self.cross and \
        self.grid_list[6][2] == self.cross:
            return True
        elif self.grid_list[1][2] == self.cross and \
        self.grid_list[4][2] == self.cross and \
        self.grid_list[7][2] == self.cross:
            return True
        elif self.grid_list[2][2] == self.cross and \
        self.grid_list[5][2] == self.cross and \
        self.grid_list[8][2] == self.cross:
            return True
        elif self.grid_list[0][2] == self.cross and \
        self.grid_list[4][2] == self.cross and \
        self.grid_list[8][2] == self.cross:
            return True
        elif self.grid_list[2][2] == self.cross and \
        self.grid_list[4][2] == self.cross and \
        self.grid_list[6][2] == self.cross:
            return True
        else:
            return False
        
            
#    def restart(self):
#        if self.turn_num > 8:
