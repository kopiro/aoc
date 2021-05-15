import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def puzzle_2(lines):
    result = 0
    lst = []
    while True:
        for num in lines:
            result = result + num
            if result in lst:
                return result
            lst.append(result)


def puzzle_1(lines):
    result = 0
    for num in lines:
        result = result + num
    return result


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [int(line.strip()) for line in f.readlines()]
    print(puzzle_2(lines))
