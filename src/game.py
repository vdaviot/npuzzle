import pygame, sys, random
from pygame.locals import *

class Game():

	def __init__(self, grid, interactive=True, benchmark=False):
		self.grid = grid
		self.done = False
		self.options = {
			'interactive': interactive,
			'benchmark': benchmark,
			}
		pygame.init()
		pygame.display.set_mode((800, 600))
		pygame.display.set_caption('Npuzzle')


	def run(self):
		for event in pygame.event.get(KEYUP):
			if event.key == K_ESCAPE:
				sys.exit(0)
		pygame.display.update()
