import pygame
import Module
#pygame setup

window_dim = 600

pygame.init()
screen = pygame.display.set_mode((window_dim, window_dim))
clock = pygame.time.Clock()
running = True
blockSize = 30 #Set the size of the grid block




def drawGrid(blockSize):
    for x in range(0, window_dim, blockSize):
        for y in range(0, window_dim, blockSize):
            cell = Module.Cell(x, y, blockSize, False)
            pygame.draw.rect(screen, "#333333", cell.gridCell, 1)
            

# def makeAlive():
#     return

# def makeDead():
#     return

while running:

    screen.fill("black")
    drawGrid(blockSize)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            m_pos = pygame.mouse.get_pos()
            print(round((m_pos[0]-(blockSize/2))/blockSize),round((m_pos[1]-(blockSize/2))/blockSize))

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     clock.tick()


    #render game here
    


    pygame.display.flip()


    #dt is delta time in sec since last frame, used for framerate independent physics
    clock.tick(60)  #limits fps to 60

pygame.quit()




