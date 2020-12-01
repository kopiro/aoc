import os
from operator import mul
from functools import reduce
from itertools import combinations

dir_path = os.path.dirname(os.path.realpath(__file__))


def puzzle_optimized_2(lines):
    lines_set = set(lines)
    for c in lines:
        k = 2020 - c
        if k in lines_set:
            return c * k


def puzzle_optimized_3(lines):
    lines_set = set(lines)
    for c in lines:
        for d in lines:
            k = 2020 - c - d
            if k in lines:
                return c * d * k


def puzzle_non_optimized(lines, count):
    for c in combinations(lines, count):
        if sum(c) == 2020:
            return mul(*c)


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [int(line.strip()) for line in f.readlines()]
    print(puzzle_optimized_2(lines))
    print(puzzle_optimized_3(lines))
