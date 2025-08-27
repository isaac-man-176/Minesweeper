import pygame

RED = (255,0,0)
BLACK = (0,0,0)
DARKGREY = (96,96,96)

class Tile:
    def __init__(self,x,y,size):
        self.xPos = x
        self.yPos = y
        self.tileSize = size
        self.rect = pygame.Rect(x,y,size,size)
        self.flagVis = False

    def draw(self, screen):
        pygame.draw.rect(screen, DARKGREY, self.rect)
        if self.flagVis == True:
            pygame.draw.polygon(screen,RED, [
            (self.xPos+self.tileSize/4,self.yPos+self.tileSize/6),      # top point
            (self.xPos+self.tileSize/4,self.yPos+self.tileSize/2),      # bottom point
            (self.xPos+self.tileSize*0.75,self.yPos+self.tileSize/3)])  # right point
            pygame.draw.rect(screen,BLACK,[(self.xPos+self.tileSize/4),(self.yPos+self.tileSize/6),(self.tileSize/8),(self.tileSize/1.5)])

    def drawFlag(self):
        self.flagVis = True