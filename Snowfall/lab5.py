import shapes
import pygame
import random

pygame.init()
size = [400,300]
screen = pygame.display.set_mode(size)
print(screen)
pygame.display.set_caption('Snowflakes')
clock = pygame.time.Clock()
running = True
print('hi')
ground = shapes.Rectangle([0,200], 400, 100, pygame.Color(0,255,0))
sky = shapes.Rectangle([0,0], 400, 200, pygame.Color(0,0,255))
drawables = [ground,sky]
print('test')
paused = True
while running:
    clock.tick(30)
    screen.fill(pygame.Color(255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.unicode == ' ':
                paused = not paused
    if paused:
        for thing in drawables:
            thing.draw(screen)
        pygame.display.update()
        continue
    drawables.append(shapes.Snowflake((random.randint(0,400),random.randint(200,300)), pygame.Color(255,255,255)))
    for thing in drawables:
        if isinstance(thing, shapes.Snowflake):
            loc = thing.getLoc()
            if loc[1] < thing.getMax():
                thing.setLoc((loc[0],loc[1]+1))
        thing.draw(screen)
    pygame.display.update()


            
            
    