import pygame

pygame.init()

# Spacing
numOfTilesHoriz = 10
numOfTilesVert = 10
tilePadding = 10
tileSize = 50
boardPadding = 10
headerHeight = 50
headerPadding = 10
restartButtonSize = 50
borderThickness = 2

# Colors
BLACK =             (0,0,0)
LIGHTBLACK =        (32,32,32)
DARKDARKGREY =      (64,64,64)
DARKGREY =          (96,96,96)
GREY =              (128,128,128)
LIGHTGREY =         (159,159,159)
LIGHTLIGHTGREY =    (191,191,191)
DARKWHITE =         (223,223,223)
WHITE =             (255,255,255)

RED = (255,0,0)

# Game Variables
numOfClicks = 0

screen = pygame.display.set_mode((boardPadding*2+(tileSize+tilePadding)*numOfTilesHoriz+tilePadding,boardPadding*2+(tileSize+tilePadding)*numOfTilesVert+tilePadding+headerPadding*2+headerHeight))
clock = pygame.time.Clock()

board = pygame.Rect(boardPadding,boardPadding,(tileSize+tilePadding)*numOfTilesHoriz+tilePadding,(tileSize+tilePadding)*numOfTilesVert+tilePadding+headerPadding*2+headerHeight)

class Tile:
    def __init__(self,x,y,size):
        self.xPos = x
        self.yPos = y
        self.tileSize = size
        self.rect = pygame.Rect(x,y,size,size)

    def draw(self):
        pygame.draw.rect(screen, DARKGREY, self.rect)

    def drawFlag(self):
        pygame.draw.polygon(screen,RED, [
            (self.xPos+self.tileSize/4,self.yPos+self.tileSize/6),      # top point
            (self.xPos+self.tileSize/4,self.yPos+self.tileSize/2),      # bottom point
            (self.xPos+self.tileSize*0.75,self.yPos+self.tileSize/3)])  # right point
        pygame.draw.rect(screen,BLACK,[(self.xPos+self.tileSize/4),(self.yPos+self.tileSize/6),(tileSize/8),(tileSize/1.5)])

# creating instances of tiles 
grid = []
for y in range(numOfTilesVert):
    line = []
    for x in range(numOfTilesHoriz):
        newTile1 = Tile(boardPadding+tilePadding+(tileSize+tilePadding)*(x),boardPadding+headerHeight+headerPadding*2+tilePadding+(tileSize+tilePadding)*(y),tileSize)
        line.append(newTile1)
    grid.append(line)

while True:
# graphics

    # board and background
    screen.fill(BLACK)
    pygame.draw.rect(screen, LIGHTLIGHTGREY,board)

    # restart button graphics
    restartButton = pygame.Rect(boardPadding+(tileSize+tilePadding)*numOfTilesHoriz/2+ tilePadding/2 - restartButtonSize/2, boardPadding+headerPadding,restartButtonSize,restartButtonSize)
    pygame.draw.rect(screen,LIGHTGREY, restartButton,restartButtonSize)
    restartButtonBorder = pygame.Rect(boardPadding+(tileSize+tilePadding)*numOfTilesHoriz/2+ tilePadding/2 - restartButtonSize/2, boardPadding+headerPadding,restartButtonSize,restartButtonSize)
    pygame.draw.rect(screen, DARKGREY, restartButtonBorder, borderThickness)
    
    # drawing each instance of tile
    for row in grid:
        for tile in row:
            tile.draw()
            tile.drawFlag()

# updates 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.MOUSEBUTTONDOWN:
            numOfClicks += 1
            print("Times Clicked:" + str(numOfClicks))
        
    # refresh frame
    pygame.display.flip()
    clock.tick(60)

