from UseCases.General.DefaultDeck import DefaultDeck
from UseCases.General.DefaultCard import DefaultCard
from Infrastructure.DataAccess.CardDataAccess import CardInfo
from Infrastructure.ListHelper import isNextElement


class FoundationPile(DefaultDeck):
    def __init__(self):
        super(FoundationPile, self).__init__()
        self.cards = CardInfo.ranks
        self.cards = self.cards[::-1]
        self.mark = -1

    def append(self, card: DefaultCard):
        if self.mark == -1 and card.rank == CardInfo.ranks[-1]:
            super().append(card)
            self.mark = card.mark
            return True

        if isNextElement(self.cards, self.getCards(), card.rank):
            super().append(card)
            return True
        return False

    def isCompleted(self):
        if (self.getCards()[-1].rank == CardInfo.ranks[-1]):
            return True
        return False
