from Entities.Card import *
from random import randint as rn


class Deck:
    def __init__(self, cards):
        self._cards = cards

    def makeRandomSequence(self):
        tmp = []
        length = len(self._cards)
        while length>0:
            index = rn(0, length-1)
            tmp.append(self._cards.pop(index))
            length = len(self._cards)
        self._cards = tmp

    def appendCard(self, card: Card):
        if isinstance(card, Card):
            self._cards.append(card)
            return True
        return False

    def appendCards(self, cards: list):
        for card in cards:
            self.appendCard(card)

    def popCard(self, index:int):
        try:
            return self._cards.pop(index)
        except IndexError:
            return None

    def getCards(self):
        return self._cards.copy()

    def setCards(self, cards: list):
        tmp = self.getCards()
        self._cards = []
        try:
            for card in cards:
                self.appendCard(card)
        finally:
            if len(self._cards) == 0:
                self._cards = tmp
                return False
            return True

    def setBlankDeck(self):
        self._cards = []

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        result = ""
        for card in self._cards:
            result += f"{card}; \n"
        return result



