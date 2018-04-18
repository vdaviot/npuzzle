# UTILISE LE coding: utf-8 !
import pygame, sys, random
from pygame.locals import *
from node import Neighbours

DIRECTION = ['right', 'left', 'top', 'bottom']
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

class Game(object):

	def __init__(self, grid, solvedGrid, len=3, interactive=True):
		# Interactive False = Bench mode
		self.grid = grid
		self.solvedGrid = solvedGrid
		self.done = False
		self.len = len
		self.options = {
			'interactive': interactive,
			}
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
		self.x, self.y = self._getTile(0)
		self.nb = Neighbours(self.grid.grid, (self.x, self.y), self.len)
		self.snb = Neighbours(self.solvedGrid.grid, (0, 0), self.len)



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


	def gridAfterMove(self, move, posX, posY):
		new_grid = [row[:] for row in self.grid]
		if move == 'right':
			new_grid[posY][posX], new_grid[posY][posX + 1] = new_grid[posY][posX + 1], new_grid[posY][posX]
		elif move == 'left':
			new_grid[posY][posX], new_grid[posY][posX - 1] = new_grid[posY][posX - 1], new_grid[posY][posX]
		elif move == 'top':
			new_grid[posY][posX], new_grid[posY - 1][posX] = new_grid[posY - 1][posX], new_grid[posY][posX]
		elif move == 'bottom':
			new_grid[posY][posX], new_grid[posY + 1][posX] = new_grid[posY + 1][posX], new_grid[posY][posX]
		return new_grid

	def _handle_key(self, key):
		 # Get 0 tile posX, posY
		if key in [K_UP, K_w] and self._isValidMove(UP):
			self.grid.grid[self.y][self.x], self.grid.grid[self.y - 1][self.x] = self.grid.grid[self.y - 1][self.x], self.grid.grid[self.y][self.x]

		elif key in [K_DOWN, K_s] and self._isValidMove(DOWN):
			self.grid.grid[self.y][self.x], self.grid.grid[self.y + 1][self.x] = self.grid.grid[self.y + 1][self.x], self.grid.grid[self.y][self.x]

		elif key in [K_LEFT, K_a] and self._isValidMove(LEFT):
			self.grid.grid[self.y][self.x], self.grid.grid[self.y][self.x - 1] = self.grid.grid[self.y][self.x - 1], self.grid.grid[self.y][self.x]

		elif key in [K_RIGHT, K_d] and self._isValidMove(RIGHT):
			self.grid.grid[self.y][self.x], self.grid.grid[self.y][self.x + 1] = self.grid.grid[self.y][self.x + 1], self.grid.grid[self.y][self.x]

	def _getTile(self, tile, grid=None):
		for idy, row in enumerate(self.grid.grid if grid == None else grid):
			for idx, col in enumerate(row):
				if col == tile:
					return idx, idy


	def _isValidMove(self, move):
		if  move == UP and self.y - 1 >= 0 or \
			move == DOWN and self.y + 1 < self.len or \
			move == LEFT and self.x - 1 >= 0 or \
			move == RIGHT and self.x + 1 < self.len:
			return True
		return False


	# use with len > 2
	def manhattanDistance(self, gridFrom, gridTo):
		xA, yA = self._getTile(0, gridFrom)
		xB, yB = self._getTile(0, gridTo)
		return abs(xB - xA) + abs(yB - yA)

	# Use with len 1 or 2
	def uniformCost(self):
		return 0

	def stringify(self, grid):
		return ''.join(' '.join(str(col) for col in row) for row in grid)

	def getF(self, openList, fScore):
		index = 0
		minF = fScore[openList[0].__str__]
		for idx, option in enumerate(openList):
			try:
				if fScore[option.__str__] < minF:
					minF = fScore[option.__str__]
				index = idx
			except:
				pass
		return openList[index], index


	def astarAll(self, grid, solvedGrid):
		# grid = Instance de neighbours

		# case de dict -> stringify

		openList = []
		closedList = []
		cameFrom = []
		gScore = {}
		fScore = {}

		gScore[grid.__str__] = 0
		fScore[grid.__str__] = self.manhattanDistance(grid.grid, solvedGrid.grid)

		openList.append(grid)
		print "APPENDED {}".format(grid.__class__)
		while openList:
			# Get lowest f value
			current, index = self.getF(openList, fScore)

			# If the grid is in resolved state
			if current.grid == solvedGrid.grid:
				return self.inversePath(cameFrom, current)

			# Pop the lowest f, added to tried options
			openList.pop(index)
			closedList.append(current)

			for direction in DIRECTION:
				nb = current.hr[direction]['n']
				# If already tested, jump
				if nb in closedList:
					continue

				# If not tested, append
				if nb not in openList:
					n = Neighbours(nb, self._getTile(0, nb), self.len)
					openList.append(n)
					print "APPENDED {}".format(n.__class__)

				tryGscore = int(gScore[current.__str__] + self.manhattanDistance(current.grid, nb))
				strNb = self.stringify(nb)

				if tryGscore >= self.manhattanDistance(nb, solvedGrid.grid):
					continue # Not the best path

				# Best path found
				gScore[strNb] = int(tryGscore)
				fScore[strNb] = gScore[strNb] + self.manhattanDistance(nb, solvedGrid.grid)

				print "openList:\n"
				for thing in enumerate(openList):
					print "{}".format(thing.__class__)
				print
				print "closedList:\n"
				for thing in enumerate(openList):
					print "{}".format(thing.__class__)
				print
				print "gScore:\n"
				for key, thing in gScore.items():
					print "({}) [{}]->{}".format(thing.__class__, key, thing)
				print
				print "fScore:\n"
				for key, thing in fScore.items():
					print "({}) [{}]->{}".format(thing.__class__, key, thing)
				print

		return None

	def handle_events(self, event_list):
		for event in event_list:
			if event.type in [MOUSEBUTTONDOWN, KEYUP]:
				if event.key == K_ESCAPE:
					self.done = True
				elif event.key in [K_UP, K_w, K_DOWN, K_s, K_LEFT, K_a, K_RIGHT, K_d]:
					self._handle_key(event.key)
				elif event.key == K_SPACE:
					self.astarAll(self.nb, self.snb)
				self.x, self.y = self._getTile(0)
				self.nb.updateNodes(self.grid.grid, (self.x, self.y))

			
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

		print("Game exited. Thanks for playing")
		sys.exit(0)
