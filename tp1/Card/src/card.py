#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`card` module 

:author: ` Arnaud Kaderi, BAH Elhadj ibrahima
         Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2019, September. Last revision: 2019, september


"""



import random



class Card(object):
    """
    Cards are defined by a value and a color.
    Possible values and colors are listed in ``Card.VALUES`` and ``Card.COLORS``.

    >>> c1 = Card("Ace", "heart")
    >>> c1.get_color()
    'heart'
    >>> c1.get_value()
    'Ace'
    >>> c1
    Card("Ace", "heart")
    >>> c2 = Card.random()
    >>> c2.get_value() in Card.VALUES
    True
    >>> c2.get_color() in Card.COLORS
    True
    >>> c1 == c1
    True
    >>> c1 != c1
    False
    >>> c1 < c1
    False
    >>> c1 <= c1
    True
    """

    ## tuple of possible values and colors in ascending order
    VALUES = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Knight", "Queen", "King")
    """
    possible values for card's construction
    """
    
    COLORS = ("spade", "heart", "diamond", "club")
    """
    possible colors for card's construction
    """

    
    
    def __init__(self, value, color):
        """
        creates a card with value and color

        :param value: value of the card
        :type value: element of `Card.VALUES`
        :param color: color of the card
        :type color: element of `Card.COLORS`
        """
        assert value in self.VALUES, "value must be one of these (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Knight, Queen, King)"
        assert color in self.COLORS, "color must be one of these (spade, heart, diamond, club)"

        self.__value = value
        self.__color = color

        



    def __repr__(self):
        """
        function to represent the card in a more readable form

        >>> c = Card("Ace", "heart")
        >>> c
        Card("Ace", "heart")
        >>> print(c)
        Card("Ace", "heart")

        """

        return 'Card("{:s}", "{:s}")'.format(self.get_value(), self.get_color())



    

    def __eq__(self, card):
        """
        allow to use the sign "==" on Cards

        >>> c = Card("Ace", "heart")
        >>> c1 = Card("Ace", "heart")
        >>> c2 = Card("2", "heart")
        >>> c == c1
        True
        >>> c == c2
        False
        
        """

        return self.compare(card) == 0


    

    def __neq__(self, card):
        """
        allow to use the sign "!=" on cards

        >>> c = Card("Ace", "heart")
        >>> c1 = Card("King", "diamond")
        >>> c != c1
        True
        
        """

        return self.compare(card) != 0 


    

    def __lt__(self, card):
        """
        allow to use "<" on cards 
        
        >>> c = Card("Ace" , "heart")
        >>> c1 = Card("2", "heart")
        >>> c < c1
        True
        
        """

        return self.compare(card) < 0


    

    def __le__(self, card):
        """
        allow to use "<=" on cards
        
        >>> c = Card("Ace", "heart")
        >>> c11 = Card("2", "diamond")
        >>> c <= c11
        True
        """

        return self.compare(card) <= 0

    

    def __gt__(self, card):
        """
        allow to use ">" on cards

        >>> c = Card("Ace", "heart")
        >>> c11 = Card("2", "diamond")
        >>> c11 > c
        True

        """

        return self.compare(card) > 0

    

    def __ge__(self, card):
        """
        allow to use ">=" on cards

        >>> c = Card("Ace", "heart")
        >>> c11 = Card("2", "diamond")
        >>> c11 >= c
        True
        
        """

        return self.compare(card) >= 0


    
        
        
    
    def random():
        """
        create a card whose value and color are randomly chosen
        
        :returns: *(card)* -- a randomly chosen card
        
        >>> c = Card.random()
        >>> c.get_value() in Card.VALUES
        True
        >>> c.get_color() in Card.COLORS
        True
        """

        random_value = random.choice(Card.VALUES)
        random_color = random.choice(Card.COLORS)

        return Card(random_value, random_color)



        
    
    def get_color(self):
        """
        returns the color of the card

        :return: the color of the card
        :rtype: str
        :UC: none
        :Example:

        >>> c = Card('Ace', 'heart')
        >>> c.get_color()
        'heart'
        """
        return self.__color

    

    def get_value(self):
        """
        returns the value of the card
    
        :param card: the card
        :type card: card
        :returns:  the value of the card
        :rtype: str
        :UC: none
        :Example:
        
        >>> c = Card('Ace', 'heart')
        >>> c.get_value()
        'Ace'
        """
        return self.__value
    




    
    def compare_value(self, card):
         """
         compares cards values

         :param card: the second card
         :type card: card
         :return: (int)

            * a positive number if self's value is greater than card's
            * a negative number if self's value is lower than card's
            * 0 if self's value is the same greater than card's
         :UC: none
         :Example: 

         >>> c1 = Card('Ace', 'heart')
         >>> c2 = Card('King', 'heart')
         >>> c3 = Card('Ace', 'spade')
         >>> c1.compare_value(c2) < 0
         True
         >>> c2.compare_value(c1) > 0
         True
         >>> c3.compare_value(c1) == 0
         True
         """
         return Card.VALUES.index(self.get_value()) - Card.VALUES.index(card.get_value())




     

    def compare_color(self, card):
        """
        compares cars colors, returns : 
        
        :param card: the second card
        :type card: card
        :returns: *(int)* --      
          
           * a positive number if self's color is greater than card's
           * a negative number if self's color is lower than card's
           * 0 if self's color is the same greater than card's
        :UC: none
        :Example: 

        >>> c1 = Card('Ace', 'heart')
        >>> c2 = Card('King', 'heart')
        >>> c3 = Card('Ace', 'spade')
        >>> c1.compare_color(c3) > 0
        True
        >>> c3.compare_color(c1) < 0
        True
        >>> c1.compare_color(c2) == 0
        True
        """

        return Card.COLORS.index(self.get_color()) - Card.COLORS.index(card.get_color())



        

    def compare(self, card):
        """
        compares cards.

        Order on cards is defined  first by order on values, and in case of equal values 
        by order on colors. Order on values is defined by `VALUES` attribute. Same for colors.

        :param card: the second card
        :type card: card

        :return: *(int)* --     
          
           * a positive number if self is greater than card
           * a negative number if self is lower than card
           * 0 if self is the same than card

        :UC: none
        :Example: 

        >>> c1 = Card('Ace', 'heart')
        >>> c2 = Card('King', 'heart')
        >>> c3 = Card('Ace','spade')
        >>> c1bis = Card('Ace','heart')
        >>> c1.compare(c2) < 0
        True
        >>> c2.compare(c1) > 0
        True
        >>> c1.compare(c3) > 0
        True
        >>> c1bis.compare(c1bis) == 0
        True
        """

        if (self.compare_value(card) !=  0):
            return self.compare_value(card)
        else:
            return self.compare_color(card)




        
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
