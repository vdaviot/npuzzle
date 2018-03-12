# TODO nPuzzle

Parsing: 

	Ne pas parser les commentaires (# et \**\) -> Done
	Generateur fournit -> Parsing OK
	Generateur perso -> Parsing OK / Generation OK-ish -> Pas de choix de solvable / unsolvable
	Ajouter option Benchmark -> En cours

Visuel:
	
	Plateau de jeu pygame -> Done
	Boutons user (start stop resolve restart)
	Catch les event de la fenetre
	Animation pour chaque action
	Mode resolution (1 action/s) avec temps et actions

Erreur:

	Erreur parsing (Fichier vide/Pas de params/Binaire/Dossier) -> Done ? -> A ameliorer avec classe gestion d'erreur
	Erreur resolution

Resolution:

	3 Heuristiques minimum (Manhattan-distance obligatoire, les autres aux choix)


Sortie:

	Valeurs a fournir:

		Nombre total de state pour la resolution (complexite / temps)
		Nombre de mouvement avant resolution
		Ordre des states
		Solvable ou pas

	

