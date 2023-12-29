from collections import Counter

cards_slice = slice(0, 5)
bid_slice = slice(6, None)

card_strength = {
    'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
    '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
}


class Hand:
    def __init__(self, line) -> None:
        self.cards = tuple(line[cards_slice])
        self.bid = int(line[bid_slice])
        self.rank = self.__value_rank()

    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank < other.rank

        return (self.rank, tuple(card_strength[card] for card in self.cards)) < \
               (other.rank, tuple(card_strength[card] for card in other.cards))

    def __str__(self) -> str:
        return f"Hand - {self.cards} {self.bid} {self.rank}"

    def __value_rank(self):
        card_counts = Counter(self.cards)
        sorted_counts = sorted(card_counts.values(), reverse=True)
        return {
            (5,): 7, (4, 1): 6, (3, 2): 5,
            (3, 1, 1): 4, (2, 2, 1): 3, (2, 1, 1, 1): 2
        }.get(tuple(sorted_counts), 1)


def calc_total_bid(hands: list):
    total = 0
    for n, hand in enumerate(hands, start=1):
        total += hand.bid*(n)
    return total


def main():
    with open('data.txt', 'r') as f:
        hands = [Hand(line.strip()) for line in f]

    hands.sort()
    print(calc_total_bid(hands))


if __name__ == "__main__":
    main()
