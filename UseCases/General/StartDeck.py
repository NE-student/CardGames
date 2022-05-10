from Infrastructure.DataAccess.CardDataAccess import CardInfo
from UseCases.General.DefaultCard import DefaultCard
from UseCases.General.BlankDeck import BlankDeck


class StartDeck(BlankDeck):
    def __init__(self):
        super().__init__()
        self.makeDefaultSequence()

    def makeDefaultSequence(self):
        for mark in CardInfo.marks:
            for rank in CardInfo.ranks:
                self.append(DefaultCard(rank, mark))


if __name__ == "__main__":
    da = StartDeck()
    array = da.getCards()
    array.append("Test")
    array.append("Test2")
    da.setCards(array)
    print(str(da))