from Entities.Deck import Deck


class EmptyDeck(Deck):
    def __init__(self):
        super().__init__([])

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


