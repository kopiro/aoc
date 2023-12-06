import os

dir_path = os.path.dirname(os.path.realpath(__file__))

'''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''

def parse_lines(lines):
    seeds = [int(seed) for seed in lines[0].replace('seeds: ', '').split(" ")]
    mapping = {}
    for line in lines[1:]:
        if line == "":
            continue
        if line.find("map:") != -1:
            last_key = line.replace(' map:', '')
            mapping[last_key] = []
        else:
            line_parsed = [int(i) for i in line.split(" ")]
            mapping[last_key].append({ 
                "src_start": line_parsed[1],
                "src_end": line_parsed[1] + line_parsed[2],
                "dst_start": line_parsed[0], 
                "dst_end": line_parsed[0] + line_parsed[2],
                "len": line_parsed[2]
            })
    return seeds, mapping

def get_steps(mapping, to_key, search_key):
    steps = []
    steps.append(search_key)
    while search_key != to_key:
        found = False
        for key in mapping.keys():
            k = key.split('-to-')
            if k[1] == search_key:
                steps.append(k[0])
                search_key = k[0]
                found = True
                break
        if not found:
            return None
    return steps
    
def transform_value_by_mapping_src_dst(mapping_key, value):
    for conv in mapping_key:
        if value >= conv["src_start"] and value <= conv["src_end"]:
            return conv["dst_start"] + (value - conv["src_start"])
    return value

def transform_value_by_mapping_dst_src(mapping_key, value):
    for conv in mapping_key:
        if value >= conv["dst_start"] and value <= conv["dst_end"]:
            return conv["src_start"] + (value - conv["dst_start"])
    return value


def puzzle_1(lines):
    seeds, mapping = parse_lines(lines)
    steps = get_steps(mapping, "seed", "location")
    if not steps:
        raise Exception("No path found")
    
    min_traversing_value = float('inf')
    steps.reverse()

    for seed in seeds:
        traversing_value = seed
        for index in range(0, len(steps) - 1, 1):
            step = steps[index]
            key = step + "-to-" + steps[index + 1]
            if not key in mapping:
                raise Exception("No key" + key + " found")
            traversing_value = transform_value_by_mapping_src_dst(mapping[key], traversing_value)
        min_traversing_value = min(min_traversing_value, traversing_value)
    
    return min_traversing_value

def puzzle_2(lines):
    seeds, mapping = parse_lines(lines)

    seeds_ranges = []
    for index in range(0, len(seeds) - 1, 2):
        seeds_ranges.append({
            "start": seeds[index],
            "end": seeds[index] + seeds[index+1]
        })
    seeds_ranges.sort(key=lambda x: x["start"])

    steps = get_steps(mapping, 'seed', "location")
    if not steps:
        raise Exception("No path found")
    
    best = float('inf')
    steps.reverse()

    # Start by traversing all steps
    for step_index in range(0, len(steps)-1, 1):
        step_key = steps[step_index] + "-to-" + steps[step_index+1]

        # Now try all possible ranges within this mapping
        for ranges in mapping[step_key]:
            # We want to try all possible intervals
            ranges_to_try = [
                ranges["src_start"], 
                ranges["src_end"], 
                ranges["dst_start"], 
                ranges["dst_end"]
            ]
            for r in ranges_to_try:

                # Traverse to right (reach location)
                tr_value = r
                for step_index_toright in range(step_index+1, len(steps)-1, 1):
                    step_key_toright = steps[step_index_toright] + "-to-" + steps[step_index_toright+1]
                    # src -> dst
                    tr_value = transform_value_by_mapping_src_dst(mapping[step_key_toright], tr_value)
                final_right_value = tr_value

                # If we found a new best min value, additional checks
                if final_right_value < best:
                    # Now traverse to left (reach seed)
                    tr_value = r
                    for step_index_toleft in range(step_index, -1, -1):
                        step_key_toleft = steps[step_index_toleft] + "-to-" + steps[step_index_toleft+1]
                        # dst -> src
                        tr_value = transform_value_by_mapping_dst_src(mapping[step_key_toleft], tr_value)
                    final_left_value = tr_value

                    #  nd check if seed is within ranges
                    found = False
                    for seed in seeds_ranges:
                        if final_left_value >= seed["start"] and final_left_value <= seed["end"]:
                            found = True
                            break
                    
                    # If we have reached seed, this means we have found a new best value
                    if found:
                        best = final_right_value                 
        
    return best


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    # print("Puzzle 1:", puzzle_1(lines))
    print("Puzzle 2:", puzzle_2(lines))
