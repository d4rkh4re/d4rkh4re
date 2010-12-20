"""
a1.py
William C. Morris
<d4rkh4re@gmail.com>
"""
import math
import random

""" FUNC: double_exps(n) """
def double_exps(n):
    justification = len(str(2**(2**n)))
    for i in range(1, n+1):
        math_result = str(2**(2**i))
        print(i, math_result.rjust(justification))

""" FUNC: guess_number(level) """
def guess_number(level):
    player_guesses = 0
    upper_bound = math.pow(level, 2)
    r = random.randint(level, upper_bound)

    player_input = input(str("I'm thinking of a number between " + str(level) \
                             + " and " + str(upper_bound) + "\n"))

    while True:
        if (int(player_input) > r):
            player_input = input("Your guess: " + str(player_input) + \
                                 "\nThat's too high.\n")
            player_guesses += 1
        elif (int(player_input) < r):
            player_input = input("Your guess: " + str(player_input) + \
                                 "\nThat's too low.\n")
            player_guesses += 1
        else:
            player_guesses += 1
            print("That's it!\nIt took you", player_guesses, \
                  "tries to find my number.\nYou where lucky!")
            break

""" FUNC: right_justify(s, n) """
def right_justify(s, n):
    s_length = len(s)
    if (len(s) >= n):
        return s
    else:
        return s.rjust(n)

# Never use anything bigger than 16.
double_exps(5)
guess_number(4)
print( right_justify('12', 4) )
