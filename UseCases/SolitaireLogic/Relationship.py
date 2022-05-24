

class RelationShip:
    @staticmethod
    def sendCard(card, receiver, sender):
        if receiver.append(card):
            sender.pop(card)

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
