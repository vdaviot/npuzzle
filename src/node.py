UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


# Etape
# 1 - Creer les neighbours a l'init, leur donner un poids de 1 hgf
# 2 - Apres chaque move, recalcul des neighbours, reatribution du hgf


# F G H
class Neighbours():

	def __init__(self, grid, pos, len):
		# hr = fgh for each neighbours
		# n = neighbours
		self.len = len
		self.grid = grid

		self.hr = dict({'right': {'n': self.getNeighbours('right', self.grid, pos), 'f': 1, 'g': 1, 'h': 1}})
		self.hr.update({'left': {'n': self.getNeighbours('left', self.grid, pos), 'f': 1, 'g': 1, 'h': 1}})
		self.hr.update({'top': {'n': self.getNeighbours('top', self.grid, pos), 'f': 1, 'g': 1, 'h': 1}})
		self.hr.update({'bottom': {'n': self.getNeighbours('bottom', self.grid, pos), 'f': 1, 'g': 1, 'h': 1}})


	def getNeighbours(self, move, grid, pos):
		updated_grid = [row[:] for row in grid]
		# pos[0] = x pos[1] = y
		if move == 'right' and pos[0] + 1 < self.len:
			updated_grid[pos[0]][pos[1]], updated_grid[pos[0]][pos[1] + 1] = updated_grid[pos[0]][pos[1] + 1], updated_grid[pos[0]][pos[1]]
		elif move == 'left' and pos[0] - 1 >= 0:
			updated_grid[pos[0]][pos[1]], updated_grid[pos[0]][pos[1] - 1] = updated_grid[pos[0]][pos[1] - 1], updated_grid[pos[0]][pos[1]]
		elif move == 'top' and pos[1] - 1 >= 0:
			updated_grid[pos[0]][pos[1]], updated_grid[pos[0] - 1][pos[1]] = updated_grid[pos[0] - 1][pos[1]], updated_grid[pos[0]][pos[1]]
		elif move == 'bottom' and pos[1] + 1 < self.len:
			updated_grid[pos[0]][pos[1]], updated_grid[pos[0] + 1][pos[1]] = updated_grid[pos[0] + 1][pos[1]], updated_grid[pos[0]][pos[1]]
		return updated_grid

	def updateNodes(self, grid, pos):
		self.grid = grid

		print
		for direction in ['right', 'left', 'top', 'bottom']:
			try:
				self.hr.update({direction: {'n': self.getNeighbours(direction, self.grid, pos)}})
			except:
				self.hr.update({direction: {'n': None}})
			finally:
				print self.hr[direction]['n']
		print


