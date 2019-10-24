=========================
:mod:`minesweeper` module
=========================

:doc:`back <index>`

.. automodule:: minesweeper
      
Ce module définit des classes et fonctions auxiliaires pour gérer le plateau du jeu de démineur.


Class description
=================

Une classe pour définir un type énuméré pour l'état du jeu.


La classe :class:`GameState`
----------------------------

.. autoclass:: GameState
   :members:	       
	       
Les trois états possibles du jeu : gagnant (winning), perdant (losing), ou inachevé (unfinished) sont décrits par trois attributs de mêmes noms.
			   
La classe :class:`Minesweeper`
------------------------------   

.. autoclass:: Minesweeper
   :members: get_height, get_width, get_nbombs, get_cell, get_state,
	     cell_in_grid, reveal_all_cells_from


Méthode spéciale
~~~~~~~~~~~~~~~~

.. automethod:: Minesweeper.__init__

