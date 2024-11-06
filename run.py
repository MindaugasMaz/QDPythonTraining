import re

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
                adjacent_chars.append(arr[new_x][new_y])

    return adjacent_chars

def calculate_sum(data):
    sum = 0
    number_pattern = re.compile(r'[0-9]+')

    for row, line in enumerate(data):
        for match in number_pattern.finditer(line):
            start_idx = match.start()
            end_idx = match.end()
            number = match.group()

            for x in range(start_idx, end_idx):
                adjacent_chars = get_adjacent(data, row, x)
                for char in adjacent_chars:
                    if not char.isdigit() and char != '.' and char != '\n':
                        print(f"Line {row + 1}: Found number {number}")
                        sum += int(number)
                        break
                else:
                    continue
                break

    return sum

def main():
    with open('input.txt') as f:
        data = f.readlines()

    print(f"{calculate_sum(data)}")

if __name__ == "__main__":
    main()
