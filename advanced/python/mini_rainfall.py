#! /usr/bin/env python

import sys

def calculate_mean_until(list_of_numbers, trigger=99):
    '''
    Calculates and returns the mean of all entries in `list_of_numbers` up to
    and including the first entry equal to `trigger`.
    '''
    seen = []
    for num_in in list_of_numbers:
        num_in = int(num_in.strip())
        seen.append(num_in)
        if num_in == trigger:
            mean_seen = sum(seen)/len(seen)
            return mean_seen

if __name__ == '__main__':
    input_numbers = sys.stdin.readlines()
    mean = calculate_mean_until(input_numbers, 99)
    sys.stdout.write(f'mean of numbers seen: {round(mean,2)}\n')
