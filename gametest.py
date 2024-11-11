#!/usr/bin/env python3

import os
import pygame

pygame.init()

display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Testing')

clock = pygame.time.Clock()
crashed = False

class Car(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, carImg.get_size()[0], carImg.get_size()[1])
        self.image = carImg

carImg = pygame.transform.scale2x(pygame.image.load('open.png'))

def draw_car(x, y):
    gameDisplay.blit(carImg, (x, y))

x = display_width * 0.45
y = display_height * 0.8

gameDisplay.fill(white)
draw_car(x, y)

pygame.display.flip()

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    y -= 1
    gameDisplay.fill(white)
    draw_car(x, y)

    if y < 10:
        crashed = True

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
quit()
