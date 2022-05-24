from UseCases.General.DefaultDeck import DefaultDeck
from Entities.Card import Card


class WastePile(DefaultDeck):
    def __init__(self):
        super(WastePile, self).__init__()

    def clear(self):
        return self.popCards()

    def append(self, card: Card):
        super().append(card)
        if not card.isStatsVisible:
            card.flip()
