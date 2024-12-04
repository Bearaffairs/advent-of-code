import argparse

def read_line(file):
    for line in open(file):
        yield line

def is_floor_safe(floor):    

    if all(floor[i] > floor[i+1] for i in range(len(floor) -1)) or \
        all(floor[i] < floor[i+1] for i in range(len(floor) -1)):
        for x,y in zip(floor[::], floor[1::]):
            delta = abs(x-y)
            if delta < 1 or delta > 3:
                return False
    else:
        return False

    return True

def parse_file(file):
    safe_floors = 0

    for line in read_line(file):
        out = line.split()
        floor = [int(x) for x in out]

        if is_floor_safe(floor):
            safe_floors += 1
        
    print(f'Safe floors {safe_floors}')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='Day Two AoC')
    parser.add_argument('-f', '--filename', type=str)

    args = parser.parse_args()
    parse_file(args.filename)
