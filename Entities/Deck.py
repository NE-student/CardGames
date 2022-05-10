from Infrastructure.StackIterator import StackIterator
from Entities.Card import *
from random import randint as rn


class Deck:
    def __init__(self, cards):
        self._cards = cards

    def __iter__(self):
        return StackIterator(self._cards)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._cards[item]
        raise IndexError

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        result = ""
        for card in self._cards:
            result += f"{card}; \n"
        return result

    def makeRandomSequence(self):
        tmp = Deck([])
        length = len(self)
        while length > 0:
            index = rn(0, length-1)
            tmp.append(self.popCard(index))
            length = len(self)
        self._cards = tmp.getCards()

    def append(self, card: Card):
        if isinstance(card, Card):
            self._cards.append(card)
            return True
        return False

    def appendCards(self, cards: list):
        for card in cards:
            self.append(card)

    def popCard(self, index: int):
        return self._cards.pop(index)

    def getCards(self):
        return self._cards.copy()

    def setCards(self, cards: list):
        tmp = Deck(self.getCards())
        self._cards = []
        try:
            for card in cards:
                self.append(card)
        finally:
            if len(self) == 0:
                self._cards = tmp.getCards()
                return False
            return True

    def setBlankDeck(self):
        self._cards = []




