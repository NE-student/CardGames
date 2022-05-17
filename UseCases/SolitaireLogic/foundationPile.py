from UseCases.General.EmptyDeck import EmptyDeck
from UseCases.General.DefaultCard import DefaultCard
from Infrastructure.DataAccess.CardDataAccess import CardInfo
from Infrastructure.ListHelper import isNextElement


class FoundationPile(EmptyDeck):
    def __init__(self):
        super(FoundationPile, self).__init__()
        self.mark = -1

    def append(self, card: DefaultCard):
        if self.mark == -1 and card.rank == CardInfo.ranks[0]:
            super().append(card)
            self.mark = card.mark
            return True
        if isNextElement(CardInfo.ranks, self.getCards(), card.rank):
            super().append(card)
            return True
        return False

    def isCompleted(self):
        if (self.getCards()[-1].rank == CardInfo.ranks[-1]):
            return True
        return False
