#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`parentheses_checker2` module

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
    if true nothing happens otherwise print the line number and caracter that causes
    the problem

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

    line_number = 1

    res = ''

    while(line_read != '' and not bad_parentheses):
        i = 0
        while(i <len(line_read) and not bad_parentheses):
            if line_read[i] in {'(',')','[',']','{','}'}:
                if line_read[i] in PARENTHESES.keys():
                    #Pushing a list of the caracter at index 0,
                    #his place in the line at the index 1
                    #and the line number at index 2
                    line_stack.push([line_read[i],i,line_number])
                elif not line_stack.is_empty() and PARENTHESES[line_stack.top()[0]] == line_read[i]:
                    line_stack.pop()
                elif not line_stack.is_empty():
                    bad_parentheses = True
                    res = ("Closed parenthese {} at line {} char {}"
                            " don't match the open parenthese {} at line {}"
                            " char {}").format(line_read[i], line_number, i, line_stack.top()[0],line_stack.top()[2],
                                    line_stack.top()[1])
                else:
                    bad_parentheses = True
                    res = ("No open parenthese matching parenthese {} at line {} char {}"
                            "").format(line_read[i], line_number, i)
            i+=1
        line_read = open_file.readline()
        line_number += 1

    open_file.close()
    if bad_parentheses:
        print(res)
    elif not line_stack.is_empty():
        print(("Parenthese {} at line {} char {}"
                " has no matching closed parenthese").format(line_stack.top()[0], line_stack.top()[2], line_stack.top()[1]))







if __name__=='__main__':
    parentheses_checker()




