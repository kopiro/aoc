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
    return (word[(int)(idxa)-1] == char) ^ (word[(int)(idxb)-1] == char)


def puzzle_1(lines):
    return sum(1 if process_line_puzzle_1(line) else 0 for line in lines)


def puzzle_2(lines):
    return sum(1 if process_line_puzzle_2(line) else 0 for line in lines)


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print(puzzle_1(lines))
    print(puzzle_2(lines))
