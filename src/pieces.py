import pygame, random, sys, re, argparse
from pygame.locals import *


class Game(object):

	def _solve(self, grid):
		pass

	def __init__(self, grid, len=3, interactive=True):
		# Interactive False = Bench mode
		self.grid = grid
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
			self.font = pygame.font.SysFont('Arial', self.screenX / 10)
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
		color_r = (0, 0, 0) # Temporary
		for row in range(len(board)):
			for col in range(len(board[0])):
				posX, posY, sizeX, sizeY = self.calcPadding(row, col)
				pygame.draw.rect(self.screen, color_r, (posX, posY, sizeX, sizeY))
				self.screen.blit(self.font.render(str(board[row][col].value), True, color_f), (posX, posY))

	def _getMovingTile(self):
		for line in self.grid.grid:
			for col in line:
				if col.moving == True:
					print col.value
					return col.posX, col.posY

	def _setMovingTile(self):
		for line in self.grid.grid:
			for col in line:
				col.moving = False if col.value != 0 else True

	def _canMove(self, posX, posY):
		if posX < 0 or posY < 0 or posX >= self.len or posY >= self.len and self.grid.grid[posX][posY].value != 0:
			return False
		return True

	def _handle_key(self, key): # Probleme ici, le check de position ne fonctionne pas correctement
	
		posX, posY = self._getMovingTile() # Get 0 tile posX, posY

		print(posX, posY)

		if key == K_UP and self._canMove(posX - 1, posY):
			self.grid.grid[posX][posY], self.grid.grid[posX - 1][posY] = self.grid.grid[posX - 1][posY], self.grid.grid[posX][posY]
			# self.grid.grid[posX][posY].moving, self.grid.grid[posX - 1][posY].moving = True, False

		elif key == K_DOWN and self._canMove(posX + 1, posY):
			self.grid.grid[posX][posY], self.grid.grid[posX + 1][posY] = self.grid.grid[posX + 1][posY], self.grid.grid[posX][posY]

		elif key == K_LEFT and self._canMove(posX, posY - 1):
			self.grid.grid[posX][posY], self.grid.grid[posX][posY - 1] = self.grid.grid[posX][posY - 1], self.grid.grid[posX][posY]

		elif key == K_RIGHT and self._canMove(posX, posY + 1):
			self.grid.grid[posX][posY], self.grid.grid[posX][posY + 1] = self.grid.grid[posX][posY + 1], self.grid.grid[posX][posY]

		self._setMovingTile()
		print(self.grid)

	def _handle_mouse(self, key):
		pass

	def handle_events(self, event_list):
		for event in event_list:
			if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
				if event.key == K_ESCAPE:
					self.done = True
				elif event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
					self._handle_key(event.key)
				elif event.type == MOUSEBUTTONDOWN:
					self._handle_mouse(event.key)
			
	def update_display(self):
		pygame.display.update()
		self.clock.tick(60)

	def run(self):
		while game.done is False:
			# Dessin de grille
			self.draw_grid(self.grid.grid)					

			# Actions user / resolve
			self.handle_events(pygame.event.get())

			# Update display
			self.update_display()			

		print ("Game exited. Thanks for playing")
		sys.exit(0)

class Board(Game):

	# Generation de puzzle si aucun fournit
	def _parse_npuzzle(self, grid_file):
		new_grid = list()
		try:
			real_len = 0
			with open(grid_file, 'r+') as fd:

				# On enleve les commentaires potentiels
				reg = re.compile("#.*")
				for line in fd.readlines(): # Peu etre opti
					content = re.sub(reg, "", line).strip().split()
					if not content: # Si commentaire
						continue
					actual_len = len(content)
					if actual_len <= 2:
						real_len = int(content[0])
						continue
					elif actual_len != real_len:
						print("Wrong file format.")
						sys.exit(0)
					new_grid.append(content)


		except IOError:
			print("Can't open file. It may be a directory, binary or the file does not exist.")
			sys.exit(0)

		# Renvoi du constructeur
		self.lenX, self.lenY = actual_len, actual_len
		return [[Piece(int(x), idxy, idxx) for idxx, x in enumerate(y)] for idxy, y in enumerate(new_grid)]



	# Generation de grid len_grid*len_grid
	def _generate_npuzzle(self, len_grid, grid=None, solvable=True):
		if grid is None:
			self.lenX, self.lenY = len_grid, len_grid
			# Genere une liste random sans repetition
			piece_list = random.sample(range(len_grid * len_grid), len_grid * len_grid)
			# Split en len_grid col
			split = [piece_list[i::len_grid] for i in range(len_grid)]
			# Renvoi du constructeur
			return [[Piece(int(x), idxy, idxx) for idxx, x in enumerate(y)] for idxy, y in enumerate(split)]

		return self._parse_npuzzle(grid)



	def __init__(self, len_grid, grid=None):
		self.grid = self._generate_npuzzle(len_grid, grid=grid)
		print("Puzzle of size {}x{}.\n".format(self.lenX, self.lenY))

	def __str__(self):
		return '\n'.join(' '.join(str(col.value) for col in row) for row in self.grid) if self.grid else "Empty grid\n"

class Piece(Board):

	def __init__(self, x, posX, posY):
		self.value = abs(x)
		self.moving = True if x == 0 else False
		self.posX = posX
		self.posY = posY
		self.weight = 1

	def __str__(self):
		return str(self.value)



if __name__ == '__main__':
	# A recup: Soit taille (-g | --generate) soit fichier (-m | --map)
	parser = argparse.ArgumentParser(description='Npuzzle solver.', prog="Npuzzle") 
	parser.add_argument('-p', '--puzzle', help="Puzzle to solve", default=argparse.SUPPRESS)
	parser.add_argument('-g', '--generate', help="X/Y size of the generated map. (Pointless with -p option)", type=int, default=0, choices=range(1, 10))
	parser.add_argument('-b', '--bench', help="Mode benchmark. Disable visual and game aspect.", action='store_false')
	args = parser.parse_args()

	try:
		puzzle = args.puzzle
		iMode = args.bench
	except AttributeError:
		puzzle = None
	finally:
		size = 3 if (args.generate == 0) else args.generate

	grid = Board(size, puzzle)
	print(grid)

	game = Game(grid, grid.lenX, iMode)
	game.run()


