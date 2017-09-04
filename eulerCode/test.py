import pygame
import sys
from pygame.locals import *
pygame.init()
s=pygame.display.set_mode((100,100))
while True:
    for i in pygame.event.get():
        print(i)
        if i.type==KEYDOWN:
            if i.unicode=='a':
                sys.exit()

        
