import pygame, sys, random
import RPi.GPIO as GPIO
from subprocess import call


pygame.init()

window = pygame.display.set_mode((128,160) , pygame.NOFRAME)
kortlys = pygame.image.load('kortlys3.gif')
langlys = pygame.image.load('langlys3.gif')
animationTimer = pygame.time.Clock()

x = 8
y = 0

xspeed = 1
yspeed = 2

while True:
    window.fill((0,0,0))
    window.blit(langlys, (x, y))
    x += xspeed
    y += yspeed

    if y > 107 or y < 0:
        yspeed *= -1

    if x > 64 or x < 0:
        xspeed *= -1 

    animationTimer.tick(30)    

    pygame.display.update()
