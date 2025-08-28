import pygame
from tile import Tile
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

class Main:

    # Game Variables
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((boardPadding*2+(tileSize+tilePadding)*numOfTilesHoriz+tilePadding,boardPadding*2+(tileSize+tilePadding)*numOfTilesVert+tilePadding+headerPadding*2+headerHeight))

    
    def __init__(self):
        self.grid = []
        self.setup()

    def setup(self):
    # creating instances of tiles 
        for y in range(numOfTilesVert):
            line = []
            for x in range(numOfTilesHoriz):
                newTile1 = Tile(boardPadding+tilePadding+(tileSize+tilePadding)*(x),boardPadding+headerHeight+headerPadding*2+tilePadding+(tileSize+tilePadding)*(y),tileSize)
                line.append(newTile1)
            self.grid.append(line)

    def restart(self):
        self.grid = []
        self.setup()

    def run(self):
        while True:
            # graphics

            # board and background
            self.screen.fill(BLACK)
            board = pygame.Rect(boardPadding,boardPadding,(tileSize+tilePadding)*numOfTilesHoriz+tilePadding,(tileSize+tilePadding)*numOfTilesVert+tilePadding+headerPadding*2+headerHeight)
            pygame.draw.rect(self.screen, LIGHTLIGHTGREY,board)

            # restart button graphics
            restartButton = pygame.Rect(boardPadding+(tileSize+tilePadding)*numOfTilesHoriz/2+ tilePadding/2 - restartButtonSize/2, boardPadding+headerPadding,restartButtonSize,restartButtonSize)
            pygame.draw.rect(self.screen,LIGHTGREY, restartButton,restartButtonSize)
            restartButtonBorder = pygame.Rect(boardPadding+(tileSize+tilePadding)*numOfTilesHoriz/2+ tilePadding/2 - restartButtonSize/2, boardPadding+headerPadding,restartButtonSize,restartButtonSize)
            pygame.draw.rect(self.screen, DARKGREY, restartButtonBorder, borderThickness)
    
            # drawing each instance of tile
            for row in self.grid:
                for tile in row:
                    tile.draw(self.screen)

            # updates 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                elif event.type == pygame.MOUSEBUTTONDOWN:
                
                    # clicking on restart button
                    if event.button == 1: # left click
                        if restartButton.collidepoint(pygame.mouse.get_pos()):
                            print("restarted")
                            self.restart()

                    # clicking on a tile
                    clickedTile = Tile.findTile(self.grid)
                    if clickedTile:
                        if event.button == 1: # left click
                            print("left click")
                        if event.button == 3: # right click
                            clickedTile.drawFlag()
        
            # refresh frame
            pygame.display.flip()
            self.clock.tick(60)         

game = Main()
game.run()