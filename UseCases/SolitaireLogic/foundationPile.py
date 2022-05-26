from Entities.Deck import Deck
from UseCases.General.DefaultCard import DefaultCard
from Infrastructure.DataAccess.CardDataAccess import CardInfo
from Infrastructure.ListHelper import isNextElement
from copy import deepcopy


class FoundationPile(Deck):
    def __init__(self, index, deck=None):
        super(FoundationPile, self).__init__(deck)
        self.mark = -1
        self.index = index

    def pop(self, index):
        if len(self) == 1:
            self.mark = -1
        return super(FoundationPile, self).pop(index)

    def isCompleted(self):
        if (self.getCards()[-1].rank == CardInfo.ranks[-1]):
            return True
        return False
