import pygame
import RPi.GPIO as GPIO
from subprocess import call

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # set up pin 4
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # set up pin 17

pygame.init()

window = pygame.display.set_mode((128,160) , pygame.NOFRAME)
kortlys = pygame.image.load('kortlys3.gif')
langlys = pygame.image.load('langlys3.gif')
batteri = pygame.image.load('batteri3.gif')
olie = pygame.image.load('olie.gif')
neutral = pygame.image.load('neutrallys3.gif')
venstre = pygame.image.load('venstre.gif')
hoejre = pygame.image.load('hoejre.gif')
sort = pygame.image.load('sort.gif')


while True:

   
    if GPIO.input(4) == 0:
       # call("sudo shutdown now", shell=True)
        
       window.blit(kortlys, (0,0))
    if GPIO.input(4) == 1:
        window.blit(langlys, (0,0))
    if GPIO.input(17) == 0:
        window.blit(batteri, (64,0))
    if GPIO.input(17) == 1:
        window.blit(sort, (64,0))     
    
    window.blit(olie, (0,53))
    window.blit(neutral, (64,53))
    window.blit(hoejre, (0,106))
    
    pygame.display.update()
