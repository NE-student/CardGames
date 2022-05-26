from UseCases.SolitaireLogic.SolitaireZone import SolitaireZone
from Infrastructure.ListHelper import isNextElement
from Infrastructure.DataAccess.CardDataAccess import CardInfo
from copy import deepcopy, copy

class SolitaireGamePlay:
    def __init__(self, SolitaireZone):
        self.SolitaireZone = SolitaireZone
        self.stepIndex = -1
        self.Steps = []
        self.addStep()

    def addStep(self):

        step =\
            {
                "StockPile": deepcopy(self.SolitaireZone.StockPile),
               "WastePile": deepcopy(self.SolitaireZone.WastePile),
               "FoundationPiles": deepcopy(self.SolitaireZone.FoundationPiles),
               "ColumnsOfTableau": deepcopy(self.SolitaireZone.ColumnsOfTableau)
            }

        self.Steps = self.Steps[:self.stepIndex+1]
        self.Steps.append(step)
        self.stepIndex +=1

    def undoStep(self):
        if self.stepIndex >= 0:
            self.stepIndex -= 1
            self.setStep()

    def redoStep(self):
        if self.stepIndex <= len(self.Steps):
            self.stepIndex += 1
            self.setStep()

    def setStep(self):
        self.SolitaireZone.ColumnsOfTableau = deepcopy(self.Steps[self.stepIndex]["ColumnsOfTableau"])
        self.SolitaireZone.StockPile = deepcopy(self.Steps[self.stepIndex]["StockPile"])
        self.SolitaireZone.WastePile = deepcopy(self.Steps[self.stepIndex]["WastePile"])
        self.SolitaireZone.FoundationPiles = deepcopy(self.Steps[self.stepIndex]["FoundationPiles"])
        print(self.stepIndex)


    def appendToStockPile(self, deck):
        deck.hideAllCardsStats()
        self.SolitaireZone.StockPile.append(deck)
        self.addStep()

    def appendToWastePile(self, deck):
        if len(deck) == 1:
            deck.showAllCardsStats()
            self.SolitaireZone.WastePile.append(deck)
            self.addStep()

    def appendToFoundationPile(self, deck, index):
        if len(deck) == 1:
            if self.SolitaireZone.FoundationPiles[index].mark == -1 and deck[0].rank == CardInfo.ranks[0]:
                self.SolitaireZone.FoundationPiles[index].append(deck)
                self.SolitaireZone.FoundationPiles[index].mark = deck[0].mark
                self.addStep()
                return True

            if not self.SolitaireZone.FoundationPiles[index].isEmpty() and \
                    isNextElement(CardInfo.ranks, self.SolitaireZone.FoundationPiles[index].getCards(), deck[0].rank):
                self.SolitaireZone.FoundationPiles[index].append(deck)
                self.addStep()
                return True
        return False

    def appendToColumnOfTableau(self, deck, index):
        if len(deck) == 1:

            if self.SolitaireZone.ColumnsOfTableau[index].isEmpty():
                if deck[0].rank == CardInfo.reverseRanksSequence[0]:
                    self.SolitaireZone.ColumnsOfTableau[index].append(deck)
                    self.addStep()
                    return True
                return False

            if not self.SolitaireZone.ColumnsOfTableau[index][-1].isStatsVisible:
                return False

            if self.SolitaireZone.ColumnsOfTableau[index][-1].isRed() != deck[0].isRed() and \
                    isNextElement(CardInfo.reverseRanksSequence, self.SolitaireZone.ColumnsOfTableau[index].getCards(),
                                  deck[0].rank):
                self.SolitaireZone.ColumnsOfTableau[index].append(deck)
                self.addStep()
                return True

        if len(deck) > 1:
            if self.SolitaireZone.ColumnsOfTableau[index].isEmpty() and \
                    deck[0].rank == CardInfo.reverseRanksSequence[0]:
                self.SolitaireZone.ColumnsOfTableau[index].append(deck)
                self.addStep()
                return True

            if self.SolitaireZone.ColumnsOfTableau[index].getCards()[-1].isRed() != deck[0].isRed() and \
                    isNextElement(CardInfo.reverseRanksSequence, self.SolitaireZone.ColumnsOfTableau[index].getCards(),
                                  deck[0].rank):
                self.SolitaireZone.ColumnsOfTableau[index].append(deck)
                self.addStep()
                return True
        return False

    def SendToFoundationPileFromColumnOfTableau(self,  foundationIndex, columnIndex, cardIndex):
        deck = self.SolitaireZone.ColumnsOfTableau[columnIndex].pop(cardIndex)
        if not self.appendToFoundationPile(deck, foundationIndex):
            self.setStep()

    def SendToFoundationPileFromWastePile(self, foundationIndex):
        deck = self.SolitaireZone.WastePile.pop(-1)
        if not self.appendToFoundationPile(deck, foundationIndex):
            self.setStep()

    def SendToFoundationPileFromFoundationPile(self, foundationIndexTo, foundationIndexFrom, cardIndex):
        deck = self.SolitaireZone.FoundationPiles[foundationIndexFrom].pop(cardIndex)
        if not self.appendToFoundationPile(deck, foundationIndexTo):
            self.setStep()

    def SendToColumnOfTableauFromFoundationPile(self, columnIndex, foundationIndex, cardIndex):
        deck = self.SolitaireZone.FoundationPiles[foundationIndex].pop(cardIndex)
        if not self.appendToColumnOfTableau(deck, columnIndex):
            self.setStep()

    def SendToColumnOfTableauFromWastePile(self, columnIndex):
        deck = self.SolitaireZone.WastePile.pop(-1)
        if not self.appendToColumnOfTableau(deck, columnIndex):
            self.setStep()

    def SendToColumnOfTableauFromColumnOfTableau(self, columnIndexTo, columnIndexFrom, cardIndex):
        if columnIndexFrom == columnIndexTo:
            return
        deck = self.SolitaireZone.ColumnsOfTableau[columnIndexFrom].pop(cardIndex)
        if not self.appendToColumnOfTableau(deck, columnIndexTo):
            self.setStep()

    def SendToWastePileFromStockPile(self):
        deck = self.SolitaireZone.StockPile.pop(-1)
        self.appendToWastePile(deck)

    def SendToStockPileFromWastePile(self):
        deck = self.SolitaireZone.WastePile.pop(0)
        self.appendToStockPile(deck)

    def findReciever(self, deck):
        if deck in self.SolitaireZone.ColumnsOfTableau:
            for column in self.SolitaireZone.ColumnsOfTableau:
                if deck == column:
                    return column
        if deck in self.SolitaireZone.FoundationPiles:
            for pile in self.SolitaireZone.FoundationPiles:
                if deck == pile:
                    return pile

    def findCard(self, rank, mark):
        card = None

        for column in self.SolitaireZone.ColumnsOfTableau:
            card = column.find(rank, mark)
            if card is not None:
                return (card, column)

        card = self.SolitaireZone.WastePile.find(rank, mark)
        if card is not None:
            return (card, self.SolitaireZone.WastePile)

        for pile in self.SolitaireZone.FoundationPiles:
            card = pile.find(rank, mark)
            if card is not None:
                return (card, pile)

        return None
