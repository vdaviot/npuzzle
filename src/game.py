# UTILISE LE coding: utf-8 !
import pygame, sys, random
from pygame.locals import *

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

class Game(object):

	def __init__(self, grid, solvedGrid, len=3, interactive=True):
		# Interactive False = Bench mode
		print("é")
		self.grid = grid
		self.solvedGrid = solvedGrid
		self.done = False
		self.len = len
		self.options = {
			'interactive': interactive,
			}
		self.neighbours = Neighbours(self.grid, self._getTile(0))
		if self.options['interactive']: # Initialisation pygame
			self.screenX, self.screenY = 800, 600
			self.tileSize = self.screenX / self.len
			self.marginX = (self.screenX - (self.tileSize * self.len + (self.len - 1))) / 2
			self.marginY = (self.screenY - (self.tileSize * self.len + (self.len - 1))) / 2
			self.padding = self.screenX / self.len / 20
			self.spaceX = self.padding + (self.screenX - self.padding * (self.len + 1)) / self.len
			self.spaceY = self.padding + (self.screenY - self.padding * (self.len + 1)) / self.len

			pygame.init()
			self.screen = pygame.display.set_mode((self.screenX, self.screenY))
			self.font = pygame.font.SysFont('Arial', self.screenX / 20)
			self.clock = pygame.time.Clock()
			pygame.display.set_caption('Npuzzle')
		else: # Pas de visuel, juste resolution et affichage stat
			self._solve(grid)


	def calcPadding(self, row, col):
		return [self.padding + self.spaceX * col, self.padding + self.spaceY * row, self.spaceX - self.padding, self.spaceY - self.padding]


	def getColor(self):
		return (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))


	def draw_grid(self, board):
		color_f = (255, 255, 255) # Temporary 
		color_r = (25, 25, 25) # Temporary
		for row in range(self.len):
			for col in range(self.len):
				posX, posY, sizeX, sizeY = self.calcPadding(row, col)
				if board[row][col] == 0:
					pygame.draw.rect(self.screen, (120, 25, 25), (posX, posY, sizeX, sizeY))
				else:
					pygame.draw.rect(self.screen, color_r, (posX, posY, sizeX, sizeY))
				self.screen.blit(self.font.render(str(board[row][col]), True, color_f), (posX, posY))


	# def gridAfterMove(self, move, posX, posY):
	# 	new_grid = [row[:] for row in self.grid.grid]
	# 	if move == 'right':
	# 		new_grid[posY][posX], new_grid[posY][posX + 1] = new_grid[posY][posX + 1], new_grid[posY][posX]
	# 	elif move == 'left':
	# 		new_grid[posY][posX], new_grid[posY][posX - 1] = new_grid[posY][posX - 1], new_grid[posY][posX]
	# 	elif move == 'top':
	# 		new_grid[posY][posX], new_grid[posY - 1][posX] = new_grid[posY - 1][posX], new_grid[posY][posX]
	# 	elif move == 'bottom':
	# 		new_grid[posY][posX], new_grid[posY + 1][posX] = new_grid[posY + 1][posX], new_grid[posY][posX]
	# 	return new_grid

	def _handle_key(self, key):
		posX, posY = self._getTile(0) # Get 0 tile posX, posY
		if key in [K_UP, K_w] and self._isValidMove(UP):
			self.grid.grid[posY][posX], self.grid.grid[posY - 1][posX] = self.grid.grid[posY - 1][posX], self.grid.grid[posY][posX]

		elif key in [K_DOWN, K_s] and self._isValidMove(DOWN):
			self.grid.grid[posY][posX], self.grid.grid[posY + 1][posX] = self.grid.grid[posY + 1][posX], self.grid.grid[posY][posX]

		elif key in [K_LEFT, K_a] and self._isValidMove(LEFT):
			self.grid.grid[posY][posX], self.grid.grid[posY][posX - 1] = self.grid.grid[posY][posX - 1], self.grid.grid[posY][posX]

		elif key in [K_RIGHT, K_d] and self._isValidMove(RIGHT):
			self.grid.grid[posY][posX], self.grid.grid[posY][posX + 1] = self.grid.grid[posY][posX + 1], self.grid.grid[posY][posX]
		self.neighbour.setNodes(self.grid.grid, {'x': posX, 'y': posY})


	def _getTile(self, tile):
		for idy, row in enumerate(self.grid.grid):
			for idx, col in enumerate(row):
				if col == tile:
					return idx, idy

	# def _getNeighbour(self):
	# 	posX, posY = self._getTile(0)
	# 	return {
	# 		'right': self.gridAfterMove('right', posX, posY) if posX < self.len - 1 else None,
	# 		'left': self.gridAfterMove('left', posX, posY) if posX > 0 else None,
	# 		'top': self.gridAfterMove('top', posX, posY) if posY > 0 else None,
	# 		'bottom': self.gridAfterMove('bottom', posX, posY) if posY < self.len - 1 else None,
	# 	}

	def _isValidMove(self, move):
		posX, posY = self._getTile(0)
		if move == UP and posY - 1 >= 0:
			return True
		elif move == DOWN and posY + 1 < self.len:
			return True
		elif move == LEFT and posX - 1 >= 0:
			return True
		elif move == RIGHT and posX + 1 < self.len:
			return True
		return False


	def getF(openList):
		index = 0
		minF = openList[0].f
		for idx, move in enumerate(openList): # A modif pour prendre ne charge les maps
			if move.f < minF:
				minF = move.f
				index = idx
		return openList[index], index



	def astarAll(self, grid, solvedGrid):
		# Grid -> has neighboor, f, g, h
		# each neighboor has f g h too
		# self.neighbours = Neighbours(self.grid, self._getTile(0))

		openList = []
		closedList = []
		cameFrom = []
		openList.append(grid)

		while openList:

			current, index = self.getF(openList)
			if current == solvedGrid:
				return self.inversePath(cameFrom, current)
			openList.pop(index)
			closedList.append(current)

			for neighbour in current: # pour chaque possiblite de la position actuelle
				if neighbour in closedList:
					continue # Deja test
				elif neighbour not in openList:
					openList.append(neighbour)

				gTry = current.g # On recup le gscore general
				if gTry >= neighboor.g: # Comparaison du score general au prochain, le plus petit gagne
					continue

				cameFrom[neighboor] = current
				neighboor.g = gTry
				neighbour.f = gTry + 1

		return None



	def astarStep(self, grid, solvedGrid):
		pass
	def astarStepBack(self, grid, solvedGrid):
		pass






	def _handle_mouse(self, key):
		pass

	def handle_events(self, event_list):
		for event in event_list:
			if event.type in [MOUSEBUTTONDOWN, KEYUP]:
				if event.key == K_ESCAPE:
					self.done = True
				elif event.key in [K_UP, K_w, K_DOWN, K_s, K_LEFT, K_a, K_RIGHT, K_d]:
					self._handle_key(event.key)
				elif event.key == K_SPACE:
					self.astarAll(self.grid.grid, self.solvedGrid)
				elif event.key == K_n:
					self.astarStep(self.grid, self.solvedGrid)
				elif event.key == K_p:
					self.astarStepBack(self.grid, self.solvedGrid)
				elif event.type == MOUSEBUTTONDOWN:
					self._handle_mouse(event.key)
			
	def update_display(self):
		pygame.display.update()
		self.clock.tick(60)


	def run(self):
		while self.done is False:
			# Dessin de grille
			self.draw_grid(self.grid.grid)					

			# Actions user / resolve
			self.handle_events(pygame.event.get())

			# Update display
			self.update_display()		

		print ("Game exited. Thanks for playing")
		sys.exit(0)
