import random

def play():
    user = input("WHAT İS YOUR CHOICE?  'r' for rock, 'p' for paper, 's' for scissors : ")
    computer = random.choice(['r', 'p', 's']) 

    if user == computer:
        print(f"The computer choice is {computer}")
        return 'Its a tie'

    if is_win(user,computer):
        print(f"The computer choice is {computer}")
        return 'You won!!'

    return 'You lost'

def is_win(player, opponent):
    # return True if player wins
    # r > s, p > r, s > p

    if (player == 'r' and opponent == 's') or (player == 's' and opponent =='p') or\
        (player == 'p' and opponent == 'r'):

        return True

print(play())

