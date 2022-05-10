from Entities.Deck import Deck


class BlankDeck(Deck):
    def __init__(self):
        super().__init__([])

    def toggleDeck(self):
        self.isAllVisible = not self.isAllVisible
        self.toggleAllCards()

    def toggleAllCards(self):
        cardArray = self.getCards()
        for card in cardArray:
            if card.isStatsVisible is not self.isAllVisible:
                card.flip()
        self.setCards(cardArray)

    def isAllVisible(self):
        for card in self:
            if not card.isStatsVisible:
                return False
        return True

    def isBlank(self):
        if len(self) == 0:
            return True
        return False

