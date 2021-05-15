import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def puzzle_1(lines):
    lines = sorted(lines)
    device = lines[-1] + 3
    diffs = [0, 0, 0, 0]
    previous = 0
    for line in lines + [device]:
        d = line - previous
        previous = line
        diffs[d] += 1
    return diffs[1] * diffs[3]


memo = {}


def puzzle_2_rec(lines, previous, start):
    if start == len(lines)-1:
        return +1

    s = 0
    for j in range(start, len(lines)):
        d = lines[j] - previous
        if d <= 3:
            if j not in memo:
                val = puzzle_2_rec(lines, lines[j], j+1)
                memo[j] = val
                s += val
            else:
                s += memo[j]
        else:
            break
    return s


def puzzle_2(lines):
    lines = sorted(lines)
    device = lines[-1] + 3
    lines.append(device)
    combs = puzzle_2_rec(lines, 0, 0)
    return combs


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [int(line.strip()) for line in f.readlines()]
    # print(puzzle_1(lines))
    print(puzzle_2(lines))
