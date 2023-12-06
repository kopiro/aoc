import os
import re
import math

dir_path = os.path.dirname(os.path.realpath(__file__))

'''
For example:

Time:      7  15   30
Distance:  9  40  200
This document describes three races:

The first race lasts 7 milliseconds. The record distance in this race is 9 millimeters.
The second race lasts 15 milliseconds. The record distance in this race is 40 millimeters.
The third race lasts 30 milliseconds. The record distance in this race is 200 millimeters.
'''
def parse_lines_puzzle_one(lines):
    times = lines[0].split("Time:")[1]
    records = lines[1].split("Distance:")[1]
    times = [int(time) for time in re.split("\s+", times) if time != ""]
    records = [int(record) for record in re.split("\s+", records) if record != ""]
    return times, records

def puzzle_1(lines):
    times, records = parse_lines_puzzle_one(lines)
    r = 1
    for i in range(len(times)):
        time = times[i]
        record = (1 + records[i])
        h1 = math.ceil((time - math.sqrt(time * time - 4 * record)) / 2)
        h2 = math.floor((time + math.sqrt(time * time - 4 * record)) / 2)
        diff = abs(1 + h2 - h1)
        r *= diff

    return r

'''
As the race is about to start, you realize the piece of paper with race times and record distances you got earlier actually just has very bad kerning. There's really only one race - ignore the spaces between the numbers on each line.

So, the example from before:

Time:      7  15   30
Distance:  9  40  200
...now instead means this:

Time:      71530
Distance:  940200
'''
def parse_lines_puzzle_two(lines):
    times = lines[0].split("Time:")[1]
    records = lines[1].split("Distance:")[1]
    # Remove all the spaces and join all digits
    time = int("".join(times.split()))
    record = int("".join(records.split()))
    return time, record

def puzzle_2(lines):
    time, record = parse_lines_puzzle_two(lines)
    record += 1
    h1 = math.ceil((time - math.sqrt(time * time - 4 * record)) / 2)
    h2 = math.floor((time + math.sqrt(time * time - 4 * record)) / 2)
    diff = abs(1 + h2 - h1)
    return diff

if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print("Puzzle 1:", puzzle_1(lines))
    print("Puzzle 2:", puzzle_2(lines))
