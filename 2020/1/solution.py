import os
from functools import reduce
from itertools import combinations

dir_path = os.path.dirname(os.path.realpath(__file__))


def puzzle(lines, count):
    for c in combinations(lines, count):
        if sum(c) == 2020:
            return reduce((lambda x, y: x * y), c)


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [int(line.strip()) for line in f.readlines()]
    print(puzzle(lines, 2))
    print(puzzle(lines, 3))
