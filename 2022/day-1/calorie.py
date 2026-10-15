#!/usr/bin/env python3

import argparse

def read_file(file):
    for line in open(file):
        yield line.strip()

def largest_elf(elves):
    return max(elves, key=elves.get)

def count_calories(file):
    counter = 0
    current_calories = 0
    
    elves = {}

    for calorie in read_file(file):
    
        if not calorie:
            counter += 1
            elves[counter] = current_calories
            current_calories = 0
        else:
            current_calories += int(calorie)
            

    biggest = largest_elf(elves)
    print(f"Part one: {biggest}: {elves[biggest]}")

    current_calories = 0
    
    for i in range(0, 3):
        target = largest_elf(elves)
        current_calories += elves[target]
        elves.pop(target)

    print(f"Part two: Combined: {current_calories}")




if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Day 1')
    parser.add_argument('--filename', type=str, required=True)
    args =  parser.parse_args()

    count_calories(args.filename)


