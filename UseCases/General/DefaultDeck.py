from Entities.Deck import Deck
from Infrastructure.DataAccess.CardDataAccess import CardInfo
from UseCases.General.DefaultCard import DefaultCard
from random import randint as rn

class DefaultDeck(Deck):
    def __init__(self, deck=None):
        if deck is None:
            super().__init__([])
        else:
            super().__init__(deck)

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

    def makeDefaultSequence(self):
        for mark in CardInfo.marks:
            for rank in CardInfo.ranks:
                self.append(DefaultCard(rank, mark))

    def makeRandomSequence(self):
        tmp = []
        length = len(self)
        while length > 0:
            index = rn(0, length-1)
            tmp.append(self.pop(index))
            length = len(self)
        self.appendCards(tmp)


