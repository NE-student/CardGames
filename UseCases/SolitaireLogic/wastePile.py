from UseCases.General.BlankDeck import BlankDeck
from  Entities.Card import Card


class WastePile(BlankDeck):
    def __init__(self):
        super(WastePile, self).__init__()

    def clear(self):
        tmp = self.getCards()
        self.setBlankDeck()
        return tmp

    def append(self, card: Card):
        super().append(card)
        self.toggleAllCards()

    def popLastCard(self):
        return super(WastePile, self).popCard(-1)
