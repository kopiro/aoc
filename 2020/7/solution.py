import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_line(line):
    m = re.match('(.+) bags contain (.+)', line)
    container = m.group(1)
    if m.group(2) == 'no other bags.':
        return container, {}
    bags = {}
    for e in m.group(2).split(", "):
        m = re.match('(\d+) (.+) bags?', e)
        bags[m.group(2)] = (int)(m.group(1))
    return container, bags


def traverse_1(all_bags, bag):
    s = 0
    for sub_bag in all_bags[bag]:
        if all_bags[sub_bag]:
            s += traverse_1(all_bags, sub_bag)
    return s + (1 if bag == 'shiny gold' else 0)


def puzzle_1(lines):
    all_bags = {}
    for line in lines:
        container, bags = parse_line(line)
        all_bags[container] = bags
    s = 0
    for bag in all_bags:
        bs = traverse_1(all_bags, bag)
        if bag != 'shiny gold' and bs >= 1:
            s += 1
    return s


def traverse_2(all_bags, bag):
    if len(all_bags[bag]) == 0:
        print('end', bag)
        return 0
    s = 0
    for sub_bag in all_bags[bag]:
        count = all_bags[bag][sub_bag]
        s += count + count * traverse_2(all_bags, sub_bag)
    return s


def puzzle_2(lines):
    all_bags = {}
    for line in lines:
        container, bags = parse_line(line)
        all_bags[container] = bags
    return traverse_2(all_bags, 'shiny gold')


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print(puzzle_1(lines))
    print(puzzle_2(lines))
