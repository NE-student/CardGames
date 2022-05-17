from Infrastructure.StackIterator import StackIterator
from Entities.Card import *


class Deck:
    def __init__(self, cards):
        self._cards = cards

    def __iter__(self):
        return StackIterator(self._cards)

    def __getitem__(self, item):
        if isinstance(item, int) and not self.isEmpty():
            return self._cards[item]
        return None

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        result = ""
        for card in self._cards:
            result += f"{card}; \n"
        return result

    def append(self, card: Card):
        if isinstance(card, Card):
            self._cards.append(card)
            return True
        return False

    def appendCards(self, cards: list):
        for card in cards:
            self.append(card)

    def popCard(self, index=-1):
        return self._cards.pop(index)

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




