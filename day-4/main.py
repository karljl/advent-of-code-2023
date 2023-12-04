import re


def read_file(file_name: str) -> list[str]:
    with open(file_name, 'r') as file:
        return file.readlines()


def clean_data(data: list[str]) -> list[tuple]:
    output = []

    for row in data:
        row = re.split(r'[:|]', row)
        numbers_you_have = {ch for ch in row[1].split()}
        winning_numbers = {ch for ch in row[2].split()}
        output.append((numbers_you_have, winning_numbers))

    return output


def calculate_score(card: tuple[set]) -> int:
    winning_numbers = card[0] & card[1]
    if len(winning_numbers) == 0:
        return 0
    # return int(2 ** (len(winning_numbers) - 1))
    return len(winning_numbers)


def get_number_of_tickets(rows: list[tuple]):
    output = 0
    cards = {card_nr: 1 for card_nr in range(1, len(rows) + 1)}

    for card, row in enumerate(rows, 1):
        output += cards[card]
        winning_tickets = calculate_score(row)
        for x in range(1, winning_tickets + 1):
            if card + x > len(rows):
                break
            cards[card + x] += cards[card] * 1

    return output


def main() -> int:
    input_file = './input.txt'
    rows = clean_data(read_file(input_file))
    output = get_number_of_tickets(rows)
    return output


if __name__ == '__main__':
    result = main()
    print(result)
