from UseCases.General.BlankDeck import BlankDeck


class StockPile(BlankDeck):
    def __init__(self, cards):
        super(StockPile, self).__init__()
        self.setCards(cards)
        self.toggleDeck()

    def popLastCard(self):
        return super(StockPile, self).popCard(-1)
