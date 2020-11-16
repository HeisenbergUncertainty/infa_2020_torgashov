# coding: utf8
import pygame
from pygame.draw import *
from random import randint

def tree(x, y, kx, ky): #рисует дерево с координатами x, y; kx, ky - параметры размера
    rect(screen, (230, 190, 0), (x, y, 10*kx, 10*ky))

def mushroom(x, y, k): #рисует гриб с координатами x, y; k - параметр размера
    ellipse(screen, (255, 255, 255), (x + 7.5*k , y + 5*k, k*5, k*15))    
    ellipse(screen, (255, 0, 0), (x, y, k*20, k*10))
    
    for _ in range(10):
        ellipse(screen, (255, 255, 255), (x + randint(2, 16)*k, 
                                          y + randint(1, 7)*k, 2*k, k))            
    
def hedge(x, y, k): #рисует ежа с координатами x, y; k - параметр размера
    ellipse(screen, (120, 120, 120), (x+k*16, y+k*7, k*6, k*3))
    ellipse(screen, (120, 120, 120), (x, y+k*7, k*6, k*3))
    ellipse(screen, (250, 120, 120), (x+k*17, y+k*3, k*6, k*3))
    
    ellipse(screen, (120, 120, 120), (x, y, k*20, k*10))
    ellipse(screen, (150, 150, 150), (x+k*17, y+k*3, k*7, k*4))
    
    circle(screen, (255, 0, 0), (x+k*20, y+k*4), k//2) #ãëàçà
    circle(screen, (255, 0, 0), (x+k*22, y+k*4), k//2)
    
    
    for i in range(50):
        x1, y1 = x + randint(2, 16)*k, y + randint(1, 7)*k
        polygon(screen, (0, 0, 0), [[x1, y1], [x1+2*k, y1], [x1+k, y1-4*k]], 0)
        if i == 40:
            mushroom(x-k, y-k, k/3)
            mushroom(x+2*k, y+2*k, k/3)
            mushroom(x+8*k, y+3*k, k/3)
            circle(screen, (255, 112, 77), (x+10*k, y+k), 2*k)
            circle(screen, (255, 112, 77), (x+14*k, y+k*3), 2*k)
            
            
pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))
rect(screen, (150, 200, 70), (0, 0, 500, 500)) #Ôîí
rect(screen, (180, 60, 14), (0, 500, 500, 200))

#"база данных" картинки
trees = [(0, 0, 3, 61), (50, 0, 8, 65), (320, 0, 4, 55), (430, 0, 3, 60)]
hedges = [(300, 550, 7), (400, 400, 4), (100, 500, 3), (-50, 650, 5)]
mushrooms = [(450, 650, 4), (410, 660, 4), (370, 640, 4), (320, 655, 4)]

#отрисовка
for tr in trees:
    tree(*tr)

for hg in hedges:
    hedge(*hg)
    
for mush in mushrooms:
    mushroom(*mush)

#костыль отрисовки
tree(50, 0, 8, 65)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
