import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_line(line):
    m = re.match('(\w+) ([+-])(\d+)', line)
    if m == None:
        return None
    op = m.group(1)
    val = (-1 if m.group(2) == '-' else 1) * (int)(m.group(3))
    return op, val


def puzzle_1(lines):
    registry_acc = 0
    registry_pc = 0
    pc_executed = {}
    size = len(lines)
    while True:
        if registry_pc == size:
            break
        if registry_pc in pc_executed:
            return registry_acc

        pc_executed[registry_pc] = True
        line = lines[registry_pc]

        op, val = parse_line(line)
        if op == 'acc':
            registry_acc += val
            registry_pc += 1
        elif op == 'jmp':
            registry_pc += val
        elif op == 'nop':
            registry_pc += 1

    return False


def check_if_finish(line_to_change, size):
    registry_acc = 0
    registry_pc = 0
    pc_executed = {}
    while True:
        if registry_pc == size:
            return registry_acc
        if registry_pc in pc_executed:
            return False

        pc_executed[registry_pc] = True
        line = lines[registry_pc]

        op, val = parse_line(line)
        if line_to_change == line:
            op = ('nop' if op == 'jmp' else 'jmp')

        if op == 'acc':
            registry_acc += val
            registry_pc += 1
        elif op == 'jmp':
            registry_pc += val
        elif op == 'nop':
            registry_pc += 1


def puzzle_2(lines):
    size = len(lines)
    for line_to_change in lines:
        if line_to_change[0:3] == 'jmp' or line_to_change[0:3] == 'nop':
            acc = check_if_finish(line_to_change, size)
            if acc != False:
                return acc


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print(puzzle_1(lines))
    print(puzzle_2(lines))
