import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def is_number_or_dot(char):
    return char.isdigit() or char == "."

# Map with all cooordinates already been added so we can skip them
added_coordinates = {}

def match_number_until_digit(line, x, y, originator_x, originator_y):
    if not line[x].isdigit():
        return None
    number = ""
    tmp_added_coordinates = {}
    # in reverse order
    for _x in range(x, -1, -1):
        char = line[_x]
        if (_x, y) in added_coordinates:
            return None
        if char.isdigit():
            tmp_added_coordinates[(_x, y)] = True
            number = char + number
        else:
            break
    for _x in range(x+1, len(line)):
        char = line[_x]
        if (_x, y) in added_coordinates:
            return None
        if char.isdigit():
            tmp_added_coordinates[(_x, y)] = True
            number = number + char
        else:
            break
    added_coordinates.update(tmp_added_coordinates)
    if number:
        return int(number)

def puzzle_1(lines):
    numbers = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if not is_number_or_dot(char):
                # Get all numbers around the symbol
                for _x in range(-1, 2):
                    for _y in range(-1, 2):
                        if _x + x < 0 or _y + y < 0 or _x + x >= len(line) or _y + y >= len(lines):
                            continue
                        if _x == 0 and _y == 0:
                            continue
                        number = match_number_until_digit(lines[y+_y], x+_x, y+_y, x, y)
                        if number:
                            numbers.append(number)
    result = sum(numbers)
    return result


def puzzle_2(lines):
    sum = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "*":
                numbers = []
                # Get all numbers around the symbol
                for _x in range(-1, 2):
                    for _y in range(-1, 2):
                        if _x + x < 0 or _y + y < 0 or _x + x >= len(line) or _y + y >= len(lines):
                            continue
                        if _x == 0 and _y == 0:
                            continue
                        number = match_number_until_digit(lines[y+_y], x+_x, y+_y, x, y)
                        if number:
                            numbers.append(number)
                if len(numbers) == 2:
                    gear_ratio = numbers[0] * numbers[1]
                    sum += gear_ratio
    return sum


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print("Puzzle 1:", puzzle_1(lines))
    print("Puzzle 2:", puzzle_2(lines))
