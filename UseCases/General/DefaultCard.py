from Entities.Card import Card
from Infrastructure.DataAccess.CardDataAccess import CardInfo


class DefaultCard(Card):
    def __init__(self, rank=CardInfo.ranks[0], mark=CardInfo.marks.Clovers):
        super(DefaultCard, self).__init__(rank, mark)

    def isRed(self):
        if self.mark == CardInfo.marks.Hearts or self.mark == CardInfo.marks.Diamonds:
            return True
        return False

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        if value in CardInfo.ranks:
            self._rank = value
            return True
        if value in range(len(CardInfo.ranks)):
            self._rank = CardInfo.ranks[value]
            return True
        return False

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        try:
            self._mark = CardInfo.marks(value)
        except ValueError:
            print(f"Value {value} is not defined, available values is {CardInfo.ranks.getAllValues()}")

if __name__ == "__main__":
    da = DefaultCard()
    da.mark = CardInfo.marks.Hearts
    print(da.mark)
