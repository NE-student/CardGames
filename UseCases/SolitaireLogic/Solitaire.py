from Entities.Game import Game
from UseCases.SolitaireLogic.Tableau import Tableau
from UseCases.SolitaireLogic.stockNwastePiles import StockAndWasteRelationship
from UseCases.SolitaireLogic.stockPile import StockPile
from UseCases.SolitaireLogic.wastePile import WastePile
from UseCases.SolitaireLogic.foundationPile import FoundationPile
from UseCases.General.DefaultDeck import DefaultDeck
from UseCases.SolitaireLogic.Relationship import RelationShip
from random import randint as rn


class Solitaire(Game):
    def __init__(self):
        self.tableau = Tableau()
        self.stock = StockPile()
        self.waste = WastePile()
        self.snw = StockAndWasteRelationship(self.stock, self.waste)
        self.foundationPiles = [FoundationPile() for i in range(4)]
        self.startDeck = None
        self.RelationShip = RelationShip()

    def start(self):
        self.startDeck = DefaultDeck()
        self.startDeck.makeDefaultSequence()
        self.startDeck.makeRandomSequence()
        self.startDeck.hideAllCardsStats()

        for i in range(len(self.tableau.columns)):
            for j in range(i):
                index = rn(0, len(self.startDeck)-1)
                card = self.startDeck.pop(index)
                self.tableau.columns[i].append(card, True)
            index = rn(0, len(self.startDeck) - 1)
            card = self.startDeck.pop(index)
            card.flip()
            self.tableau.columns[i].append(card, True)

        self.snw.stock.appendCards(self.startDeck.getCards())
        self.startDeck = DefaultDeck()

    def resume(self):
        pass

    def pause(self):
        pass

    def exit(self):
        pass

    def save(self):
        pass

    def load(self):
        pass


if __name__ == "__main__":
    game = Solitaire()
    game.start()
    print(game.tableau)