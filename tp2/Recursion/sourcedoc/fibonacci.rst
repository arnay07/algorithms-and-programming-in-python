=================
Fibonacci numbers
=================

:doc:`back <index>`
      
.. automodule:: fibonacci

What are Fibonacci numbers?
===========================

Fibonacci numbers are a sequence of numbers defined by the two first terms :

.. math::

   f_0 &= 0\\
   f_1 &= 1\\

and for all :math:`n\geq 0` by the following recursion relation :

.. math::

   f_{n+2} &= f_{n+1} + f_{n}.

Here are the Fibonacci numbers for :math:`0\leq n \leq 10` :

.. table:: Table of the first Fibonacci numbers
 

   ===========  ============
   :math:`n`     :math:`f_n`  
   ===========  ============
   0            0
   1            1
   2            1
   3            2
   4            3
   5            5
   6            8
   7            13
   8            21
   9            34
   10           55
   ===========  ============


A recursive function
====================

.. autofunction:: fibo

		  
fibo(40) prend beaucoup de temps à s'exécuter si on ne fait pas appel
à la mémoïsation, mais une fois qu'on utilise la mémoïsation il s'exécute
assez rapidement

.. code-block:: python

	>>> fibo.counter = 0
	>>> fibo(40)
	>>> fibo.counter
	79
