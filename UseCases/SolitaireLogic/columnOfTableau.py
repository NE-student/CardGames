from Entities.Deck import Deck
from Entities.Card import Card
from UseCases.General.DefaultCard import DefaultCard
from Infrastructure.DataAccess.CardDataAccess import CardInfo
from Infrastructure.ListHelper import isNextElement
from copy import deepcopy


class ColumnOfTableau(Deck):

    def __init__(self, index, deck=None):
        super(ColumnOfTableau, self).__init__(deck)
        self.index = index

    def pop(self, T):
        deck = super(ColumnOfTableau, self).pop(T)
        return deck

    def showLastCard(self):
        if self[-1] is not None and not self[-1].isStatsVisible:
            self[-1].flip()
