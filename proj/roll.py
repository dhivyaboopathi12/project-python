roll = input("Need to play !! Press Enter..")
import random

#range of the values of a dice
min_val = 1
max_val = 6

#to loop the rolling through user input
roll_again = "yes"

while roll_again == "yes" or roll_again == "y" or roll_again == "s": 
    print("Rolling The Dices...")
    print("The Values are :")
    
    #generating first value
    print(random.randint(min_val, max_val))
    
    #generating second value
    print(random.randint(min_val, max_val))
    
    #asking user to roll the dice again
    roll_again = input("Roll the Dices Again?") 