from game import Game
import re, pygame

class Board(Game): # Ok

	# Parsing given puzzle
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
		return [[int(x) for x in y] for y in new_grid]

	# Grid generation if no puzzle given
	def _generate_npuzzle(self, len_grid, grid=None, solvable=True):
		if grid is None:
			self.lenX, self.lenY = len_grid, len_grid
			# Genere une liste random sans repetition
			piece_list = random.sample(range(len_grid * len_grid), len_grid * len_grid)
			# Split en len_grid col
			split = [piece_list[i::len_grid] for i in range(len_grid)]
			# Renvoi du constructeur
			return [[int(x) for x in y] for y in split]

		return self._parse_npuzzle(grid)


	# Return solved version of the board
	def _getSolved(self):
		np = range(0, self.lenX * self.lenX)
		return [[np.pop(0) for x in range(self.lenX)] for y in range(self.lenX)]

	# Comparison method
	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	# Print method
	# def __str__(self):
	# 	return '\n'.join(' '.join(str(col) for col in row) for row in self.grid) if self.grid else "Empty grid\n"

	# Board initiatialisation
	def __init__(self, len_grid, grid, solved=False):
		self.lenX, self.lenY = len_grid, len_grid
		self.grid = self._generate_npuzzle(len_grid, grid=grid) if not solved else self._getSolved()
		self.f, self.g, self.h = 1, 1, 1
		
		print("Puzzle of size {}x{}.\n".format(self.lenX, self.lenY))
		print(self.__str__() + '\n')

