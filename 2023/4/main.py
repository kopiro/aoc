import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

'''
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''
def parse_line(line):
    numbers = line.split(":")
    numbers = numbers.split("|")
    numbers = [x.strip() for x in numbers]
    winning_numbers = []
    for number in re.split('\s+', numbers[0]):
        winning_numbers.append(int(number))
    my_numbers = []
    for number in re.split('\s+', numbers[1]):
        my_numbers.append(int(number))
    return winning_numbers, my_numbers

def puzzle_1(lines):
    sum = 0
    for line in lines:
        winning_numbers, my_numbers = parse_line(line)
        s = 0
        for number in my_numbers:
            if number in winning_numbers:
                if s == 0:
                    s += 1
                else:
                    s *= 2
        sum += s
    return sum


def puzzle_2(lines):
    won = {}
    for index, line in enumerate(lines):
        if not index in won:
            won[index] = 0
        winning_numbers, my_numbers = parse_line(line)
        s = 0
        for number in my_numbers:
            if number in winning_numbers:
                s += 1
        for i in range(index+1, index + 1 + s):
            if i in won:
                won[i] += (won[index] + 1) * 1
            else:
                won[i] = (won[index] + 1)
    sum = 0
    for value in won.values():
        sum += (1 + value)
    return sum


if __name__ == "__main__":
    with open(dir_path + "/example.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print("Puzzle 1:", puzzle_1(lines))
    print("Puzzle 2:", puzzle_2(lines))
