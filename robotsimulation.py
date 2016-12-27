
import pygame
import sys
import math
from pygame.locals import *


pygame.init()

ROOMWIDTH = 1200
ROOMHEIGHT = 1000
DISPLAYSURF = pygame.display.set_mode((ROOMWIDTH, ROOMHEIGHT), 0, 32)
pygame.display.set_caption('Robot Simulation')

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

DISPLAYSURF.fill(WHITE)

#pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (360, 60), 4)
#pygame.draw.line(DISPLAYSURF, BLACK, (360, 60), (360, 240), 4)
#pygame.draw.line(DISPLAYSURF, GREEN, (360, 240), (60, 240), 4)
#pygame.draw.line(DISPLAYSURF, RED, (60, 240), (60, 60), 4)
#pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
#pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

ROBOTARCWIDTH = 5*25
ROBOTARCHEIGHT = 5*25


class Robot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        #pygame.draw.rect(DISPLAYSURF, BLACK, (self.x, self.y, 5, 5*25))
        #pygame.draw.rect(DISPLAYSURF, BLACK, (self.x, self.y, 5*25, 5))
        #pygame.draw.rect(DISPLAYSURF, BLACK, (self.x, self.y, 5, -5*25))
        #pygame.draw.rect(DISPLAYSURF, BLACK, (self.x, self.y, -5*25, 5))
        pygame.draw.arc(DISPLAYSURF, BLACK, (self.x, self.y, ROBOTARCWIDTH, ROBOTARCHEIGHT), 7/4 * math.pi, 5/4 * math.pi)

    #def shootLaser(self):


#list of walls
walls = []  

class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

#current room
room = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "W                                                W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",]
    





#parse the above picture into the walls
x = y = 0
for row in room:
    for col in row:
        if col == "W":
            Wall((x,y))
        x += 16
    y += 16
    x = 0





#generate the wall
for wall in walls:
    pygame.draw.rect(DISPLAYSURF, RED, wall.rect)



while True: #main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mX, mY = pygame.mouse.get_pos()
            fetch = Robot(mX - ROBOTARCWIDTH/2 , mY - ROBOTARCHEIGHT/2)
            fetch.draw()
            
            
            
    pygame.display.update()
