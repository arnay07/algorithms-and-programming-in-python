#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`console_main` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH 

:date: 03/10/2019


"""

from minesweeper import *
import sys


def main():
    """
    main function for console minesweeper game
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

    trace_grid(game)
    
    while game.get_state() == GameState.unfinished:
        
        x ,y ,action = input("Your play x,y,C (C=(R)eveal,(S)et,(U)nset): ").split(',')
        
        while not game.cell_in_grid(int(x),int(y)) or not action in {'R', 'S', 'U'}:
            if not game.cell_in_grid(int(x),int(y)):
                print('(x,y) must in the grid')
            else:
                print('C must be R for reveal or S for set or U for unset\n')
            x,y,action = input("Your play x,y,C (C=(R)eveal,(S)et,(U)nset): ").split(',')

        if action == 'R':
            game.reveal_all_cells_from(int(x),int(y))
        elif action == 'S':
            game.get_cell(int(x), int(y)).set_hypothetic()
        elif action == 'U':
            game.get_cell(int(x), int(y)).unset_hypothetic()
            
        trace_grid(game)
        
        if game.get_state() == GameState.losing:
            print('You lose!')
        elif game.get_state() == GameState.winning:
            print('You win!')




def trace_line(width):
    """
    Trace the lines in the grid
    
    :param width: the width of the grid
    :type width: int
    """
    print(' ', end='')
    for i in range(width):
        print('+---', end='')
    print('+')



def trace_grid(game):
    """
    Display the console of the game on the console
    
    :param game: a Minesweeper game
    :type game: Minesweeper
    """
    print(' ',end='')
    for i in range(game.get_width()):
        print("{:4d}".format(i), end='')
    print('')    
    trace_line(game.get_width())

    for i in range(game.get_height()):
        print('{}|'.format(i), end='')
        for j in range(game.get_width()):
            print(' {} |'.format(game.get_cell(j,i)) ,end='')
        print('')
        trace_line(game.get_width())
    
    
    
    


    
if __name__ == '__main__':
    main()


