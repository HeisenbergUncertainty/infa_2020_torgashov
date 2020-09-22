import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((230, 230, 230))

#rect(screen, (255, 0, 255), (100, 100, 200, 200))
#polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               #(300,100), (100,100)], 5)
#circle(screen, (255, 255, 255), (200, 175), 50, 5)

x1, y1, r1 = 200, 175, 100
circle(screen, (0, 0, 0), (x1, y1), r1+1, r1+1)
circle(screen, (255, 215, 0), (x1, y1), r1, r1)

x2, y2, r2 = 160, 140, 20
circle(screen, (0, 0, 0), (x2, y2), r2 + 1, r2 + 1)
circle(screen, (250, 0, 0), (x2, y2), r2, r2)
circle(screen, (0, 0, 0), (x2, y2), r2 - 5, r2 - 5)

x3, y3, r3 = 230, 140, 15
circle(screen, (0, 0, 0), (x3, y3), r3 + 1, r3 + 1)
circle(screen, (250, 0, 0), (x3, y3), r3, r3)
circle(screen, (0, 0, 0), (x3, y3), r3 - 7, r3 - 7)

x4, y4 = 180, 130
polygon(screen, (0, 0, 0), [(x4, y4), (x4-70,y4-70),
                               (x4-55,y4-85), (x4+15, y4-15)], 0)

x5, y5 = 400 - x4, y4
polygon(screen, (0, 0, 0), [(x5, y5), (x5+70,y5-70),
                               (x5+55,y5-85), (x5-15, y5-15)], 0)

x6, y6 = 140, 200
rect(screen, (0, 0, 0), (x6, y6, 120, 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()