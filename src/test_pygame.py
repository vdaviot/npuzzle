import pygame, sys
from pygame.locals import *

pygame.init()

size = width, height = 600, 800
screen = pygame.display.set_mode(size)
done = False
while not done:
	events = pygame.event.get()
	for event in events:
	    if event.type == pygame.KEYDOWN:
	        if event.key == pygame.K_ESCAPE:
	            sys.exit()
	        if event.key == pygame.K_RIGHT:
	            print("RIGHT\n")
	        
