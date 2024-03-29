#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`parentheses_checker1` module

:author: Arnaud Kaderi, Elhadj Ibrahima BAH


:date: 2019, october
:last revision: 07/11/2019 

"""


from stack import *
import sys

PARENTHESES = {'(':')','[':']','{':'}'}


def parentheses_checker():
    """
    Checks if the program in the file is well parenthesed
    and print Well parenthesed if true or Bad parenthesed if false

    :returns: none
    :UC: none

    """

    global PARENTHESES

    assert len(sys.argv)==2,'the number of files to check must be one'

    file = sys.argv[1]

    line_stack = Stack()

    open_file = open(file, 'r')

    line_read = open_file.readline()

    bad_parentheses = False

    while(line_read != '' and not bad_parentheses):
        i = 0
        while(i <len(line_read) and not bad_parentheses):
            if line_read[i] in {'(',')','[',']','{','}'}:
                if line_read[i] in PARENTHESES.keys():
                    line_stack.push(line_read[i])
                elif not line_stack.is_empty() and PARENTHESES[line_stack.top()] == line_read[i]:
                    line_stack.pop()
                else:
                    bad_parentheses = True
            i+=1
        line_read = open_file.readline()
    open_file.close()
    if bad_parentheses or not line_stack.is_empty():
        print('Bad parenthesed')
    else:
        print('Well parenthesed')







if __name__=='__main__':
    parentheses_checker()




