from Infrastructure.StackIterator import StackIterator
from Entities.Card import *


class Deck:
    def __init__(self, cards):
        self._cards = cards

    def __iter__(self):
        return StackIterator(self._cards)

    def __getitem__(self, item):
        if self.isEmpty():
            return None
        if isinstance(item, int):
            return self._cards[item]
        return None

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        result = ""
        for card in self._cards:
            result += f"{card}; \n"
        return result

    def find(self, rank, mark):
        for card in self._cards:
            if rank == card.rank and mark == card.mark.value:
                return card
        return None

    def append(self, card: Card):
        if isinstance(card, Card):
            self._cards.append(card)
            return True
        return False

    def appendCards(self, cards: list):
        for card in cards:
            self.append(card)

    def pop(self, index=-1):
        if isinstance(index, Card):
            for i, card in enumerate(self._cards):
                if index == card:
                    return self._cards.pop(i)
        if isinstance(index, int):
            return self._cards.pop(index)
        return None

    def popCards(self):
        tmp = self.getCards()
        self._cards = []
        return tmp

    def getCards(self):
        return self._cards.copy()

    def isEmpty(self):
        if len(self) == 0:
            return True
        return False




