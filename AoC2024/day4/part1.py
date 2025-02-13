from enum import Enum


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP_LEFT = (-1, -1)
    UP_RIGHT = (-1, 1)
    DOWN_LEFT = (1, -1)
    DOWN_RIGHT = (1, 1)


data = []


def check_word_in_direction(row: int, col: int, letters: str, direction: Direction) -> bool:
    try:
        for i, letter in enumerate(letters):
            new_row = row + direction.value[0] * (i+1)
            new_col = col + direction.value[1] * (i+1)
            if data[new_row][new_col] != letter:
                return False
        return True
    except IndexError:
        return False


def search_for_word(row: int, col: int, letters: str) -> int:
    found = 0
    for direction in Direction:
        if check_word_in_direction(row, col, letters, direction):
            found += 1
    return found


def main():
    global data
    total = 0

    with open('input.txt') as f:
        data = f.read().splitlines()

    letters = "MAS"
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'X':  # Only start checking from X
                total += search_for_word(i, j, letters)

    print(f"Total XMAS found: {total}")


if __name__ == '__main__':
    main()
