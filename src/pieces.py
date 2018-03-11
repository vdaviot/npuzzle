import pygame, random, sys, re, argparse


class Game(object):

	def __init__(self):
		pass

class Board(Game):

	# Generation de puzzle si aucun fournit
	def _parse_npuzzle(self, grid_file):
		new_grid = list()
		with open(grid_file, 'r+') as fd:
			# On enleve les commentaires potentiels
			reg = re.compile("#.*")
			for line in fd.readlines()[1:]:
				# Strip d'espaces en trop
				new_grid.append(re.sub(reg, "", line).strip().replace(" ", ""))

		# Renvoi du constructeur
		grid_len = len(new_grid[1:])
		self.lenX, self.lenY = grid_len, grid_len
		return [[Piece(x, idxx, idxy) for idxx, x in enumerate(y)] for idxy, y in enumerate(new_grid[1:])]


	# Generation de grid
	def _generate_npuzzle(self, len_grid, grid=None, solvable=True):
		if grid is None:
			self.lenX, self.lenY = len_grid, len_grid
			# Genere une liste random sans repetition
			piece_list = random.sample(range(len_grid * len_grid), len_grid * len_grid)
			# Split en len_grid col
			split = [piece_list[i::len_grid] for i in range(len_grid)]
			# Renvoi du constructeur
			return [[Piece(x, idxx, idxy) for idxx, x in enumerate(y)] for idxy, y in enumerate(split)]

		return self._parse_npuzzle(grid)

	def __init__(self, len_grid, grid=None):
		self.grid = self._generate_npuzzle(len_grid, grid=grid)
		print("Puzzle of size {}x{}.\n".format(self.lenX, self.lenY))


	def __str__(self):
		return '\n'.join(' '.join(str(col.value) for col in row) for row in self.grid)

	def __del__(self):
		pass


class Piece(Board):

	def __init__(self, x, posX, posY):
		self.value = abs(int(x))
		self.posX = posX
		self.posY = posY
		self.weight = 1

	def __str__(self):
		return self.value

	def __del__(self):
		pass


if __name__ == '__main__':
	# A recup: Soit taille (-g | --generate) soit fichier (-m | --map)
	parser = argparse.ArgumentParser(description='Npuzzle solver.', prog="Npuzzle") 
	parser.add_argument('-p', '--puzzle', help="Puzzle to solve", default=argparse.SUPPRESS)
	parser.add_argument('-g', '--generate', help="X/Y size of the generated map. (Pointless with -p option)", type=int, default=0, choices=range(1, 10))
	args = parser.parse_args()

	try:
		puzzle = args.puzzle
	except AttributeError:
		puzzle = None
	finally:
		size = 3 if (args.generate == 0) else args.generate
		
	grid = Board(size, puzzle)
	print(grid)


