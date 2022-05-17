from UseCases.General.EmptyDeck import EmptyDeck
from Entities.Card import Card

class StockPile(EmptyDeck):
    def __init__(self):
        super(StockPile, self).__init__()

    def append(self, card: Card):
        super().append(card)
        if card.isStatsVisible:
            card.flip()

