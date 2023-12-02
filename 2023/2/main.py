import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# Line example
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def parse_line(line):
    id, sets = line.split(":")
    id = int(id.split(" ")[1])
    sets = sets.split(";")
    sets = [set.strip() for set in sets]
    sets = [set.split(",") for set in sets]
    sets = [[item.strip() for item in set] for set in sets]
    sets = [[item.split(" ") for item in set] for set in sets]
    sets = [[[int(item[0]), item[1]] for item in set] for set in sets]
    return id, sets

# Max only 12 red cubes, 13 green cubes, and 14 blue cubes
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
def is_valid(sets):
    for set in sets:
        red = 0
        green = 0
        blue = 0
        for item in set:
            if item[1] == "red":
                red += item[0]
            elif item[1] == "green":
                green += item[0]
            elif item[1] == "blue":
                blue += item[0]
        invalid = red > MAX_RED or green > MAX_GREEN or blue > MAX_BLUE
        if invalid:
            return False
    return True

def puzzle_1(lines):
    sum_valid = 0
    for line in lines:
        id, sets = parse_line(line)
        if is_valid(sets):
            sum_valid += id
    return sum_valid


def get_max_each_color(sets):
    max_red = 0
    max_green = 0
    max_blue = 0
    for set in sets:
        red = 0
        green = 0
        blue = 0
        for item in set:
            if item[1] == "red":
                red += item[0]
            elif item[1] == "green":
                green += item[0]
            elif item[1] == "blue":
                blue += item[0]
        max_red = max(max_red, red)
        max_green = max(max_green, green)
        max_blue = max(max_blue, blue)
    return max_red, max_green, max_blue

def puzzle_2(lines):
    sum_powers = 0
    for line in lines:
        id, sets = parse_line(line)
        max_colors = get_max_each_color(sets)
        power = max_colors[0] * max_colors[1] * max_colors[2]
        sum_powers += power
    return sum_powers


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print(puzzle_1(lines))
    print(puzzle_2(lines))
