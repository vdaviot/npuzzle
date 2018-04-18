UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


# Etape
# 1 - Creer les neighbours a l'init, leur donner un poids de 1 hgf
# 2 - Apres chaque move, recalcul des neighbours, reatribution du hgf

class Neighbours():

	def __init__(self, grid, pos, len):
		# hr = fgh for each neighbours
		# n = neighbours
		self.len = len
		self.grid = grid

		self.hr = dict({'right': {'n': self.getNeighbours('right', self.grid, pos)}})
		self.hr.update({'left': {'n': self.getNeighbours('left', self.grid, pos)}})
		self.hr.update({'top': {'n': self.getNeighbours('top', self.grid, pos)}})
		self.hr.update({'bottom': {'n': self.getNeighbours('bottom', self.grid, pos)}})


	def getNeighbours(self, move, grid, pos):
		updated_grid = [row[:] for row in grid]
		# pos = X, Y
		if  pos[0] + 1 >= self.len and move == 'right' or \
			pos[0] - 1 < 0 and move == 'left' or \
			pos[1] - 1 < 0 and move == 'top' or \
			pos[1] + 1 >= self.len and move == 'bottom':
			return None
		if move == 'right':
			updated_grid[pos[1]][pos[0]], updated_grid[pos[1]][pos[0] + 1] = updated_grid[pos[1]][pos[0] + 1], updated_grid[pos[1]][pos[0]]
		elif move == 'left':
			updated_grid[pos[1]][pos[0]], updated_grid[pos[1]][pos[0] - 1] = updated_grid[pos[1]][pos[0] - 1], updated_grid[pos[1]][pos[0]]
		elif move == 'top':
			updated_grid[pos[1]][pos[0]], updated_grid[pos[1] - 1][pos[0]] = updated_grid[pos[1] - 1][pos[0]], updated_grid[pos[1]][pos[0]]
		elif move == 'bottom':
			updated_grid[pos[1]][pos[0]], updated_grid[pos[1] + 1][pos[0]] = updated_grid[pos[1] + 1][pos[0]], updated_grid[pos[1]][pos[0]]
		return updated_grid

	def __str__(self):
		return ''.join(' '.join(str(col) for col in row) for row in self.grid)

	def updateNodes(self, grid, pos):
		self.grid = grid

		for direction in ['right', 'left', 'top', 'bottom']:
			self.hr.update({direction: {'n': self.getNeighbours(direction, self.grid, pos)}})
			# try:
		# except:
			# self.hr.update({direction: {'n': None}})
		# finally: # debug print
			print self.hr[direction]['n']
		print


