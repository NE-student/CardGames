from Entities.Deck import Deck
from UseCases.General.DefaultCard import DefaultCard
from UseCases.SolitaireLogic.foundationPile import FoundationPile
from UseCases.SolitaireLogic.columnOfTableau import ColumnOfTableau
from Infrastructure.DataAccess.CardDataAccess import CardInfo
from random import randint as rn


class SolitaireZone:
    def __init__(self):
        self.StockPile = Deck()
        self.WastePile = Deck()

        self.FoundationPiles = [FoundationPile(i) for i in range(4)]
        self.ColumnsOfTableau = [ColumnOfTableau(i) for i in range(7)]

        startDeck = Deck()
        for mark in CardInfo.marks:
            for rank in CardInfo.ranks:
                startDeck.append(DefaultCard(rank, mark))
        startDeck.makeRandomSequence(5)
        startDeck.hideAllCardsStats()

        for i in range(len(self.ColumnsOfTableau)):
            for j in range(i):
                card = startDeck.pop(-1)
                self.ColumnsOfTableau[i].append(card)
            card = startDeck.pop(-1)
            card.showAllCardsStats()
            self.ColumnsOfTableau[i].append(card)

        self.StockPile.append(startDeck)


