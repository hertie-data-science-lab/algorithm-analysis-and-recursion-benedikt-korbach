# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:24:20 2023

@author: Benedikt Korbach
"""
# Iniate total_moves counter
total_moves = 0

# Define moving method
def move(n, from_rod, to_rod):
    print("Move plate", n, "from rod", from_rod, "to", to_rod)
    global total_moves
    total_moves += 1

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):

    # Base case
    if n == 0:
        return

    # Move all plates except for the biggest one to the auxilliary rod
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)

    # Move the biggest plate to the to-rod
    move(n, from_rod, to_rod)

    # Move all the remaining plates from the auxilliary rod to the to-rod
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

# Select the number of plates by changing the first variable
TowerOfHanoi(3, 'A', 'C', 'B')

# Print total moves needed to solve Tower of Hanoi puzzle
print("Total moves needed to solve: ", total_moves)