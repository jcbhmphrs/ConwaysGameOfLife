import pygame

#pygame setup

window_dim = 800

pygame.init()
screen = pygame.display.set_mode((window_dim, window_dim))
clock = pygame.time.Clock()
running = True


def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, window_dim, blockSize):
        for y in range(0, window_dim, blockSize):
            cell = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, "#333333", cell, 1)


while running:

    screen.fill("black")
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)


    #render game here
    


    pygame.display.flip()


    #dt is delta time in sec since last frame, used for framerate independant physics
    clock.tick(60)  #limits fps to 60

pygame.quit()




