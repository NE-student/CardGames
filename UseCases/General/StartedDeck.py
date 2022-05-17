from Infrastructure.DataAccess.CardDataAccess import CardInfo
from UseCases.General.DefaultCard import DefaultCard
from UseCases.General.EmptyDeck import EmptyDeck
from random import randint as rn


class StartedDeck(EmptyDeck):
    def __init__(self):
        super().__init__()
        self.makeDefaultSequence()

    def makeDefaultSequence(self):
        for mark in CardInfo.marks:
            for rank in CardInfo.ranks:
                self.append(DefaultCard(rank, mark))

    def makeRandomSequence(self):
        tmp = EmptyDeck()
        length = len(self)
        while length > 0:
            index = rn(0, length-1)
            tmp.append(self.popCard(index))
            length = len(self)
        self._cards = tmp.getCards()


if __name__ == "__main__":
    da = StartedDeck()
    array = da.getCards()
    array.append("Test")
    array.append("Test2")
    da.setCards(array)
    print(str(da))