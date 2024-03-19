"""
Angry Bird Dice Roller
3/19/2024
by stereoscoped
"""

import random
import time

while True:

    roll = input("Enter anything to roll! ")

    roll = random.randint(0,5)
    if roll == 0:
        print("Red")
    elif roll == 1:
        print("Blues")
    elif roll == 2:
        print("Bomb")
    elif roll == 3:
        print("Chuck")
    elif roll == 4:
        print("Matilda")
    elif roll == 5:
        print("Terence")
    
    time.sleep(1)
