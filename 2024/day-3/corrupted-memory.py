import argparse
import re

def read_line(file):
    for line in open(file):
        yield line

def solve_puzzle(file):
    sum = 0
    smarter_sum = 0
    enabled = True

    regex = re.compile(r'mul\(([0-9]+),([0-9]+)\)|(don\'t\(\))|(do\(\))')
    for line in read_line(file):
        matches = regex.findall(line)
        for x, y, dont, do in matches:
            if do or dont:
                enabled = bool(do)
            if x and y:
                val = int(x) * int(y)
                sum += val
                smarter_sum += val * enabled

    print(f'Part one sum is: {sum}')
    print(f'Part two sum is: {smarter_sum}')


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(prog='Day Three AoC')
    parser.add_argument('-f', '--filename', type=str)

    args = parser.parse_args()
    solve_puzzle(args.filename)
