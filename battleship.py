#import random number generator function
from random import randint

#Initialize an empty list
board = []

#create a 5x5 grid of "O"s to form the game board
for x in range(5):
    board.append(["O"] * 5)

#function to print the game board
def print_board(board):
    for row in board:
        #Remove the list formatting and just show the "O"s
        #.join(list) will merge the list values with what's between the quotation marks
        print " ".join(row)

#print welcome statement and print the game board
print "Let's play Battleship!"
print_board(board)

#functions to generate random integers between 0 and the game board size
def random_row(board):
    #generate random int between 0 and board length, inclusive
    return randint(0, len(board) - 1)
def random_col(board):
    #generate random int between 0 and board length, inclusive
    return randint(0, len(board) - 1)

#generate a random x,y coordinate for the battleship location
ship_row = random_row(board)
ship_col = random_col(board)

#uncomment the 2 print... lines below to show the answer for debugging or filthy cheaters
#the "+ 1" is to convert 0-4 nomenclature to a more user friendly 1-5
#print ship_row + 1
#print ship_col + 1

#below is everything used for game play
#used a for loop to give the player 4 guesses
for turn in range(4):
    #Indicate which turn the player is on and increment the count
    print "Turn", turn + 1
    
    #prompt the user for a row and column guess.
    #the "- 1" is to convert user friendly 1-5 numbers to standard python 0-4 nomenclature
    guess_row = int(raw_input("Guess Row:")) - 1
    guess_col = int(raw_input("Guess Col:")) - 1
    
    #if the user guesses the correct battleship coordinates
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    #if the user guesses incorrectly
    else:
        #if the guess is off the grid
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        #if the user guesses a coordinate they've already guessed this round
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        #a valid, but incorrect guess
        else:
            print "You missed my battleship!"
            #change the guess location from "O" to "X"
            board[guess_row][guess_col] = "X"
        #after 4 wrong guesses
        if turn == 3:
            print "Game Over"
            #reveal location of the battleship
            #convert all non guessed coordinates to "_" for viewing ease
            for row in board:
                for i in range(len(row)):
                    if row[i] == "O":
                        row[i] = "_"
            #show the battleship location as a "$"
            board[ship_row][ship_col] = "$"
        #reprint the game board
        print_board(board)