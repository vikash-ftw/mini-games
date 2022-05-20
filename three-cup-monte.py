from random import shuffle

# cups having ball in mid
cups = ['','O','']

# function to return a shuffled cup list
def shuffle_cups(cups=['','O','']):
    # take list and shuffle it
    shuffle(cups)
    return cups

# function to take input from user
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a cup number: 0, 1, or 2 --> ")
    
    return int(guess)

# function to check player guess via indexing
def check_guess(shuffled_cups, guess):
    if shuffled_cups[guess] == 'O':
        print("CORRECT GUESS!")
    else:
        print('WRONG! BETTER LUCK NEXT TIME')
        print(shuffled_cups)

# check users guess 
check_guess(shuffle_cups(cups),player_guess())


