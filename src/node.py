UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


# Etape
# 1 - Creer les neighbours a l'init, leur donner un poids de 1 hgf
# 2 - Apres chaque move, recalcul des neighbours, reatribution du hgf


# F G H
class Neighbours():

	def __init__(self, grid, pos):
		# hr = fgh for each neighbours
		# n = neighbours
		self.grid = grid

		self.hr = dict({'right': None, 'left': None, 'top': None, 'bottom': None})

		self.hr.update({'right': {'n': self.getNeighbours('right', self.grid, pos), 'f': 1, 'g': 1, 'h': 1}})
		self.hr.update({'left': {'n': self.getNeighbours('left', self.grid, pos), 'f': 1, 'g': 1, 'h': 1}})
		self.hr.update({'top': {'n': self.getNeighbours('top', self.grid, pos), 'f': 1, 'g': 1, 'h': 1}})
		self.hr.update({'bottom': {'n': self.getNeighbours('bottom', self.grid, pos), 'f': 1, 'g': 1, 'h': 1}})

		# for keys, values in self.hr.items():
		# 	print "{}: {}".format(keys, values)



	def getNeighbours(self, move, grid, pos):
		updated_grid = [row[:] for row in grid]
		if move == 'right':
			updated_grid[pos[0]][pos[1]], updated_grid[pos[0]][pos[1] + 1] = updated_grid[pos[0]][pos[1] + 1], updated_grid[pos[0]][pos[1]]
		elif move == 'left':
			updated_grid[pos[0]][pos[1]], updated_grid[pos[0]][pos[1] - 1] = updated_grid[pos[0]][pos[1] - 1], updated_grid[pos[0]][pos[1]]
		elif move == 'top':
			updated_grid[pos[0]][pos[1]], updated_grid[pos[0] - 1][pos[1]] = updated_grid[pos[0] - 1][pos[1]], updated_grid[pos[0]][pos[1]]
		elif move == 'bottom':
			updated_grid[pos[0]][pos[1]], updated_grid[pos[0] + 1][pos[1]] = updated_grid[pos[0] + 1][pos[1]], updated_grid[pos[0]][pos[1]]
		return updated_grid

	def updateNodes(self, pos):
		self.hr.update({'right': {'n': self.getNeighbours('right', self.grid, pos)}})
		self.hr.update({'left': {'n': self.getNeighbours('left', self.grid, pos)}})
		self.hr.update({'top': {'n': self.getNeighbours('top', self.grid, pos)}})
		self.hr.update({'bottom': {'n': self.getNeighbours('bottom', self.grid, pos)}})


