# TODO nPuzzle

Parsing: 

	Ne pas parser les commentaires (# et \**\) -> Done
	Generateur fournit -> Parsing OK
	Generateur perso -> Parsing OK / Generation OK-ish -> Pas de choix de solvable / unsolvable
	Ajouter option Benchmark -> Done

Visuel:
	
	Plateau de jeu pygame -> Done
	Catch les event de la fenetre -> Done
	Animation pour chaque action

Erreur:

	Erreur parsing (Fichier vide/Pas de params/Binaire/Dossier) -> Done ? -> A ameliorer avec classe gestion d'erreur
	Erreur resolution

Resolution:

	3 Heuristiques minimum (Manhattan-distance obligatoire, les autres aux choix)
	Mode resolution (1action/s) et mode benchmark avec sortie temps / nombre de move
	Sortie mode resolution multi heuristique si demande

Sortie:

	Valeurs a fournir:

		Nombre total de state pour la resolution (complexite / temps)
		Nombre de mouvement avant resolution
		Ordre des states
		Solvable ou pas

	

