#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'YOUR NAME HERE'
__date_creation__ = 'DATE HERE'
__doc__ = """
:mod:`recursive_sorts_analysis` module
:author: {:s} 
:creation date: {:s}
:last revision:


""".format(__author__, __date_creation__)

import sys
import timeit
from matplotlib import pyplot as plt
import random

from ap2_decorators import count
from recursive_sorts import compare, quicksort, mergesort

SORTS = {'quicksort': quicksort,
         'mergesort': mergesort
}

def random_list(size):
    '''
    :param size: (int)
    :return: (list) list of size size containing all natural numbers from 0 to n-1 in random order
    :CU: n >= 0
   
    >>> l1 = random_list(10)
    >>> l1.sort()
    >>> l1 == list(range(10))
    True
    '''

def myplot(listX, listY, title='', xlabel='', ylabel=''):
    '''
    :param listX: (list) list of x-values
    :param listY: (list) list of y-values
    :param title: (str) [optional] title of the plot
    :param xlabel: (str) [optional] x-axe's label
    :param ylabel: (str) [optional] y-axe's label
    :return: (NoneType)
    :side effect: plot the data in listX and listY
    '''

def build_times_list(sort, max_size, sample_size):
    '''
    :param sort: (str) name of sorting method
    :param max_size: (int) max size of the lists to sort
    :param sample_size: (int) 
    :return: (list) list of average time for sorting lists of size up to max_size
    '''


def build_comp_number_list(sort, max_size, sample_size):
    '''
    :param sort: (str) name of sorting method
    :param max_size: (int) max size of the lists to sort
    :param sample_size: (int) 
    :return: (list) list of average number of comparisons for sorting lists of size up to max_size
    '''


    
def quicksort_best_case(n):
    """
    :param n: (int)
    :return: (int) number of comparisons in quicksort for sorting a list of length n
             in the best case
    
    >>> [quicksort_best_case(k) for k in range(10)]
    [0, 0, 1, 2, 4, 6, 8, 10, 13, 16]
    """

def quicksort_worst_case(n):
    """
    :param n: (int)
    :return: (int) number of comparisons in quicksort for sorting a list of length n
             in the worst case

    >>> [quicksort_worst_case(k) for k in range(10)]
    [0, 0, 1, 3, 6, 10, 15, 21, 28, 36]
    """


def mergesort_best_case(n):
    """
    :param n: (int) 
    :return: (int)number of comparisons in mergesort for sorting a list of length n
             in the best case

    >>> [mergesort_best_case(k) for k in range(10)]
    [0, 0, 1, 2, 4, 5, 7, 9, 12, 13]
    """


def mergesort_worst_case(n):
    """
    :param n: (int)
    :return: (int) number of comparisons in mergesort for sorting a list of length n
             in the worst case

    >>> [mergesort_worst_case(k) for k in range(10)]
    [0, 0, 1, 3, 5, 8, 11, 14, 17, 21]
    """


COUNTERS = {('quicksort', 'best'): quicksort_best_case,
            ('quicksort', 'worst'): quicksort_worst_case,
            ('mergesort', 'best'): mergesort_best_case,
            ('mergesort', 'worst'): mergesort_worst_case
}


def usage():
    print('Usage: {:s} <option> <sort> <max size> <sample size | case>'.format(sys.argv[0]),
          file=sys.stderr)
    print('avec\n\t<option> = -time | -comp | -theory', file=sys.stderr)
    print('\t<sort> = {:s}'.format(' | '.join(SORTS.keys())), file=sys.stderr)
    print('\t<max size> = max size of lists to sort', file=sys.stderr)
    print('\t<sample size> = size of samples. Avalaible only for -time or -comp options',
          file=sys.stderr)
    print('\t<case> = best | worst. Avalaible only for -theory option', file=sys.stderr)
    exit(1)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)

    # Arguments verification
    if len(sys.argv) != 5:
        print('Bad number of arguments!', file=sys.stderr)
        usage()

    OPTIONS = ('-time', '-comp', '-theory')
    OPTION = sys.argv[1]
    if OPTION not in OPTIONS:
        print('Bad option!', file=sys.stderr)
        usage()

    SORT = sys.argv[2]
    if SORT not in ('mergesort', 'quicksort'):
        print('Unknown sorting method!', file=sys.stderr)
        usage()

    try:
        MAX_SIZE = int(sys.argv[3])
    except ValueError:
        print('Max size must be an integer!', file=sys.stderr)
        usage()

    SIZES = list(range(MAX_SIZE))
    
    if OPTION != '-theory':
        try:
            SAMPLE_SIZE = int(sys.argv[4])
        except ValueError:
            print('Sample size must be an integer!', file=sys.stderr)
            usage()
    else:
        CASE = sys.argv[4]
        if CASE not in ('worst', 'best'):
            print('Case must be worst or best!', file=sys.stderr)
            usage()

    # all is OK
    if OPTION == '-time':
        '''
        HERE'S THE CODE FOR TIME EXPERIMENT AND PLOT
        '''
    
    elif OPTION == '-comp':
        '''
        HERE'S THE CODE FOR COMPARISON EXPERIMENT AND PLOT
        '''
    else:
        '''
        HERE'S THE CODE FOR THEORETIC COMPARISON'S NUMBER AND PLOT 
        '''
