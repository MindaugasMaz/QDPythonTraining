import re
from collections import defaultdict

def is_valid_position(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def get_adjacent(arr, x, y):
    n = len(arr)
    m = len(arr[0])
    adjacent_chars = []

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            new_x = x + dx
            new_y = y + dy
            if is_valid_position(new_x, new_y, n, m):
                adjacent_chars.append([arr[new_x][new_y], new_x, new_y])

    return adjacent_chars

def repeating_gear_indexes(gear_idxs):
    gear_idxs_dict = defaultdict(list)
    for index_in_list, gear_idx in enumerate(gear_idxs):
        gear_idxs_dict[str(gear_idx)].append(index_in_list)

    return {key: value for key, value in gear_idxs_dict.items() if len(value) > 1}

def calculate_sum(data):
    sum = 0
    number_pattern = re.compile(r'[0-9]+')

    numbers_near_gears = []
    gear_idxs = []
    for row_idx, line in enumerate(data):
        for match in number_pattern.finditer(line):
            start_idx = match.start()
            end_idx = match.end()
            gear_idx = match.group()

            for x in range(start_idx, end_idx):
                adjacent_chars = get_adjacent(data, row_idx, x)
                for char in adjacent_chars:
                    if char[0] == "*":
                        numbers_near_gears.append(gear_idx)
                        gear_idxs.append([char[1], char[2]])
                        break
                else:
                    continue
                break

    repeating_gear_idxs = repeating_gear_indexes(gear_idxs)

    for key, value in repeating_gear_idxs.items():
        first_gear_number = int(numbers_near_gears[value[0]])
        second_gear_number = int(numbers_near_gears[value[1]])
        gear_ratio = first_gear_number * second_gear_number
        # print(f"Gear at {key}. Its ratio: {gear_ratio}")
        
        sum = sum + gear_ratio

    return sum

def main():
    with open('input.txt') as f:
        data = f.readlines()

    print(f"{calculate_sum(data)}")

if __name__ == "__main__":
    main()
