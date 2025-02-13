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

        letter = data[new_row][new_col]
        print(f"Checking position ({new_row}, {new_col}): found {letter}")
        return letter
    except IndexError:
        return None


def search_for_X(row: int, col: int) -> bool:
    found = {'M': 0, 'S': 0}
    print(f"\nChecking A at position ({row}, {col})")
    for direction in Direction:
        letter = get_symbol_in_direction(row, col, direction)
        print(f"Direction {direction.name}: found {letter}")
        if letter == 'M' or letter == 'S':
            found[letter] += 1

    print(f"Total found: M={found['M']}, S={found['S']}")
    return found['M'] == 2 and found['S'] == 2


def main():
    global data
    total = 0

    with open('input.txt') as f:
        data = f.read().splitlines()

    # Print the grid for debugging
    print("Grid:")
    for row in data:
        print(row)
    print()

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'A':
                if search_for_X(i, j):
                    print(f"Found valid X-MAS at ({i}, {j})")
                    total += 1

    print(f"Total X-MAS found: {total}")


if __name__ == '__main__':
    main()
