card_strength = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1,
}


class Hand:
    def __init__(self, line) -> None:
        self.cards = tuple(line[:5])
        self.bid = int(line[6:])
        self.rank = self.__value_rank()

    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank < other.rank

        return (self.rank, tuple(card_strength[card] for card in self.cards)) < \
               (other.rank, tuple(card_strength[card] for card in other.cards))

    def __str__(self) -> str:
        return f"Hand - {self.cards} {self.bid} {self.rank}"

    def __value_rank(self):
        dict = {}
        for card in self.cards:
            dict[card] = dict.get(card, 0)+1
        jokers = dict.pop('J', 0)
        if len(dict) == 0 and jokers == 5:
            return 7
        values = sorted(dict.values(), reverse=True)
        values[0] += jokers
        match values:
            case [5]:
                return 7
            case [4, _]:
                return 6
            case [3, 2]:
                return 5
            case [3, 1, 1]:
                return 4
            case [2, 2, 1]:
                return 3
            case [2, 1, 1, 1]:
                return 2
            case _:
                return 1


def calc_total_bid(hands: list):
    total = 0
    for n, hand in enumerate(hands):
        total += hand.bid*(n+1)
    return total


with open('data.txt', 'r') as f:
    hands = [Hand(line.strip()) for line in f]

hands.sort()
print(calc_total_bid(hands))
