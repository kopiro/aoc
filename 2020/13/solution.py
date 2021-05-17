import os
from functools import reduce

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_lines_with_x(lines):
    ts = int(lines[0])
    buses = []
    for bus in lines[1].split(","):
        buses.append((int(bus) if bus != 'x' else 'x'))
    return ts, buses


def parse_lines(lines):
    ts = int(lines[0])
    buses = []
    for bus in lines[1].split(","):
        if bus != 'x':
            buses.append(int(bus))
    return ts, buses


def puzzle_1(lines):
    ts, buses = parse_lines(lines)
    min_ts = None
    id_bus = None
    for bus in buses:
        mod = ((ts // bus) + 1) * bus
        if mod < min_ts or min_ts is None:
            min_ts = mod
            id_bus = bus
    min_ts -= ts
    print(min_ts, id_bus)
    return id_bus * min_ts


def solve_nx_eq1_mod_y(n, y):
    # We can definitely do better than this isntead of iterating
    for i in range(1, y):
        if (n * i) % y == 1:
            return i


def puzzle_2(lines):
    ts, buses = parse_lines_with_x(lines)
    xs = []
    i = 0
    mod_prod = 1
    for bus in buses:
        if bus != 'x':
            xs.append([i, bus])
            mod_prod = mod_prod * bus
        i += 1
    s = 0
    for i in range(0, len(xs)):
        prod = 1
        x = xs[i][0]
        bus = xs[i][1]
        for j in range(0, len(xs)):
            if i != j:
                prod = prod * xs[j][1]
        sol = solve_nx_eq1_mod_y(prod, bus)
        to_add = (sol * prod * x)
        s += to_add
    max_mul = s//mod_prod
    result_neg = abs(s - ((max_mul-1) * mod_prod))
    result_pos = abs(s - ((max_mul+1) * mod_prod))
    return min(result_neg, result_pos)


if __name__ == "__main__":
    with open(dir_path + "/simple.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    # print(puzzle_1(lines))
    print(puzzle_2(lines))
