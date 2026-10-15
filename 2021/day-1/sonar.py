#!/usr/bin/env python3

import argparse

def read_file(file):
    for line in open(file):
        yield line.strip()


def sonar(file, window_size):

    previous_depth = -1
    depth_increases = 0

    depths = []

    for depth_str in read_file(file):
        if not depth_str:
            continue

        depth = int(depth_str)

        # Apply the depth to all current depths
        depths = [x + depth for x in depths]
        depths.append(depth)

        if len(depths) == window_size:
            total_depth = depths[0]
            if previous_depth > 0 and total_depth > previous_depth:
                depth_increases += 1

            previous_depth = total_depth
            depths.pop(0)

    print(f'Increases: {depth_increases} with window: {window_size}.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', required=True, type=str)
    parser.add_argument('--size', default=0, type=int)
    args = parser.parse_args()
    # Part One
    sonar(args.filename, 1)
    # Part Two
    sonar(args.filename, 3)

    if args.size > 0:
        sonar(args.filename, args.size)
