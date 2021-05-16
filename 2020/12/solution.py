import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def puzzle_1(lines):
    x, y, dir = 0, 0, 0
    for cmd in lines:
        new_dir, power = cmd[0:1], int(cmd[1:])
        if new_dir == 'N':
            y += power
        elif new_dir == 'E':
            x += power
        elif new_dir == 'W':
            x -= power
        elif new_dir == 'S':
            y -= power
        elif new_dir == 'L':
            dir += power
        elif new_dir == 'R':
            dir -= power
        elif new_dir == 'F':
            if dir % 360 == 0:
                x += power
            elif dir % 360 == 90:
                y += power
            elif dir % 360 == 180:
                x -= power
            elif dir % 360 == 270:
                y -= power
        print(x, y)
    print(abs(x)+abs(y))


def puzzle_2(lines):
    x, y, wpx, wpy, dir = 0, 0, 10, 1, 0
    for cmd in lines:
        new_dir, power = cmd[0:1], int(cmd[1:])
        if new_dir == 'N':
            wpy += power
        elif new_dir == 'E':
            wpx += power
        elif new_dir == 'W':
            wpx -= power
        elif new_dir == 'S':
            wpy -= power
        elif new_dir == 'R' or new_dir == 'L':
            if new_dir == "L":
                angle = power % 360
            elif new_dir == "R":
                angle = -power % 360
            if angle == 0:
                pass
            elif angle == 90:
                (wpx, wpy) = (-wpy, wpx)
            elif angle == 180:
                (wpx, wpy) = (-wpx, -wpy)
            elif angle == 270:
                (wpx, wpy) = (wpy, -wpx)
        elif new_dir == 'F':
            x += power * (wpx)
            y += power * (wpy)
        print(x, y, wpx, wpy)
    print(abs(x)+abs(y))


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    # print(puzzle_1(lines))
    print(puzzle_2(lines))
