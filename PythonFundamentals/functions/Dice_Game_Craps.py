""" Simulating the dice game craps """

import random


def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple


def display_dice(dice):
    """ Display one roll of the two dice."""
    die1, die2 = dice  # unpack the tuple into variables die1 and die2
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')


die_values = roll_dice()  # first roll
display_dice(die_values)

# determine game status and poing, based on first roll

sum_of_dice = sum(die_values)

if sum_of_dice in (7, 11):  # win
    game_status = 'WON'
elif sum_of_dice in (2, 3, 12):  # lose
    game_status = 'LOST'
else:  # remember count
    game_status = 'CONTINUE'
    my_point = sum_of_dice
    print('Point is', my_point)

# Continue rolling until player wins or loses
while game_status == 'CONTINUE':
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)

    if sum_of_dice == my_point:  # win by making point
        game_status == 'WON'
    elif sum_of_dice == 7:
        game_status = 'LOST'

# Display "wins" or "loses" message

if game_status == 'WON':
    print('Pleyer wins')
else:
    print('Player loses')
