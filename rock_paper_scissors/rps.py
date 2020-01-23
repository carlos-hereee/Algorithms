#!/usr/bin/python

import sys


# generate all possible plays per game where n is the number of plays per round

# You'll want to define a list with all of the possible Rock Paper Scissors plays.


def rock_paper_scissors(n):
     # we're building up a list of results
    outcome = []
    choices = ['rock', 'paper', 'scissors']

    def inner_rps(rounds_left, result=[]):
        if rounds_left == 0:
            outcome.append(result)
            return False
        for c in choices:
            # recursion
            inner_rps(rounds_left-1, result+[c])
    inner_rps(n, [])
    return outcome


print('\nnumber of plays:  ', rock_paper_scissors(3))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
