import pygame

#pygame setup

pygame.init()
screen = pygame.display.set_mode((500,350))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    #render game here
    pygame.draw.circle(screen, "green", player_pos, 20)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt


    pygame.display.flip()


    #dt is delta time in sec since last frame, used for framerate independant physics
    dt = clock.tick(60) / 1000  #limits fps to 60

pygame.quit()


    