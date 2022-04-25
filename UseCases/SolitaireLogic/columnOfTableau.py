from UseCases.General.BlankDeck import BlankDeck
from UseCases.General.DefaultCard import DefaultCard
from CardDataAccess.CardDataAccess import CardInfo
from Infrastructure.ListHelper import isNextElement

class ColumnOfTableau(BlankDeck):
    reverseRanksSequence = CardInfo.ranks.reverse()
    KingCode = 0
    def __init__(self):
        super(ColumnOfTableau, self).__init__()

    def appendCard(self, card: DefaultCard):
        if card.isStatsVisible == False:
            super(ColumnOfTableau, self).appendCard(card)
            return True

        if self.isBlank() and card.rank == self.reverseRanksSequence[self.KingCode]:
            super(ColumnOfTableau, self).appendCard(card)
            return True

        if self.getCards()[-1].isRed() != card.isRed() and \
                isNextElement(self.reverseRanksSequence, self.getCards(), card.rank):
            super(ColumnOfTableau, self).appendCard(card)
            return True
        return False

    def appendCards(self, cards: list):
        if self.isBlank() and \
                cards[self.KingCode].rank == self.reverseRanksSequence[self.KingCode]:
            super(ColumnOfTableau, self).appendCards(cards)
            return True

        if self.getCards()[-1].isRed() != cards[0].isRed() and \
                isNextElement(self.reverseRanksSequence, self.getCards(), cards[0].rank):
            super(ColumnOfTableau, self).appendCards(cards)
            return True
        return False

    def popCard(self, index:int):
        if index == len(self.getCards()-1):
            return super(ColumnOfTableau, self).popCard(index)
        else:
            tmp = self.getCards()
            upPiece = tmp[:index]
            downPiece = tmp[index:]
            self.setCards(upPiece)
            return downPiece
