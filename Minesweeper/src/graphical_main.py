#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`main` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date:  2019, september. Last revision: 2019, september

Main module to play the minesweeper's game : graphical version


"""

import sys
from minesweeper import Minesweeper
import graphicalboard

def main():
    """
    main function for graphical minesweeper game
    """
    if len(sys.argv) == 4:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        nbombs = int(sys.argv[3])
    else:
        width = 8
        height = 8
        nbombs = 10
    game = Minesweeper(width, height, nbombs)
    graphicalboard.create(game)

if __name__ == '__main__':
    main()


