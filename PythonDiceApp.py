import random


def dice_sides():
    sides = int(input('How many sides would you like on your dice: '))
    return sides


def dice_number():
    num_dice = int(input('How many dice would you like to roll: '))
    return num_dice


def roll_dice(sides, num_dice):  # Simulate rolling of dice
    dice = []
    print(f'You rolled {num_dice} nos., {sides} sided dice.\n*********Results are as '
          f'follows ******')
    for i in range(num_dice):
        value = random.randint(1, sides)
        print(f'\t{value}')
        dice.append(value)
    return dice


def sum_dice(dice):  # Add all values of dice
    print(f'The total value of the roll is {sum(dice)}.')


''' total = 0
 for die in dice:
     total += die
 print(f'The total value of the roll is {total}.')'''


def roll_again():  # Ask user to roll again
    choice = input('Would you like to roll again?(Yes/No): ').lower().strip()
    if choice.startswith('n'):
        repeat = False
        print('Thank you for playing with us..Good bye..!')
    else:
        repeat = True
    return repeat


print('Welcome to Python Dice App')
repeat = True
while repeat:
    d_sides = dice_sides()
    d_number = dice_number()
    my_dice = roll_dice(d_sides, d_number)
    sum_dice(my_dice)
    repeat = roll_again()
