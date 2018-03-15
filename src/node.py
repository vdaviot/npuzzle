UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

class Neighbours():

	def __init__(self, grid, pos):
		self.grid = grid
		self.setNodes(grid, pos)

	def setGrid(self, grid):
		self.grid = grid

	def setPos(self, pos):
		self.posX, self.pos.y = pos.x, pos.y

	def setNodes(self, grid, pos):
		try:
			del self.neighbours
		except:
			pass
		self.neighbours = [Node(grid, LEFT, (pos.x - 1, pos.y)), Node(grid, RIGHT, (pos.x + 1, pos.y)), \
		Node(grid, UP, (pos.x, pos.y - 1)), Node(grid, DOWN, (pos.x, pos.y + 1))]

		self.setPos(pos)
		self.setGrid(grid)


	class Node():

		def gridAfterMove(self, move, grid, pos):
			new_grid = [row[:] for row in grid]
			if move == 'right':
				new_grid[pos.y][pos.x], new_grid[pos.y][pos.x + 1] = new_grid[pos.y][pos.x + 1], new_grid[pos.y][pos.x]
			elif move == 'left':
				new_grid[pos.y][pos.x], new_grid[pos.y][pos.x - 1] = new_grid[pos.y][pos.x - 1], new_grid[pos.y][pos.x]
			elif move == 'top':
				new_grid[pos.y][pos.x], new_grid[pos.y - 1][pos.x] = new_grid[pos.y - 1][pos.x], new_grid[pos.y][pos.x]
			elif move == 'bottom':
				new_grid[pos.y][pos.x], new_grid[pos.y + 1][pos.x] = new_grid[pos.y + 1][pos.x], new_grid[pos.y][pos.x]
			return new_grid

		def __eq__(self, other):
			return self.__dict__ == other.__dict__

		def __init__(self, move, grid, pos):
			self.f, self.g, self.h = 1, 1, 1
			self.grid = self.gridAfterMove(move, grid, pos)
