import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def parse_line(line):
    values = [int(x) for x in line.split(" ")]
    return values

def puzzle_1(lines):
    res = 0
    for line in lines:
        values = parse_line(line)
        tree = [values]
        for j in range(0, len(values)-1):
            new_values = []
            all_zeros = True
            for i in range(0, len(tree[j])-1):
                diff = tree[j][i+1] - tree[j][i]
                new_values.append(diff)
                if diff != 0:
                    all_zeros = False
            tree.append(new_values)
            if all_zeros:
                break
        # add zero at the end of the tree
        tree[-1].append(0)
        for j in range(len(tree)-2, -1, -1):
            tree[j].append(tree[j+1][-1] + tree[j][-1])
        val = tree[0][-1]
        res += val
    return res


def puzzle_2(lines):
    res = 0
    for line in lines:
        values = parse_line(line)
        tree = [values]
        for j in range(0, len(values)-1):
            new_values = []
            all_zeros = True
            for i in range(0, len(tree[j])-1):
                diff = tree[j][i+1] - tree[j][i]
                new_values.append(diff)
                if diff != 0:
                    all_zeros = False
            tree.append(new_values)
            if all_zeros:
                break
        # add zero at the end of the tree
        tree[-1].insert(0, 0)
        for j in range(len(tree)-2, -1, -1):
            print(tree[j+1][0], tree[j][0])
            tree[j].insert(0, tree[j][0] - tree[j+1][0])
        val = tree[0][0]
        res += val
    # print(tree)
    return res


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print("Puzzle 1:", puzzle_1(lines))
    print("Puzzle 2:", puzzle_2(lines))
