from Entities.Deck import Deck


class BlankDeck(Deck):
    def __init__(self):
        super().__init__([])
        self.isAllVisible = True

    def toggleDeck(self):
        self.isAllVisible = not self.isAllVisible
        self.toggleAllElements()

    def toggleAllElements(self):
        cardArray = self.getCards()
        for card in cardArray:
            if card.isStatsVisible is not self.isAllVisible:
                card.flip()
        self.setCards(cardArray)

    def isBlank(self):
        if len(self.getCards()) == 0:
            return True
        return False
