from collections import defaultdict

INPUT_FILE = './input.txt'


def get_symbols(rows: list[str]) -> set[str]:
    output = set()

    for line in rows:
        for ch in line:
            if not ch.isalnum() and ch not in {'.', '\n'}:
                output.add(ch)

    return output


def get_adjacent_indexes(x: int, y: int, last_x: int, last_y: int) -> set[tuple[int, int]]:
    output = set()

    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            new_x, new_y = x + x_offset, y + y_offset
            if 0 <= new_x <= last_x and 0 <= new_y <= last_y and (x, y) != (new_x, new_y):
                output.add((new_x, new_y))

    return output


def read_file(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        return f.readlines()


# --------------------------------------------- STEP 1 ---------------------------------------
#
# def process_rows(rows, symbols) -> int:
#     output = 0
#     is_adjacent = False
#     for depth, row in enumerate(rows):
#         current_nr = []
#         row = row.strip()
#         for width, char in enumerate(row):
#             adjacent_chars = get_adjacent_indexes(depth, width, len(row) - 1, len(rows) - 1)
#             if char.isdecimal():
#                 current_nr.append(char)
#                 if any(rows[x][y] in symbols for (x, y) in adjacent_chars):
#                     is_adjacent = True
#             else:
#                 if is_adjacent and len(current_nr) > 0:
#                     output += int(''.join(current_nr))
#                 current_nr.clear()
#                 is_adjacent = False
#
#         if is_adjacent and len(current_nr) > 0:
#             output += int(''.join(current_nr))
#
#     return output


def process_rows(rows) -> int:
    output = 0
    is_adjacent = False
    gear_map = defaultdict(list)

    for depth, row in enumerate(rows):
        current_nr = []
        current_gear_indexes = set()
        row = row.strip()
        for width, char in enumerate(row):
            adjacent_chars = get_adjacent_indexes(depth, width, len(row) - 1, len(rows) - 1)
            if char.isdecimal():
                current_nr.append(char)
                for x, y in adjacent_chars:
                    if rows[x][y] == '*':
                        is_adjacent = True
                        current_gear_indexes.add((x, y))
            else:
                if is_adjacent and len(current_nr) > 0:
                    for x, y in current_gear_indexes:
                        gear_map[(x, y)].append(int(''.join(current_nr)))
                current_nr.clear()
                current_gear_indexes.clear()
                is_adjacent = False

        if is_adjacent and len(current_nr) > 0:
            for x, y in current_gear_indexes:
                gear_map[(x, y)].append(int(''.join(current_nr)))

    valid_gears = list(filter(lambda arr: len(arr) == 2, gear_map.values()))
    for x, y in valid_gears:
        output += x * y

    return output


def main() -> int:
    rows = [row.strip() for row in read_file(INPUT_FILE)]
    # symbols = get_symbols(rows)  ------------ STEP 1 -------------
    # output = process_rows(rows, symbols)  ---------------- STEP 1 ---------------
    output = process_rows(rows)
    return output


if __name__ == '__main__':
    result = main()
    print(result)
