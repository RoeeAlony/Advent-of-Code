from enum import Enum


class Direction(Enum):
    UP_LEFT = (-1, -1)
    UP_RIGHT = (-1, 1)
    DOWN_LEFT = (1, -1)
    DOWN_RIGHT = (1, 1)


data = []


def get_symbol_in_direction(row: int, col: int, direction: Direction) -> str:
    try:
        new_row = row + direction.value[0]
        new_col = col + direction.value[1]
        return data[new_row][new_col]
    except IndexError:
        return None


def search_for_X(row: int, col: int) -> bool:
    found = {'M': 0, 'S': 0}
    for direction in Direction:
        letter = get_symbol_in_direction(row, col, direction)
        if letter == 'M' or letter == 'S':
            found[letter] += 1

    return found['M'] == 2 and found['S'] == 2


def main():
    global data
    total = 0
    totalA = 0

    with open('input.txt') as f:
        data = f.read().splitlines()

    for i in range(len(data)):
        for j in range(len(data[i])):
            # Only start checking from A
            if data[i][j] == 'A':
                totalA += 1
            if data[i][j] == 'A' and search_for_X(i, j):
                total += 1

    print(f"Total XMAS found: {total}")
    print(f"Total A found: {totalA}")


if __name__ == '__main__':
    main()
