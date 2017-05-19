#!/usr/bin/python3

import os
import pygame

pygame.init()

display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Testing')


clock = pygame.time.Clock()
crashed = False
carImg = pygame.transform.scale2x(pygame.image.load('open.png'))

def car(x,y):
    gameDisplay.blit(pygame.transform.scale2x(carImg), (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)

gameDisplay.fill(white)
car(x,y)

pygame.display.flip()

while not crashed:

#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            crashed = True

#        print(event)
    y=y-1
    gameDisplay.fill(white)
    car(x,y)

    if y < 10:
        crashed = True

    pygame.display.flip()
#   clock.tick(10)

pygame.quit()
quit()
