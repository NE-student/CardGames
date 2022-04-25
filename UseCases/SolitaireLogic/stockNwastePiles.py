from UseCases.SolitaireLogic.stockPile import StockPile
from UseCases.SolitaireLogic.wastePile import WastePile

class StockAndWasteRelationship:
    def __init__(self):
        self.stock = StockPile()
        self.waste = WastePile()

    def flipCardFromStockPile(self):
        card = self.stock.popLastCard()
        if card is not None:
            self.waste.appendCard(card)
            return True
        return False

    def restart(self):
        if self.stock.isBlank() and not self.waste.isBlank():
            cards = self.waste.clear()
            self.stock.setCards(cards)