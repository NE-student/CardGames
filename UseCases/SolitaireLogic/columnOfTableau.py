from UseCases.General.DefaultDeck import DefaultDeck
from Entities.Card import Card
from UseCases.General.DefaultCard import DefaultCard
from Infrastructure.DataAccess.CardDataAccess import CardInfo
from Infrastructure.ListHelper import isNextElement


class ColumnOfTableau(DefaultDeck):
    reverseRanksSequence = CardInfo.ranks
    KingCode = 0

    def __init__(self):
        super(ColumnOfTableau, self).__init__()
        self.reverseRanksSequence.reverse()

    def append(self, card: DefaultCard, permanently=False):
        if permanently:
            super(ColumnOfTableau, self).append(card)
            return True
        if not card.isStatsVisible:
            super(ColumnOfTableau, self).append(card)
            return True

        if self.isEmpty() or card.rank == self.reverseRanksSequence[self.KingCode]:
            super(ColumnOfTableau, self).append(card)
            return True

        if self.getCards()[-1].isRed() != card.isRed() and \
                isNextElement(self.reverseRanksSequence, self.getCards(), card.rank):
            super(ColumnOfTableau, self).append(card)
            return True
        return False

    def showLastCard(self):
        if self[-1] is not None and not self[-1].isStatsVisible:
            self[-1].flip()

    def appendCards(self, cards: list):
        if self.isEmpty() and \
                cards[self.KingCode].rank == self.reverseRanksSequence[self.KingCode]:
            super(ColumnOfTableau, self).appendCards(cards)
            return True

        if self.getCards()[-1].isRed() != cards[0].isRed() and \
                isNextElement(self.reverseRanksSequence, self.getCards(), cards[0].rank):
            super(ColumnOfTableau, self).appendCards(cards)
            return True
        return False

    def pop(self, index:int):
        if isinstance(index, Card):
            card = super(ColumnOfTableau, self).pop(index)
            self.showLastCard()
            return card
        if index == -1 or index == len(self.getCards())-1:
            card = super(ColumnOfTableau, self).pop()
            self.showLastCard()
            return card
        else:
            tmp = self.getCards()
            upPiece = tmp[:index]
            downPiece = tmp[index:]
            self.popCards()
            self.appendCards(upPiece)
            self.showLastCard()
            return downPiece
