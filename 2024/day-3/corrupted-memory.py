import argparse
import re

def read_line(file):
    for line in open(file):
        yield line

def part_one(file):
    sum = 0

    regex = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')
    for line in read_line(file):

        matches = regex.findall(line)
        for x, y in matches:
            sum += int(x)*int(y)


    print(f'Part one sum is: {sum}')


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(prog='Day Three AoC')
    parser.add_argument('-f', '--filename', type=str)

    args = parser.parse_args()
    part_one(args.filename)
