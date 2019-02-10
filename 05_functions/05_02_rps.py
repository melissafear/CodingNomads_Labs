'''
Code a game of rock paper scissors.

'''

# function to get hand based on number
# the function should take in a number and return the string representation of the hand

def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    if hand == 0:
        hand = "scissor"
    elif hand == 1:
        hand = "rock"
    elif hand == 2:
        hand = "paper"

    return hand

# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(computer, player):
    if player == "scissor" and computer == "paper" \
            or player == "rock" and computer == "scissor" \
            or player == "paper" and computer == "rock":
        winner = "you"

    elif user_hand == "scissor" and computer == "rock" \
        or player == "rock" and computer == "paper" \
        or player == "paper" and computer == "scissor":
        winner = "the computer"

    elif player == "scissor" and computer == "scissor" \
        or player == "rock" and computer == "rock" \
        or player == "paper" and computer == "paper":
        winner = "no-one"

    return winner


# '''
# Start here
# '''


# take in a number 0-2 from the user that represents their hand
# generate a random number 0-2 to use for the computer's hand

user_number = int(input("Please enter a number: 0 = scissor, 1 = rock, 2 = paper "))

import random
computer_number = random.randint(0,2)


# call the function get_hand to get the string representation of the user's hand
# call the function get_hand to get the string representation of the computer's hand

user_hand = get_hand(user_number)
computer_hand = get_hand(computer_number)


# call the function determine_winner to figure out the winner
the_winner = determine_winner(computer_hand, user_hand)

# print out the player hand and computer hand
print (f"You played {user_hand} and the computer played {computer_hand}")
# print out the winner
print(f"The winner is {the_winner}!")