import argparse

def read_line(file):
    for line in open(file):
        yield line

def is_increasing(numbers):
    return all(x < y for x, y in zip(numbers[::], numbers[1::]))

def is_decreasing(numbers):
    return all(x > y for x, y in zip(numbers[::], numbers[1::]))

def is_floor_safe(floor):    

    increasing = is_increasing(floor)
    decreasing = is_decreasing(floor)

    if not increasing and not decreasing:
        return False

    for x,y in zip(floor[::], floor[1::]):
        delta = abs(x-y)
        if delta < 1 or delta > 3:
            return False
    return True

def parse_file(file):
    safe_floors = 0
    extended_safe_floors = 0
    for line in read_line(file):
        out = line.split()
        floor = [int(x) for x in out]

        if is_floor_safe(floor):
            safe_floors += 1
            continue

        # If the floor isn't safe, enumerate through all the values on the floor.
        # We will either return early with a true and continue or the floor isn't safe.
        if any(is_floor_safe([x for j, x in enumerate(floor) if j != i]) for i in
                range(len(floor))):
            extended_safe_floors += 1

    print(f'Safe floors {safe_floors}')
    print(f'Floors safe with dampner {safe_floors + extended_safe_floors}')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='Day Two AoC')
    parser.add_argument('-f', '--filename', type=str)

    args = parser.parse_args()
    parse_file(args.filename)
