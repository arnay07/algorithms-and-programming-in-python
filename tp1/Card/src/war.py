#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`war` module 

:author: ` Arnaud Kaderi, BAH Elhadj ibrahima
         Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2019, September. Last revision: 2019, september


"""

import card




def create_hands(number_of_cards):
    """
    Create the two hands for players
    
    :param numbers_of_cards: number of cards by player
    :type numbers: int
    :CU: None
    :return: a list of the two hands
    
    """
    
   
    hand_player1 , hand_player2 = [], []
    

    for i in range(number_of_cards):
        hand_player1.append(card.Card.random())
        hand_player2.append(card.Card.random())
        
    return (hand_player1, hand_player2)
    
    
    





def game(number_of_cards):
    """
    """


    hand_player1, hand_player2 = create_hands(number_of_cards)[0], create_hands(number_of_cards)[1]
    
    table = []

    while (len(hand_player1)>0 and len(hand_player2)>0):

        print(20*'-')
        print("First plays")
        print(hand_player1[0])

        table.append(hand_player1[0])
        hand_player1.remove(hand_player1[0])

        print("Second plays")
        print(hand_player2[0])
        table.append(hand_player2[0])
        hand_player2.remove(hand_player2[0])


        table_length = len(table)

        if (table[table_length-1] == table[table_length-2]):
            print("*******War********")
            continue
        else:
            if (table[table_length-1] > table[table_length-2]):
                print("Second player wins")
                hand_player2.extend(table)
            else:
                print("First player wins")
                hand_player1.extend(table)

    


    if (len(hand_player1) == 0 and len(hand_player2) > 0 ):
        print ("\n******Player 2 wins********")

    elif (len(hand_player2) == 0 and len(hand_player1) > 0):
        print("\n*******Player 1 wins********")
        
    else:
        print("*****No one wins******")
        
        
        
        

        
        
        
    
   

        
    

def usage():

    print("usage:  python3 war.py") 
    print("or python3 war.py  [number of cards]")


    

if __name__ == '__main__':

    import sys
    if len(sys.argv) == 2:
        number_of_cards = int(sys.argv[1])
        assert number_of_cards <= 16, "the number of cards must be inferior or equal to 16"

        game(number_of_cards)
        
    elif len(sys.argv) == 1:
        game(16)

    else:
        usage()
    
    
#def usage():
#    print('number: "{:s}"'.format(sys.argv[1]))
#if __name__ == '__main__':
#    import sys
#    if len(sys.argv[1])>2:
#        usage()
#    else:
#        try:
#            num = int(sys.argv[1])
#        except valueError:
#            print("c'est pas un nombre")
#            usage()
#            exit(1)
#        game(num)    
                                 
    


