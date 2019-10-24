==================
:mod:`cell` module
==================

:doc:`back <index>`

.. automodule:: cell
		
Ce module définit une classe pour représenter les cellules (ou cases) d'un plateau de
jeu de démineur.

Une cellule peut être

* cachée ou révélée (ou encore découverte)
* elle peut ou non contenir une bombe
* son voisinage (les cellules voisines) contient un certain nombre de bombes
* elle peut avoir été jugée comme contenant hypothétiquement une bombe.


.. autoclass:: Cell
   :members: is_revealed, reveal, is_bomb, set_bomb, is_hypothetic,
	     set_hypothetic, unset_hypothetic,
	     number_of_bombs_in_neighborhood,
	     incr_number_of_bombs_in_neighborhood


méthodes spéciales
~~~~~~~~~~~~~~~~~~

.. automethod:: Cell.__init__
.. automethod:: Cell.__str__		
		



