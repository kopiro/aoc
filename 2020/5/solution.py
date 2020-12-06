import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def puzzle_1(lines):
    max_seat_id = 0
    for line in lines:
        y = 0
        max_y = 128
        x = 0
        max_x = 8
        for instruction in line:
            if instruction == "B":
                y += (max_y-y)/2
            elif instruction == "F":
                max_y -= (max_y-y)/2
            elif instruction == "R":
                x += (max_x-x)/2
            elif instruction == "L":
                max_x -= (max_x-x)/2
        seat_id = y * 8 + x
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id


def puzzle_2(lines):
    seats = []
    for line in lines:
        y = 0
        max_y = 128
        x = 0
        max_x = 8
        for instruction in line:
            if instruction == "B":
                y += (max_y-y)/2
            elif instruction == "F":
                max_y -= (max_y-y)/2
            elif instruction == "R":
                x += (max_x-x)/2
            elif instruction == "L":
                max_x -= (max_x-x)/2
        seat_id = y * 8 + x
        seats.append(seat_id)
    seats.sort()
    for i in range(0, len(seats)-1):
        if seats[i+1] - seats[i] > 1:
            return seats[i] + 1


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print(puzzle_1(lines))
    print(puzzle_2(lines))
