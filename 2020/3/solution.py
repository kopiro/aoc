import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def puzzle_2(lines):
    dirs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    x_max = len(lines[0])
    y_max = len(lines)
    count_mul = 1
    for dir in dirs:
        x = 0
        y = 0
        count = 0
        while y < y_max:
            if lines[y][x % x_max] == "#":
                count += 1
            x += dir[0]
            y += dir[1]
        count_mul *= count
    return count_mul


def puzzle_1(lines):
    x = 0
    y = 0
    count = 0
    x_max = len(lines[0])
    while y < len(lines):
        if lines[y][x % x_max] == "#":
            count += 1
        x += 3
        y += 1
    return count


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print(puzzle_1(lines))
    print(puzzle_2(lines))
