import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def puzzle_1(lines):
    preamble = 25
    for i in range(preamble, len(lines)):
        sums = set()
        for j in range(i - preamble, i):
            for k in range(j, i):
                sums.add(int(lines[j]) + int(lines[k]))
        num = int(lines[i])
        if num not in sums:
            return num


def puzzle_2(lines, num):
    for i in range(0, len(lines)):
        for j in range(i+1, len(lines)):
            s = 0
            ab = False
            for x in range(i, j):
                s += int(lines[x])
                if s > num:
                    ab = True
                    break
            if ab:
                break
            if num == s:
                sublist = map(lambda x: int(x), lines[i:j])
                sublist.sort()
                return int(sublist[0]) + int(sublist[-1])


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print(puzzle_1(lines))
    print(puzzle_2(lines, puzzle_1(lines)))
