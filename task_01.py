#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Optional and required things."""


def get_matches(players):
    """Matches players together

    Args:
        players (list): List of player names

    Returns:
        List of tuples which contain player pairs

    Examples"

        >>> get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
    """

    player_index = 0 #
    names = []
    while player_index < (len(players)-1): #all the way through
        player = players[player_index]
        player_index2 = player_index + 1 #wrong variable before [player_index]
        player_index = player_index + 1
        while player_index2 < len(players): #2nd one forward
            player2 = players[player_index2]
            player_index2 = player_index2 + 1
            somenames = (player, player2)
            names.append(somenames)
    return names


#def get_matches(players):
#    names = []
#    for myindex, myplayers in enumerate(players):
#        players[myindex] = players[myindex] + 1

#    print 'after loop'
#    print players
