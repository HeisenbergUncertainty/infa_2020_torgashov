import pygame
from pygame.draw import *
from random import randint
import numpy as np


pygame.init()

x_max, y_max = 900, 600 #sizes
R_min, R_max = 30, 80 #radius min and max
V_max = 10 #max velocity
FPS = 30
screen = pygame.display.set_mode((x_max, y_max))

'''Colours'''
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLOURS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

'''Balls'''
num = randint(4, 6) #number of balls
x = np.random.randint(R_max, x_max - R_max, num).reshape((num, 1))
y = np.random.randint(R_max, x_max - R_max, num).reshape((num, 1))
xspeed = np.random.randint(- V_max, V_max, num).reshape((num, 1))
yspeed = np.random.randint(- V_max, V_max, num).reshape((num, 1))
r = np.random.randint(R_min, R_max, num).reshape((num, 1))
colour = np.random.randint(0, 5, num).reshape((num, 1))
BALLS = np.concatenate((x, y, xspeed, yspeed, r, colour), axis = 1)

screencolour = BLACK 


def draw_ball(x, y, r, colour):
    ball = circle(screen, colour, (x, y), r)
    
def give_score(points):
    #print and write to file "out" points
    file = open("out.txt", "a")
    file.write('Name: ' + str(input("¬ведите им€\n")) + ': ' + str(points) + '\n') 
    file.close()
    
    print("Score: " + points)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
points = 0
font = pygame.font.Font(None, 50)

while not finished:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            give_score(points)
            
            finished = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range (num): #(x, y, xspeed, yspeed, r, colour)
                x_i, y_i, r_i = BALLS[i, 0], BALLS[i, 1], BALLS[i, 4]
                if (x_i - event.pos[0])**2 + (y_i - event.pos[1])**2 <= r_i**2:
                    #points = int(full_velocity * 10 / radius)
                    points += int((BALLS[i, 2]**2 + BALLS[i, 3]**2)**0.5 * 10 \
                        / BALLS[i, 4])
                    #to level out false penalties
                    points += num - 1
                    #teleport and change velocities ball after click
                    BALLS[i, 0] = randint(R_max, x_max - R_max) 
                    BALLS[i, 1] = randint(R_max, y_max - R_max)
                    BALLS[i, 2] = randint(-3 * V_max, 3 * V_max)
                    BALLS[i, 3] = randint(-3 * V_max, 3 * V_max)
                
                else:
                    #penalty points (for every ball, because than more balls
                    #than easier hit on them)
                    points -= 1

                
    for i in range(num):         
        if 0 < BALLS[i, 0] < x_max and 0 < BALLS[i, 1] < y_max:
            BALLS[i, 0] += BALLS[i, 2] #move it
            BALLS[i, 1] += BALLS[i, 3]
            draw_ball(BALLS[i, 0], BALLS[i,1], BALLS[i, 4], 
                      COLOURS[BALLS[i, 5]])
            
        elif BALLS[i, 0] <= 0:
            BALLS[i, 2] = randint(0, 3 * V_max)
            BALLS[i, 0] += BALLS[i, 2]
            draw_ball(BALLS[i, 0], BALLS[i,1], BALLS[i, 4], 
                      COLOURS[BALLS[i, 5]])
            
        elif BALLS[i, 0] >= x_max:
            BALLS[i, 2] = randint(-3 * V_max, 0)
            BALLS[i, 0] += BALLS[i, 2]
            draw_ball(BALLS[i, 0], BALLS[i,1], BALLS[i, 4], 
                      COLOURS[BALLS[i, 5]])
            
        elif BALLS[i, 1] <= 0:
            BALLS[i, 3] = randint(0, 3 * V_max)
            BALLS[i, 1] += BALLS[i, 3]
            draw_ball(BALLS[i, 0], BALLS[i,1], BALLS[i, 4], 
                      COLOURS[BALLS[i, 5]])
            
        elif BALLS[i, 1] >= y_max:
            BALLS[i, 3] = randint(-3 * V_max, 0)
            BALLS[i, 1] += BALLS[i, 3]
            draw_ball(BALLS[i, 0], BALLS[i,1], BALLS[i, 4], 
                      COLOURS[BALLS[i, 5]])
            
 
    pygame.display.update()
    screen.fill(screencolour)
    score_text = font.render("Score: " + str(points), True, (0, 255, 0))
    screen.blit(score_text, (100, 100))    

pygame.quit()
