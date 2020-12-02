import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def process_line_puzzle_1(line):
    min, max, char, word = re.findall("(\d+)-(\d+) ([a-z])\: (.+)", line)[0]
    count = 0
    for ch in word:
        if ch == char:
            count += 1
            if count > (int)(max):
                return False
    return count >= (int)(min)


def process_line_puzzle_2(line):
    idxa, idxb, char, word = re.findall("(\d+)-(\d+) ([a-z])\: (.+)", line)[0]
    count = 0
    for idx, ch in enumerate(word):
        if ch == char:
            if idx == (int)(idxa)-1:
                count += 1
            if idx == (int)(idxb)-1:
                count += 1
            if count > 1:
                return False
    return count == 1


def puzzle_1(lines):
    count = 0
    for line in lines:
        if process_line_puzzle_1(line):
            count += 1
    return count


def puzzle_2(lines):
    count = 0
    for line in lines:
        if process_line_puzzle_2(line):
            count += 1
    return count


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print(puzzle_1(lines))
    print(puzzle_2(lines))
