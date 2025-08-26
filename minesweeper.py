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


while True:
    # graphics
    screen.fill("black")
    pygame.draw.rect(screen, "darkgrey",board)

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

