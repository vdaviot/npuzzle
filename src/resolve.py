# F = sum of the cost to reach node
# G = sum of the cost to travel from parent
# H = heuristic
import cython

def manhattanDistance(self, start, end):# start et end sont des pairs de coords
	sx, sy = start
	ex, ey = end
	return abs(ex - sz) + abs(ey - sy)

def getLowestF(openList): # A trouver comment ajouter la liste des state a openList
	index = 0
	minF = openList[0].f
	for idx, move in enumerate(openList): # A modif pour prendre ne charge les maps
		if move.f < minF:
			minF = move.f
			index = idx
	return openList[index], index

def inversePath(cameFrom, current):
	final_path = []
	while current in cameFrom:
		current = cameFrom[current]
		final_path.append(current)
	return final_path


def astar(start, end):

	openList = []
	closedList = []
	cameFrom = []
	openList.append(start) # On ajoute le state de base a la liste

	while openList:

		current, index = getLowestF(openList)
		if current == end: # Si le state actuel est le final
			return inversePath(cameFrom, current) # On reconstitue le parcours
		openList.pop(index) # On retire les state testé
		closedList(current) # On retire les state testé

		# Jusqu'ici devrait fonctionner
		# Manque methode pour generer les neighbour

		for neighbor in current: # Pour chaque voisin
			if neighbor in closedList:
				continue
			elif neighbor not in openList:
				openList.append(neighbor) # On ajoute dans la liste a tester

			gTentative = current.g + 1 # On cherche la meilleur solution (1 a remplacer)
			if gTentative >= neighbor.g:
				continue # Pas la meilleur donc on continue a iterer

			cameFrom[neighbor] = current
			neighbor.g = gTentative
			neighbor.f = neighbor.g + 1 # (1 a remplacer)

	return None




solved = Astar(self.grid, self.solvedGrid)
if solved is None:
	print("Unsolvable puzzle given.")
print solved
