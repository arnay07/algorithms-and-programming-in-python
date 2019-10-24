#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`recursive sorts`
:author: `FIL - FST - Univ. Lille.fr <http://portail.fil.univ-lille1.fr>`_
:date: 2016, september. Last revised: 2018, september

Some recursive sorting algorithms:

- quicksort
- mergesort

"""

import random

def compare(a, b):
    """
    :param a: 
    :type a: any type 
    :param b:
    :type b: same as a
    :return:
       - -1 if a < b
       -  1 if a > b
       -  0 if a = b
    :UC: a and b must be comparable with <
    :Examples:

    >>> compare(0, 1)
    -1
    >>> compare('a', 'a')
    0
    >>> compare((2, 1), (1, 2))
    1
    """
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0
    
def is_sorted(l, comp=compare):
    """
    return True if list l is sorted by ascending order
    and False otherwise.

    :param l: list to test
    :param comp: (optional) comparison function (default value is compare)
    :type l: list
    :return: True if l is sorted, False otherwise
    :rtype: bool
    :UC: elements of l must be comparable
    :Examples:

    >>> is_sorted([1, 2, 3, 4])
    True
    >>> is_sorted([1, 2, 4, 3])
    False
    """
    n = len(l)
    if n <= 1:
        return True
    else:
        cmp = comp(l[0], l[1])
        return cmp <= 0 and is_sorted(l[1:], comp=comp)


######################################################
#                 QUICKSORT
######################################################

def partition(x, l, comp=compare):
    """
    return a couple (l1,l2) of lists with elements of l1 <= x
    and elements of l2 > x.

    :param x: a pivot
    :param l:
    :type l: list
    :param comp: (optional) comparison function (default value is compare)
    :return: a couple of two lists with elements of l1 <= x
             and elements of l2 > x
    :rtype: tuple
    :UC: x must be comparable with elements of l

    :Examples:

    >>> partition(3, [1, 4, 1, 5, 9, 2])
    ([1, 1, 2], [4, 5, 9])
    >>> partition(10, [1, 4, 1, 5, 9, 2])
    ([1, 4, 1, 5, 9, 2], [])
    >>> partition(3, [])
    ([], [])
    """
    if l == []:
        return ([], [])
    else:
        l1, l2 = partition(x, l[1:], comp=comp)
        cmp = comp(l[0], x)
        if cmp < 1:
            return ([l[0]] + l1, l2)
        else:
            return (l1, [l[0]] + l2)

def quicksort(l, comp=compare):
    """
    return a new list containing elements of l sorted by ascending order.

    :param l: a list to sort
    :type l: list
    :param comp: [optional] comparison function (default value is compare)
    :type: function
    :param index_pivot: [optional]  index of the pivot : 0 -> first element of list,
                        other -> random
    :type: int
    :return: a new list containing elements of l in ascending order
    :rtype: list
    :UC: elements of l are comparable
    :Examples:

    >>> quicksort([3, 1, 4, 1, 5, 9, 2])
    [1, 1, 2, 3, 4, 5, 9]
    >>> import random
    >>> n = random.randrange(20)
    >>> l = [random.randrange(20) for k in range(n)]
    >>> l1 = quicksort(l)
    >>> len(l1) == len(l)
    True
    >>> is_sorted(l1)
    True
    >>> all(k in l for k in l1)
    True
    """
    n = len(l)
    if n <= 1:
        return l.copy()
    else:
        index_pivot = random.randrange(n)
        lprime = l[:index_pivot] + l[index_pivot+1:]
        l1, l2 = partition(l[index_pivot], lprime, comp = comp)
        l1s = quicksort(l1, comp=comp)
        l2s = quicksort(l2, comp=comp)
        return l1s + [l[index_pivot]] + l2s


######################################################
#                 MERGESORT
######################################################

def split(l):
    """
    return a couple (l1,l2) of lists

    :param l:
    :type l: list
    :return: a couple of two lists of equal length
    :rtype: tuple
    :UC: none
    :Examples:

    >>> l = [3, 1, 4, 1, 5, 9, 2]
    >>> l1, l2 = split(l)
    >>> l3 = l1 + l2
    >>> len(l3) == len(l)
    True
    >>> all(k in l for k in l3)
    True
    """
    n = len(l)
    # first possibility
    # return (l[0:n//2], l[n//2:])
    if n == 0:
        return ([], [])
    elif n == 1:
        return ([l[0]], [])
    else:
        l1, l2 = split(l[2:])
        return ([l[0]] + l1, [l[1]] + l2)

def merge(l1, l2, comp=compare):
    """
    return a list containing all elements de l1 and l2.
    If l1 and l2 are sorted, so is the returned list.

    :param l1:
    :type l1: list
    :param l2:
    :type l2: list
    :param comp: (optional) comparison function (default value is compare)
    :return: a merged list from l1 and l2
    :rtype: list
    :UC: elements of l1 and l2 are comparable
    :Examples:

    >>> merge([1, 3, 4, 9], [1, 2, 5])
    [1, 1, 2, 3, 4, 5, 9]
    """
    if l1 == []:
        return l2.copy()
    elif l2 == []:
        return l1.copy()
    else:
        cmp = comp(l1[0], l2[0])
        if cmp <= 0:
            return [l1[0]] + merge(l1[1:], l2, comp=comp)
        else:
            return [l2[0]] + merge(l1, l2[1:], comp=comp)

def mergesort(l, comp=compare):
    """
    return a new list containing elements of l sorted by ascending order.

    :param l: a list to sort
    :type l: list
    :param comp: (optional) comparison function (default value is compare)
    :return: a new list containing elements of l in ascending order
    :rtype: list
    :UC: elements of l are comparable
    :Examples:

    >>> mergesort([3, 1, 4, 1, 5, 9, 2])
    [1, 1, 2, 3, 4, 5, 9]
    >>> import random
    >>> n = random.randrange(20)
    >>> l = [random.randrange(20) for k in range(n)]
    >>> l1 = mergesort(l)
    >>> len(l1) == len(l)
    True
    >>> is_sorted(l1)
    True
    >>> all(k in l for k in l1)
    True
    """
    n = len(l)
    if n <= 1:
        return l.copy()
    else:
        l1, l2 = split(l)
        l1s = mergesort(l1, comp=comp)
        l2s = mergesort(l2, comp=comp)
        return merge(l1s, l2s, comp=comp)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)


