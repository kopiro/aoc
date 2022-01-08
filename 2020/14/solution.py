import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

rx = re.compile("mem\[(\d+)\] \= (\d+)")


def parse_line(line: str):
    if line[0:7] == 'mask = ':
        mask = line[7:]
        return ['set-mask', None, mask]
    else:
        addr, val = rx.match(line).groups()
        return ['set-mem', addr, val]


def puzzle_1(lines):
    registry = '0' * 32
    for line in lines:
        op, addr, val = parse_line(line)
        if op == 'set-mask':

        elif op == 'set-mem':


def puzzle_2(lines):
    return False


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print(puzzle_1(lines))
    # print(puzzle_2(lines))
