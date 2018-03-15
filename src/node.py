UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

class Neighbours():

	def __init__(self, grid, pos):
		self.grid = grid
		self.setNodes(self.grid, pos)

	def setGrid(self, grid):
		self.grid = grid.grid

	def setPos(self, pos):
		self.posX, self.posY= pos[0], pos[1]

	def setNodes(self, grid, pos):
		self.neighbours = [Node(grid, LEFT, (pos[0] - 1, pos[1])), Node(grid, RIGHT, (pos[0] + 1, pos[1])),	Node(grid, UP, (pos[0], pos[1] - 1)), Node(grid, DOWN, (pos[0], pos[1] + 1))]

		self.setPos(pos)
		self.setGrid(grid)


class Node():

	def gridAfterMove(self, move, grid, pos):
		print "GRID: "
		print grid
		new_grid = [row[:] for row in grid]
		if move == 'right':
			new_grid[pos[0]][pos[1]], new_grid[pos[0]][pos[1] + 1] = new_grid[pos[0]][pos[1] + 1], new_grid[pos[0]][pos[1]]
		elif move == 'left':
			new_grid[pos[0]][pos[1]], new_grid[pos[0]][pos[1] - 1] = new_grid[pos[0]][pos[1] - 1], new_grid[pos[0]][pos[1]]
		elif move == 'top':
			new_grid[pos[0]][pos[1]], new_grid[pos[0] - 1][pos[1]] = new_grid[pos[0] - 1][pos[1]], new_grid[pos[0]][pos[1]]
		elif move == 'bottom':
			new_grid[pos[0]][pos[1]], new_grid[pos[0] + 1][pos[1]] = new_grid[pos[0] + 1][pos[1]], new_grid[pos[0]][pos[1]]
		return new_grid

	# def __eq__(self, other):
	# 	return self.__dict__ == other.__dict__

	def __init__(self, grid, move, pos):
		self.f, self.g, self.h = 1, 1, 1
		self.grid = self.gridAfterMove(move, grid, pos)
