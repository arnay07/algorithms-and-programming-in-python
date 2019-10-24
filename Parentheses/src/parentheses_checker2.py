#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`parentheses_checker2` module

:author:Arnaud Kaderi, Elhadj Ibrahima BAH 
         

:date: 2019, october
:last revision: 2019, october

"""


from stack import *
import sys

parentheses_dict = {'(':')','[':']','{':'}'}


def parentheses_checker():
    """
    Checks if the program in the file is well parenthesed
    
    """

    global parentheses_dict
    
    assert len(sys.argv)==2,'the number of files to check must be one'

    file = sys.argv[1]

    line_stack = Stack()
    
    open_file = open(file, 'r')

    line_read = open_file.readline()

    bad_parentheses = False

    line_number = 0

    res = ''
    
    while(line_read != '' and not bad_parentheses):
        i = 0
        j = 0
        while(i <len(line_read) and not bad_parentheses):
            if line_read[i] in {'(',')','[',']','{','}'}:
                if line_read[i] in parentheses_dict.keys():
                    j=i
                    line_stack.push(line_read[i])
                elif not line_stack.is_empty() and parentheses_dict[line_stack.top()] == line_read[i]:
                    line_stack.pop()
                else:
                    bad_parentheses = True
                    res = "Closed parenthese {} at line {} char {} don't match the open parenthese {} at line {} char {}".format(line_read[i], line_number, i, line_stack.top(),line_number, j)
            i+=1
        line_read = open_file.readline()
        line_number += 1

    open_file.close()
    if bad_parentheses or not line_stack.is_empty():
        print(res)
   





    
if __name__=='__main__':
    parentheses_checker()


        

