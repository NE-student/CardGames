from UseCases.SolitaireLogic.stockPile import StockPile
from UseCases.SolitaireLogic.wastePile import WastePile

class StockAndWasteRelationship:
    def __init__(self, stock, waste):
        self.stock = stock
        self.waste = waste

    def flipCardFromStockPile(self):
        card = self.stock.pop()
        if card is not None:
            self.waste.append(card)
            return True
        return False

    def restart(self):
        if self.stock.isEmpty() and not self.waste.isEmpty():
            cards = self.waste.clear()
            self.stock.appendCards(cards)