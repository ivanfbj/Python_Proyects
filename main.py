"""
source:
https://youtu.be/8ext9G7xspg?t=1274
https://youtu.be/8ext9G7xspg?t=1274
The objective of this project is to develop a software for play Rock Paper and scissors, user versus computer.
"""
import random


def is_win(player, opponent):
    # Return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    else:
        return 'You lost!'


if __name__ == "__main__":
    print(play())
