
# In this homework, we're going to build a simple simulator to play a
# 2-person game of Dreidel.  https://en.wikipedia.org/wiki/Dreidel

# In dreidel, each player starts with a set of pieces.
# At the beginning of each round of play, all players add one piece to the
# center 'pot.'
# Players take turns spinning a 4-sided top.
# On a player's turn, she/he wins or loses pieces to the pot.
# of pieces according to the rules here:
# https://en.wikipedia.org/wiki/Dreidel#Rules_of_the_game
#  Nun:  nothing happens
#  Gimel: the player gets all the pieces in the pot
#  He:  the player gets half the pieces in the pot (rounded up if odd)
#  Shin:  the player puts one piece in the pot
# The game ends when one player has all the pieces.

# Dreidel is a game of chance, but we've included a example output
# file so that you can check your work.  You can eliminate randomness
# in this simulator by fixing the seed that the random number generator is
# using.

# PUT ANY IMPORT STATEMENTS YOU NEED HERE

from sys import argv
import random
import itertools


#  PUT ANY FUNCTION DEFINITIONS IN THIS SECTION

# This returns one of the four dreidel values as a string
def spin_dreidel():
    return random.choice(['nun', 'shin', 'he', 'gimel'])

def move_pieces(dreidel_val, pot, spinners_stack):
    #  4.  Now fill in the logic in this function
    if dreidel_val == 'shin':

        #player adds piece to the pot
        spinners_stack = spinners_stack -1
        pot = pot+1
        # print "fSpinner: %d " % spinners_stack
        # print "fPot: %d" % pot

        return pot, spinners_stack


    elif dreidel_val == 'he':
        #spinner gets half the pot
        if int(pot/2.0)!= (pot/2.0):
            spinners_stack = spinners_stack + (pot/2)+1
            pot = (pot/2)
        else:
            spinners_stack = spinners_stack + (pot/2)
            pot = (pot/2)
        # print "fSpinner: %d " % spinners_stack
        # print "half pot: %d" % (pot/2)
        # print "fPot: %d" % pot

        return pot, spinners_stack

    elif dreidel_val == 'gimel':
        #spinner gets pot
        spinners_stack = spinners_stack + pot
        pot = pot-pot
        # print "fSpinner: %d " % spinners_stack
        # print "fPot: %d" % pot

        return pot, spinners_stack

    elif dreidel_val == 'nun':
        return pot, spinners_stack

    else:
        pass
    return pot, spinners_stack

def ante_up(pot,player_one_pieces,player_two_pieces):
    player_one_pieces = player_one_pieces - 1
    player_two_pieces = player_two_pieces - 1
    pot = pot + 2

    return pot, player_one_pieces, player_two_pieces



# 5.  Inside your while loop and after the player takes a turn, call a function
#     to print out the game state.  Define that function here.
#     Also call this function after the players put pieces into the pot at
#     the start of a round.
#     In order to check your solution, your function should print the number of
#     pieces in the pot, the number of Player 0's pieces and the number of
#     Player 1's pieces, separated by commans with a newline at the end.
#     Exactly like:
#     2,10,8
#     1,10,9
#     etc.

def game_state():
    print "%d,%d,%d" % (pot, player_one_pieces, player_two_pieces)

# EVERYTHING ELSE STARTS HERE

# 0.  Make your program depend on 2 command line arguments:
#     the seed and the number of pieces each player starts with
#     in that order.
#     Then fix the seed.
script_name, seed ,n_start_pieces = argv
# seed = 935
seed= random.seed(seed)
print seed

#  Leave this here.  Note how I made the file name depend on the parameters.
#  Also note that I'm starting off the file with a head row.
out_file = open('dreidel_%s_%s.out' % (seed, n_start_pieces), 'w')
out_file.write("Pot, Player 0, Player 1\n")

#  1.  We need to create a few variables to keep track of the state of the game.
#      Create variables for each player's number of pieces and the number of
#      pieces in the center pot.  Also, create a variable to indicate whose
#      turn it is.  Give these variables the values they should
#      have at the start of the game.

n_start_pieces=n_start_pieces
player_one_pieces = int(n_start_pieces)
player_two_pieces = int(n_start_pieces)
pot = 0
# turn = itertools.cycle(['Player1', 'Player2']).next
turn = itertools.cycle([0, 1]).next
spinner = turn()
game_round = 0

# 2.  The game continues until one player has run out of pieces.
#     Create a while loop with a valid termination criteria.
#     For now, write  a 'dummy' line of code inside the loop to make sure
#     it always ends.

while (player_one_pieces> 0) and (player_two_pieces > 0) :
    game_round = game_round + 1
    # print "Round: %d" % game_round
    pot, player_one_pieces, player_two_pieces = ante_up(pot, player_one_pieces,player_two_pieces)
    game_state()

    if (player_one_pieces > 0) and (player_two_pieces > 0):
#Player 0 spin
        # print spinner
        dreidel_val= spin_dreidel()
        # print dreidel_val
        if spinner == 0:
            spinners_stack = player_one_pieces
            pot, player_one_pieces = move_pieces(dreidel_val, pot, spinners_stack)

        else:
            spinners_stack = player_two_pieces
            pot, player_two_pieces = move_pieces(dreidel_val, pot, spinners_stack)

        game_state()

        spinner=turn()

        # print spinner
        dreidel_val= spin_dreidel()
        # print dreidel_val
        if spinner == 0:
            spinners_stack = player_one_pieces
            pot, player_one_pieces = move_pieces(dreidel_val, pot, spinners_stack)

        else:
            spinners_stack = player_two_pieces
            pot, player_two_pieces = move_pieces(dreidel_val, pot, spinners_stack)

        game_state()

        spinner=turn()
    else:
        # if player_one_pieces == 0:
        #     winner = 1
        # else:
        #     winner = 0
        # print "Game over. Player %d won!" % winner
        pass



# 3.  Inside your while loop, call a function to start a round of play if
#     Player 0's turn is about to start.  Your function should update the
#     number of pieces in the pot and for each player.

# 4.  Inside your while loop, write code to spin the dreidel and update
#     the game state accordingly.  Do this by calling the move_pieces function.
#     The move pieces function doesn't do anything yet, so keep your
#     dummy line in to make sure you exit the while loop.

# 6.  Now add a few lines of code to your while loop to print
#     'Game over.  Player N won!' (where N is 0 or 1) if one of the players
#     has just won.  For full credit here, write nice code
#     and don't repeat yourself.

# 7.  Now add a single line of code to your loop for changing whose turn it is.
#     There are a few cool ways of doing this!

# 8.  Remove any dummy code and check your work.  We've provided a test file
#     for a 2 player, 6 piece (each) game with seed = 939 and a
#     2 player, 10 piece (each) game with seed = 935
#     Remember that you can use cksum to compare files.
