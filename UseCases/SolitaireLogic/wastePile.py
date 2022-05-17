from UseCases.General.EmptyDeck import EmptyDeck
from Entities.Card import Card


class WastePile(EmptyDeck):
    def __init__(self):
        super(WastePile, self).__init__()

    def clear(self):
        return self.popCards()

    def append(self, card: Card):
        super().append(card)
        if not card.isStatsVisible:
            card.flip()
