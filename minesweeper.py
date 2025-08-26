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

# Game Variables
numOfClicks = 0

screen = pygame.display.set_mode((boardPadding*2+(tileSize+tilePadding)*numOfTilesHoriz+tilePadding,boardPadding*2+(tileSize+tilePadding)*numOfTilesVert+tilePadding+headerPadding*2+headerHeight))
clock = pygame.time.Clock()

board = pygame.Rect(boardPadding,boardPadding,(tileSize+tilePadding)*numOfTilesHoriz+tilePadding,(tileSize+tilePadding)*numOfTilesVert+tilePadding+headerPadding*2+headerHeight)

grid = []

class Tile:
    def __init__(self,xPos,yPos,tileSize):
        self.rect = pygame.Rect(xPos,yPos,tileSize,tileSize)

    def draw(self):
        pygame.draw.rect(screen, "black", self.rect)

for y in range(numOfTilesVert):
    for x in range(numOfTilesHoriz):
        newTile1 = Tile(boardPadding+tilePadding+(tileSize+tilePadding)*(x),boardPadding+headerHeight+headerPadding*2+tilePadding+(tileSize+tilePadding)*(y),tileSize)
        grid.append(newTile1)
        print("x coord "+str(x)+" y coord "+str(y))


while True:
    # graphics
    screen.fill("black")
    pygame.draw.rect(screen, "darkgrey",board)

    for tile in grid:
        tile.draw()

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

