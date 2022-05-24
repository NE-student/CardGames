from UseCases.General.DefaultDeck import DefaultDeck
from Entities.Card import Card

class StockPile(DefaultDeck):
    def __init__(self):
        super(StockPile, self).__init__()

    def append(self, card: Card):
        super().append(card)
        if card.isStatsVisible:
            card.flip()

