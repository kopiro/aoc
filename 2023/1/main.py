import os

dir_path = os.path.dirname(os.path.realpath(__file__))

k_english_numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine": 9
}

def puzzle_1(lines):
    # for each line of string find first the first occurence of number, last number and sum them
    sum = 0
    for l in lines:
        first = None
        last = None
        for i in range(0,len(l)):
            if l[i].isdigit():
                first = (l[i])
                break
        for i in range(len(l)-1, -1, -1):
            if l[i].isdigit():
                last = (l[i])
                break
        if first and last:
            sum += int(str(first) + str(last))
        else:
            raise Exception("No numbers found in line: " + l)
    return sum

def match_number(line, index):
    for k in k_english_numbers.keys():
        top = index + len(k)
        if top > len(line):
            continue
        if str(line[index:top]) == k:
            return k_english_numbers[k]

def puzzle_2(lines):
    sum = 0
    for l in lines:
        first = None
        last = None
        for i in range(0,len(l)):
            if l[i].isdigit():
                first = (l[i])
                break
            m = match_number(l, i)
            if m:
                first = m
                break
        for i in range(len(l)-1, -1, -1):
            if l[i].isdigit():
                last = (l[i])
                break
            m = match_number(l, i)
            if m:
                last = m
                break
                
        if first and last:
            sum += int(str(first) + str(last))
        else:
            raise Exception("No numbers found in line: " + l)
    return sum


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print(puzzle_1(lines))
    print(puzzle_2(lines))
