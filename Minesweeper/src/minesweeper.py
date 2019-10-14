
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`minesweeper` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH

:date: 14/10/2019

This module provides functions and a class for minesweeper's game's management.

"""

import random
from enum import Enum
from cell import Cell


################################################
# Type declaration
################################################

class GameState(Enum):
    """
    A class to define an enumerated type with three values :

    * ``winning``
    * ``losing``
    * ``unfinished``

    for the three state of minesweeper game.
    """
    winning = 1
    losing = 2
    unfinished = 3


##############################################
# Function for game's setup and management
##############################################


def neighborhood(x, y, width, height):
    """
    :param x: x-coordinate of a cell
    :type x: int
    :param y: y-coordinate of a cell
    :type y: int
    :param height: height of the grid
    :type height: int
    :param width: widthof the grid
    :type width: int
    :return: the list of coordinates of the neighbors of position (x,y) in a
             grid of size width*height
    :rtype: list of tuple
    :UC: 0 <= x < width and 0 <= y < height
    :Examples:

    >>> neighborhood(3, 3, 10, 10)
    [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]
    >>> neighborhood(0, 3, 10, 10)
    [(0, 2), (0, 4), (1, 2), (1, 3), (1, 4)]
    >>> neighborhood(0, 0, 10, 10)
    [(0, 1), (1, 0), (1, 1)]
    >>> neighborhood(9, 9, 10, 10)
    [(8, 8), (8, 9), (9, 8)]
    >>> neighborhood(3, 9, 10, 10)
    [(2, 8), (2, 9), (3, 8), (4, 8), (4, 9)]
    """
    neighbors = []

    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i != width and j != height and i>=0 and j>=0 and (i,j) != (x,y):
                neighbors.append((i,j))

    return neighbors
            
   
    


class Minesweeper():
    """
    >>> game = Minesweeper(20, 10, 4)
    >>> game.get_width()
    20
    >>> game.get_height()
    10
    >>> game.get_nbombs()
    4
    >>> game.get_state() == GameState.unfinished 
    True
    >>> cel = game.get_cell(1, 2)
    >>> cel.is_revealed()
    False
    >>> 
    """

    number_of_cells_revealed = 0

    def __init__(self, width=30, height=20, nbombs=99):
        """
        build a minesweeper grid of size width*height cells
        with nbombs bombs randomly placed.  

        :param width:[optional] horizontal size of game (default = 30)
        :type width: int
        :param height: [optional] vertical size of game (default = 20)
        :type height: int
        :param nbombs: [optional] number of bombs (default = 99)
        :type nbombs: int
        :return: a fresh grid of  width*height cells with nbombs bombs randomly placed.
        :rtype: Minesweeper
        :UC: width and height must be positive integers, and
             nbombs <= width * height
        :Example:

        >>> game = Minesweeper(20, 10, 4)
        >>> game.get_width()
        20

        10
        >>> game.get_nbombs()
        4
        >>> game.get_state() == GameState.unfinished 
        True
        """

        assert 0 <= nbombs <= width*height, "the number of bombs must be inferior to the area of the grid and superior or equal to 0"

        
        
        self.width = width
        self.height = height
        self.nbombs = nbombs
        self.gamestate = GameState.unfinished
        self.grid = {(i,j): Cell() for i in range(self.width) for j in range(self.height)}
            
        cells_with_bombs = []
        number_of_bombs = self.nbombs

        
        while number_of_bombs > 0:
            bomb = (random.randint(0,width-1), random.randint(0,height-1))
            if bomb not in cells_with_bombs:
                self.grid[bomb].set_bomb()
                cells_in_neighborhood = neighborhood(bomb[0],bomb[1],self.width, self.height)
                for cells in cells_in_neighborhood:
                    self.grid[cells].incr_number_of_bombs_in_neighborhood()
                cells_with_bombs.append(bomb)
                number_of_bombs -=  1
        
        
        
                
        

    def get_height(self):
        """
        :return: height of the grid in self
        :rtype: int
        :UC: none
        """
        return self.height


    def get_width(self):
        """
        :return: width of the grid in game
        :rtype: int
        :UC: none
            """

        return self.width

    
    def get_nbombs(self):
        """
        :return: number of bombs in game
        :rtype: int
        :UC: none
        """

        return self.nbombs



    def get_cell(self, x, y):
        """
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: the cell of coordinates (x,y) in the game's grid
        :type: cell
        :UC: 0 <= x < width of game and O <= y < height of game
        """
        assert 0 <= x < self.width and 0 <= y < self.height, "cell must be in the grid"
        
        return self.grid[(x,y)]

    


    def get_state(self):
        """
        :return: the state of the game (winning, losing or unfinished)
        :rtype: GameState
        :UC: none
        """
        
        
        return self.gamestate


    

    def cell_in_grid(self,x,y):
        """
        Check if the cell is in the  grid
        
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: True if the cell is in the grid and False otherwise
        :rtype: boolean
        :UC: none
        """

        try:
            self.get_cell(x,y)
            return True
        except AssertionError:
            return False
        



    def reveal_all_cells_from(self, x, y):
        """
        :param x: x-coordinate
        :param y: y-coordinate
        :return: none
        :side effect: reveal all cells of game game from the initial cell (x,y).
        :UC: 0 <= x < width of game and O <= y < height of game
        """

        if self.cell_in_grid(x,y) and not self.get_cell(x,y).is_revealed():
            
            self.get_cell(x,y).reveal()
            self.number_of_cells_revealed += 1

            if self.get_cell(x,y).is_bomb():
                for case in self.grid.values():
                    if case.is_bomb():
                        case.reveal()
                self.gamestate = GameState.losing
            
            
            elif self.get_cell(x,y).number_of_bombs_in_neighborhood()==0:
                for cellule in neighborhood(x,y,self.get_width(), self.get_height()):
                    self.reveal_all_cells_from(cellule[0], cellule[1])
            
                  
                
            
        if self.number_of_cells_revealed == (self.get_width()*self.get_height()) - self.get_nbombs():
            self.gamestate = GameState.winning
       






            
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)


