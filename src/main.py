import pygame, random, sys, re, argparse
from pygame.locals import *
from src import *
# from src.board import Board

if __name__ == '__main__':
	# A recup: Soit taille (-g | --generate) soit fichier (-m | --map)
	parser = argparse.ArgumentParser(description='Npuzzle solver.', prog="Npuzzle") 
	parser.add_argument('-p', '--puzzle', help="Puzzle to solve", default=argparse.SUPPRESS)
	parser.add_argument('-g', '--generate', help="X/Y size of the generated map. (Pointless with -p option)", type=int, default=0, choices=range(1, 10))
	parser.add_argument('-b', '--bench', help="Mode benchmark. Disable visual and game aspect.", action='store_false')
	args = parser.parse_args()

	try:
		puzzle = args.puzzle
	except AttributeError:
		puzzle = None
	finally:
		size = 3 if (args.generate == 0) else args.generate
		iMode = args.bench

	grid = Board(size, puzzle, False)
	solvedGrid = Board(size, puzzle, True)

	game = Game(grid, solvedGrid, grid.lenX, iMode)
	game.run()


