from UseCases.General.BlankDeck import BlankDeck


class StockPile(BlankDeck):
    def __init__(self):
        super(StockPile, self).__init__()

    def popLastCard(self):
        return super(StockPile, self).popCard(-1)
