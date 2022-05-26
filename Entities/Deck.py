from Infrastructure.StackIterator import StackIterator
from Entities.Card import *
from random import randint as rn
import copy


class Deck:
    def __init__(self, cards=None):
        self._cards = []
        if cards is not None:
            self.append(cards)

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

    def __copy__(self):
        print('__copy__()')
        return Deck(self)

    def find(self, rank, mark):
        for card in self._cards:
            if rank == card.rank and mark == card.mark.value:
                return card
        return None

    def append(self, T):
        if isinstance(T, Card):
            self._cards.append(T)
            return True
        if isinstance(T, list):
            for item in T:
                self.append(item)
            return True
        if isinstance(T, Deck):
            cards = T.getCards()
            self.append(cards)
            return True
        return False

    def pop(self, T):
        if isinstance(T, Card):
            for i, card in enumerate(self._cards):
                if T == card:
                    return self.pop(i)
        if isinstance(T, int):
            up = self._cards[:T]
            down = self._cards[T:]
            self.clear()
            self.append(up)
            return Deck(down)
        return None

    def getCards(self):
        return self._cards.copy()

    def clear(self):
        self._cards = []

    def isEmpty(self):
        if len(self) == 0:
            return True
        return False

    def makeRandomSequence(self, index = 1):
        for i in range(index):
            tmp = []
            length = len(self)
            while length > 0:
                index = rn(0, length-1)
                tmp.append(self.pop(index))
                length = len(self)
            self.append(tmp)


    def isAllCardsVisible(self):
        for card in self:
            if card.isStatsVisible == False:
                return False
        return True

    def showAllCardsStats(self):
        for card in self:
            if not card.isStatsVisible:
                card.flip()

    def hideAllCardsStats(self):
        for card in self:
            if card.isStatsVisible:
                card.flip()




