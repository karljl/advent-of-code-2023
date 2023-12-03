import re
from functools import reduce

INPUT_FILE = './input.txt'


def get_game_id(text: str) -> int:
    pattern = r'Game (\d+)'
    result = re.search(pattern, text).group(1)
    return int(result)


def get_rounds(text: str) -> list:
    pattern = r' (\d+) (\w+)'
    result = re.findall(pattern, text)
    return result


def get_round_result(game_round: list) -> tuple[int, str]:
    amount, color = int(game_round[0]), game_round[1]
    return amount, color


def is_round_valid(amount: int, color: str) -> bool:
    max_amount_of_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    return max_amount_of_cubes[color] >= amount


# ----------------------- STEP 1 ----------------------
#
# def calculate_result() -> int:
#     result = 0
#
#     with open(INPUT_FILE, 'r') as file:
#         for row in file.readlines():
#             game_id = get_game_id(row)
#             rounds = get_rounds(row)
#             for round_ in rounds:
#                 amount, color = get_round_result(round_)
#                 if not is_round_valid(amount, color):
#                     break
#             else:
#                 result += game_id
#
#     return result


def calculate_result() -> int:
    result = 0

    with open(INPUT_FILE, 'r') as file:
        for row in file.readlines():

            min_amount_of_cubes = {
                'red': 0,
                'green': 0,
                'blue': 0
            }

            rounds = get_rounds(row)
            for round_ in rounds:
                amount, color = get_round_result(round_)
                min_amount_of_cubes[color] = max(min_amount_of_cubes[color], amount)

            result += reduce(lambda x, y: x * y, min_amount_of_cubes.values())

    return result


def main():
    result = calculate_result()
    print(result)


if __name__ == '__main__':
    main()
