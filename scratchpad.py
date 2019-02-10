
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
        winner = "You won! Winner winner chicken dinner"

    elif user_number == "scissor" and computer == "rock" \
        or player == "rock" and computer == "paper" \
        or player == "paper" and computer == "scissor":
        winner = "Computer won, better luck next time :("

    elif player == "scissor" and computer == "scissor" \
        or player == "rock" and computer == "rock" \
        or player == "paper" and computer == "paper":
        winner = "No-one won, it's a tie!"

    return winner


import random

# get user number
user_number = int(input("Please enter a number from 0-2 - 0 = scissor, 1 = rock, 2 = paper "))


# get computer number
computer_number = random.randint(0, 2)


# translate numbers to strings

user_hand = get_hand(user_number)
computer_hand = get_hand(computer_number)


# compute winner

winner_is = determine_winner(computer_hand, user_hand)

# print winner and hands played
print(f"You played {user_hand}")
print(f"Computer played {computer_hand}")
print(winner_is)