import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))

'''
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
'''
def parse_line(lines):
    lr_inst = lines[0]
    maps = {}
    for line in lines[2:]:
        key, value = line.split(" = ")
        value = value[1:-1].split(", ")
        maps[key] = value
    return lr_inst, maps

def puzzle_1(lines):
    lr_inst, maps = parse_line(lines)
    val = 'AAA'
    steps = 0
    lr_step = 0
    while val != 'ZZZ':
        lr_index = 0 if lr_inst[lr_step % len(lr_inst)] == 'L' else 1
        val = maps[val][lr_index]
        steps += 1
        lr_step += 1

    return steps


def puzzle_2(lines):
    lr_inst, maps = parse_line(lines)
    steps = {}
    for key in maps.keys():
        if key[2] == 'A':
            steps[key] = {"lr_step": 0, "val": key, "path":[]}
    for key in steps.keys():
        step = steps[key]
        while step['val'][2] != 'Z':
            step = steps[key]
            lr_step, val = step["lr_step"], step["val"]
            lr_index = 0 if lr_inst[lr_step % len(lr_inst)] == 'L' else 1
            step["val"] = maps[val][lr_index]
            step['path'].append(step["val"])
            step["lr_step"] += 1

    return math.lcm(*[e['lr_step'] for e in steps.values()])

if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    #print("Puzzle 1:", puzzle_1(lines))
    print("Puzzle 2:", puzzle_2(lines))
