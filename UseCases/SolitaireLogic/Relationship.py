from UseCases.General.DefaultDeck import DefaultDeck

class RelationShip:
    @staticmethod
    def sendCard(card, receiver, sender):
        index = RelationShip.findCardIndex(sender, card)
        deck = sender.copy()
        card = deck.pop(index)
        if isinstance(card, list):
            if receiver.appendCards(card):
                sender.pop(index)
        else:
            if receiver.append(card):
                sender.pop(index)


    @staticmethod
    def findCardIndex(deck, card):
        for i, item in enumerate(deck):
            if item == card:
                return i
        return None

    @staticmethod
    def findCard(Solitaire, rank, mark):
        card = None

        for column in Solitaire.tableau.columns:
            card = column.find(rank, mark)
            if card is not None:
                return (card, column)

        card = Solitaire.waste.find(rank, mark)
        if card is not None:
            return (card, Solitaire.waste)

        for pile in Solitaire.foundationPiles:
            card = pile.find(rank, mark)
            if card is not None:
                return (card, pile)

        return None
