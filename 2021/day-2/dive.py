#!/usr/bin/env python3

import argparse

def dive(file):

    x = 0
    part_one_depth = 0

    aim = 0
    part_two_depth = 0

    start = dt.datetime.now()

    for line in open(file):
        arg, val = line.split(' ')

        val = int(val)

        if arg == 'forward':
            x += val
            part_two_depth += (aim * val)
        elif arg == 'up':
            part_one_depth -= val
            aim = max(0, aim-val)
        elif arg == 'down':
            part_one_depth += val
            aim += val

    print(f'{part_one_depth*x=}, {part_two_depth*x=}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str, required=True)
    args = parser.parse_args()

    dive(args.filename)
