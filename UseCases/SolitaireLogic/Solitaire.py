from Entities.Game import Game
from UseCases.SolitaireLogic.Tableau import Tableau
from UseCases.SolitaireLogic.stockNwastePiles import StockAndWasteRelationship
from UseCases.SolitaireLogic.foundationPile import FoundationPile
from UseCases.General.BlankDeck import BlankDeck
from UseCases.General.StartDeck import StartDeck
from random import randint as rn


class Solitaire(Game):
    def __init__(self):
        self.tableau = Tableau()
        self.snw = StockAndWasteRelationship()
        self.foundationPiles = [FoundationPile() for i in range(4)]
        self.startDeck = BlankDeck()

    def start(self):
        self.startDeck = StartDeck()
        self.startDeck.makeRandomSequence()
        self.startDeck.toggleDeck()

        for i in range(len(self.tableau.columns)):
            for j in range(i):
                card = self.startDeck.popCard(rn(0, len(self.startDeck.getCards())))
                self.tableau.columns[i].appendCard(card)
            card = self.startDeck.popCard(rn(0, len(self.startDeck.getCards())))
            card.flip()
            self.tableau.columns[i].appendCard(card)

        self.snw.stock.setCards(self.startDeck.getCards())

        self.startDeck = BlankDeck()


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

