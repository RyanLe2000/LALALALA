"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
    
    We are going to convert the coin class to a dice class
    The following code is based on the coin class from your book
"""

import random
# TODO change class name to Dice


class Dice:  # note class names are capitalized
    def __init__(self):
        # TODO change side_up to '1'
        self.side_up = '1'

        # TODO change name to roll
    def roll(self):
dice_roll = random.randint(0, 6)
    if dice_roll = 1:
            self.side_up = '1'
    elif dice_roll = 2:
            self.side_up = '2'
    elif dice_roll = 3:
            self.side_up = '3'
    elif dice_roll = 4:
            self.side_up = '4'
    elif dice_roll = 5:
            self.side_up = '5'
    elif dice_roll = 6:
            self.side_up = '6'


    def get_num_up(self):
        return self.side_up
    

def main():
    # TODO change my_coin to my_dice, my_dice_two and the appropriate class name throughout main
    my_dice = Dice()
    my_dice_two = Dice()
    print('This side is up, ', my_dice.get_num_up())
    print('This side is up, ', my_dice_two.get_num_up())
    
    print('I am tossing the coins...')
    my_dice.roll()
    my_dice_two.roll()
    print('This side is up, ', my_dice.get_num_up())
    print('This side is up, ', my_dice_two.get_num_up())


main()
