from UseCases.General.BlankDeck import BlankDeck
from  Entities.Card import Card


class WastePile(BlankDeck):
    def __init__(self):
        super(WastePile, self).__init__()

    def clear(self):
        tmp = self.getCards()
        self.setBlankDeck()
        return tmp

    def appendCard(self, card: Card):
        super().appendCard(card)
        self.toggleAllElements()

    def popLastCard(self):
        return super(WastePile, self).popCard(-1)
