from collections import deque


numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


# ----------------------- STEP 1 ----------------------
#
# def get_value(line: str, idx: int, step: int) -> str:
#     while not line[idx].isdecimal():
#         idx += step
#     return line[idx]


def get_value(line: str, idx: int, step: int) -> str:
    value = None
    word = deque()

    numbers_map = {key[::step]: val for key, val in numbers.items()}

    while value is None:
        cur_word = ''.join(word)
        if cur_word in numbers_map:
            value = numbers_map[cur_word]
        elif line[idx].isdecimal():
            value = line[idx]
        else:
            while not any(num.startswith(cur_word) for num in numbers_map):
                word.popleft()
                cur_word = ''.join(word)
            word.append(line[idx])
            idx += step

    return value


def main():
    total = 0
    with open('./input.txt', 'r') as file:
        for row in file.readlines():
            row = row.strip()
            digit = get_value(row, 0, 1) + get_value(row, len(row) - 1, -1)
            total += int(digit)
    return total


if __name__ == '__main__':
    result = main()
    print(result)
