import argparse

from collections import Counter

def read_file(file):
    for line in open(file):
        yield line

def do_things(file):
    left_column = []
    right_column = []

    for line in read_file(file):
        out = line.split()
        if len(out) == 2:
            left_column.append(out[0])
            right_column.append(out[1])
    
    left_column = [int(x) for x in left_column]
    right_column = [int(x) for x in right_column]
    left_column.sort()
    right_column.sort()

    distance = 0
    for l, r, in zip(left_column, right_column):
        distance = distance + abs(l-r)

    print(f'Distance is {distance}')

    rc = Counter(right_column)
    lc = Counter(left_column)

    similarity = 0
    for key, val in lc.items():
        similarity = similarity + (rc[key] * key)

    print(f'Similarity is {similarity}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='2024 Day 1')
    parser.add_argument('-f', '--filename', type=str)
    args = parser.parse_args()
    do_things(args.filename)


