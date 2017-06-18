import pygame, sys, random
import RPi.GPIO as GPIO
from subprocess import call

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # set up pin 4
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # set up pin 17

kortlys = pygame.image.load('kortlys3.gif')
langlys = pygame.image.load('langlys3.gif')
batteri = pygame.image.load('batteri3.gif')
olie = pygame.image.load('olie.gif')
neutral = pygame.image.load('neutrallys3.gif')
venstre = pygame.image.load('venstre.gif')
hoejre = pygame.image.load('hoejre.gif')
lys = pygame.image.load('sort.gif')

Pause = 0      #
x = 8          #
y = 0          # indstillinger for pause
xspeed = 1     #
yspeed = 2     #

pygame.init()

window = pygame.display.set_mode((128,160) , pygame.NOFRAME)


while True:
    window.fill((0,0,0))
    Pause += 1
   
    if GPIO.input(4) == 0 and Pause < 1800:
       # call("sudo shutdown now", shell=True)
        lys = kortlys
        window.blit(kortlys, (0,0))
    if GPIO.input(4) == 1 and Pause < 1800:
        lys = langlys
        window.blit(langlys, (0,0))
    if GPIO.input(17) == 0:
        Pause = 0
        window.blit(batteri, (64,0))
    
    if GPIO.input(4) == 0 and Pause > 1800:
       lys = kortlys
       window.blit(lys, (x,y))
    if GPIO.input(4) == 1 and Pause > 1800:
       lys = langlys
       window.blit(lys, (x,y))

    x += xspeed
    y += yspeed

    if y > 107 or y < 0:
        yspeed *= -1

    if x > 64 or x < 0:
        xspeed *= -1 

    pygame.time.Clock().tick(30)    

    pygame.display.update()
