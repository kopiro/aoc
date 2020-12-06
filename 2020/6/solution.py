import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def puzzle_1(lines):
    group = set()
    sum = 0
    for line in lines:
        if line == "":
            sum += len(group)
            group = set()
        else:
            for ch in line:
                group.add(ch)
    return sum


def puzzle_2(lines):
    group = {}
    group_size = 0
    ret_sum = 0
    for line in lines:
        if line == "":
            ret_sum += sum(1 if group[k] == group_size else 0 for k in group)
            group_size = 0
            group = {}
        else:
            group_size += 1
            for ch in line:
                if ch not in group:
                    group[ch] = 1
                else:
                    group[ch] += 1
    return ret_sum


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    lines.append("")
    print(puzzle_1(lines))
    print(puzzle_2(lines))
