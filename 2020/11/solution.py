import os
from copy import deepcopy

dir_path = os.path.dirname(os.path.realpath(__file__))


def puzzle1_rule_occupy(lines, row_index, col_index):
    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    if lines[row_index][col_index] != 'L':
        return False
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            if row_index+y < 0 or col_index+x < 0:
                continue
            try:
                cell_adj = lines[row_index+y][col_index+x]
                if cell_adj == "#":
                    return False
            except IndexError:
                False
    return True


def puzzle1_rule_free(lines, row_index, col_index):
    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    if lines[row_index][col_index] != '#':
        return False
    count = 0
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            if row_index+y < 0 or col_index+x < 0:
                continue
            try:
                cell_adj = lines[row_index+y][col_index+x]
                if cell_adj == "#":
                    count += 1
                    if count >= 4:
                        return True
            except IndexError:
                False
    return count >= 4


def puzzle_1(lines):
    changes_happened = True
    loop = 0
    while changes_happened:
        changes_happened = False
        lines_copy = deepcopy(lines)
        for row_index in range(0, len(lines)):
            for col_index in range(0, len(lines[row_index])):
                if puzzle1_rule_occupy(lines, row_index, col_index):
                    changes_happened = True
                    lines_copy[row_index][col_index] = "#"
                else:
                    if puzzle1_rule_free(lines, row_index, col_index):
                        changes_happened = True
                        lines_copy[row_index][col_index] = "L"
        lines = lines_copy
        loop += 1
    count = sum([e == "#" for row in lines for e in row])
    return count


def puzzle1_rule_free(lines, row_index, col_index):
    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    if lines[row_index][col_index] != '#':
        return False
    count = 0
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            if row_index+y < 0 or col_index+x < 0:
                continue
            try:
                cell_adj = lines[row_index+y][col_index+x]
                if cell_adj == "#":
                    count += 1
                    if count >= 4:
                        return True
            except IndexError:
                False
    return count >= 4


def in_bound(lines, row, col):
    return row >= 0 and col >= 0 and row < len(lines) and col < len(lines[0])


def puzzle2_rule_occupy(lines, row_index, col_index):
    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    if lines[row_index][col_index] != 'L':
        return False
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            row, col = row_index+y, col_index+x
            while in_bound(lines, row, col):
                cell_adj = lines[row][col]
                if cell_adj == "L":
                    break
                if cell_adj == "#":
                    return False
                row, col = row+y, col+x
    return True


def puzzle2_rule_free(lines, row_index, col_index):
    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    if lines[row_index][col_index] != '#':
        return False
    count = 0
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            row, col = row_index+y, col_index+x
            while in_bound(lines, row, col):
                cell_adj = lines[row][col]
                if cell_adj == "L":
                    break
                if cell_adj == "#":
                    count += 1
                    break
                row, col = row+y, col+x
    return count >= 5


def puzzle_2(lines):
    changes_happened = True
    loop = 0
    while changes_happened:
        changes_happened = False
        lines_copy = deepcopy(lines)
        for row_index in range(0, len(lines)):
            for col_index in range(0, len(lines[row_index])):
                if puzzle2_rule_occupy(lines, row_index, col_index):
                    changes_happened = True
                    lines_copy[row_index][col_index] = "#"
                else:
                    if puzzle2_rule_free(lines, row_index, col_index):
                        changes_happened = True
                        lines_copy[row_index][col_index] = "L"
        lines = lines_copy
        loop += 1
        # print("\n".join(["".join(e) for e in lines]))
        # print(loop)
    count = sum([e == "#" for row in lines for e in row])
    return count


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [list(line.strip()) for line in f.readlines()]
    print(puzzle_2(lines))
