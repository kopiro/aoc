import functools
import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))


"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""


def puzzle_2(lines):
    passport = {}

    def hgt(v):
        m = re.match('(\d+)(cm|in)', v)
        if m == None:
            return False
        n = (int)(m.group(1))
        d = m.group(2)
        if d == "cm":
            return n >= 150 and n <= 193
        elif d == "in":
            return n >= 59 and n <= 76
        else:
            return False

    required = {
        'byr': lambda v: (int)(v) >= 1920 and (int)(v) <= 2002,
        'iyr': lambda v: (int)(v) >= 2010 and (int)(v) <= 2020,
        'eyr': lambda v: (int)(v) >= 2020 and (int)(v) <= 2030,
        'hgt': hgt,
        'hcl': lambda v: re.match('^(\#[a-z0-9]{6})$', v) != None,
        'ecl': lambda v: re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', v) != None,
        'pid': lambda v: re.match('^([0-9]{9})$', v) != None,
    }
    invalid_count = 0
    valid_count = 0
    for line in lines:
        if line != "":
            for el in line.split(" "):
                k, v = el.split(":")
                passport[k] = v
        else:
            valid = True
            for r in required:
                if (r not in passport) or (required[r](passport[r])) != True:
                    print("Invalid", r, passport[r] if r in passport else '')
                    valid = False
                    break
            if valid:
                print(passport)
                valid_count += 1
            else:
                invalid_count += 1
            passport = {}
    return valid_count


def puzzle_1(lines):
    passport = {}
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    invalid_count = 0
    valid_count = 0
    for line in lines:
        if line != "":
            for el in line.split(" "):
                k, v = el.split(":")
                passport[k] = v
        else:
            valid = True
            for r in required:
                if r not in passport:
                    valid = False
                    break
            if valid:
                valid_count += 1
            else:
                invalid_count += 1
            passport = {}
    return valid_count


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    lines.append("")
    print(puzzle_1(lines))
    print(puzzle_2(lines))
