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
		self.grid = grid
		# hr = fgh for each neighbours
		self.hr = list({id: "right", f: 1, g: 1, h: 1}, {id: "left", f: 1, g: 1, h: 1}, {id: "top", f: 1, g: 1, h: 1}, {id: "bottom", f: 1, g: 1, h: 1})
		self.setNodes(pos)

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

	def update(self, grid, pos):
		self.grid = grid
		self.setNodes(pos)

	# n = neighbours
	def setNodes(self pos):
		self.posX, posY = pos[1], pos[0]
		self.rn, self.ln = self.getNeighbours('right', self.grid, pos), self.getNeighbours('left', self.grid, pos)
		self.tn, self.ln = self.getNeighbours('top', self.grid, pos), self.getNeighbours('bottom', self.grid, pos)
